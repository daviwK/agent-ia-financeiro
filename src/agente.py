"""Lógica do agente financeiro Nexus Din.

O arquivo carrega os dados, realiza cálculos simples e conversa
com um modelo local executado pelo Ollama.
"""

import json
from typing import Any

import pandas as pd
from ollama import chat

from config import DATA_DIR, OLLAMA_MODEL, PROMPT_DIR


def carregar_json(nome_arquivo: str) -> dict[str, Any]:
    """Abre um arquivo JSON da pasta data."""
    caminho = DATA_DIR / nome_arquivo

    if not caminho.exists():
        return {}

    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return {}


def carregar_transacoes() -> pd.DataFrame:
    """Abre o arquivo CSV de transações."""
    caminho = DATA_DIR / "transacoes.csv"

    if not caminho.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(caminho)
    except (pd.errors.ParserError, OSError):
        return pd.DataFrame()


def carregar_base() -> dict[str, Any]:
    """Reúne todos os dados usados pela aplicação."""
    return {
        "perfil": carregar_json("perfil_cliente.json"),
        "situacao": carregar_json("situacao_financeira.json"),
        "metas": carregar_json("metas_financeiras.json"),
        "conteudos": carregar_json("conteudos_educacionais.json"),
        "regras": carregar_json("regras_seguranca.json"),
        "transacoes": carregar_transacoes(),
    }


def carregar_system_prompt() -> str:
    """Lê o comportamento principal do agente."""
    caminho = PROMPT_DIR / "system_prompt.txt"

    if not caminho.exists():
        return "Você é o Nexus Din, um agente financeiro educativo."

    return caminho.read_text(encoding="utf-8")


def numero(valor: Any) -> float:
    """Converte um valor para número. Se falhar, retorna zero."""
    try:
        return float(valor or 0)
    except (TypeError, ValueError):
        return 0.0


def formatar_moeda(valor: float) -> str:
    """Transforma 4200.5 em R$ 4.200,50."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def calcular_indicadores(base: dict[str, Any]) -> dict[str, float]:
    """Calcula indicadores sem depender da inteligência artificial."""
    situacao = base.get("situacao", {})

    renda = numero(situacao.get("renda_liquida_mensal"))
    essenciais = numero(situacao.get("despesas_essenciais"))
    nao_essenciais = numero(situacao.get("despesas_nao_essenciais"))
    dividas = numero(situacao.get("parcelas_dividas"))

    total_despesas = essenciais + nao_essenciais + dividas
    saldo = renda - total_despesas
    comprometimento = total_despesas / renda * 100 if renda > 0 else 0

    return {
        "total_despesas": round(total_despesas, 2),
        "saldo_mensal": round(saldo, 2),
        "comprometimento_renda": round(comprometimento, 2),
    }


def montar_contexto(base: dict[str, Any]) -> str:
    """Monta um resumo curto para o modelo local."""
    perfil = base.get("perfil", {})
    situacao = base.get("situacao", {})
    metas = base.get("metas", {}).get("metas", [])
    conteudos = base.get("conteudos", {}).get("conteudos", [])
    regras = base.get("regras", {}).get("regras", [])
    indicadores = calcular_indicadores(base)

    linhas = [
        "DADOS FICTÍCIOS DO CLIENTE",
        f"Nome: {perfil.get('nome', 'Não informado')}",
        f"Conhecimento financeiro: {perfil.get('conhecimento_financeiro', 'Não informado')}",
        f"Renda líquida: {formatar_moeda(numero(situacao.get('renda_liquida_mensal')))}",
        f"Despesas totais: {formatar_moeda(indicadores['total_despesas'])}",
        f"Saldo mensal: {formatar_moeda(indicadores['saldo_mensal'])}",
        f"Reserva atual: {formatar_moeda(numero(situacao.get('reserva_atual')))}",
        "",
        "METAS",
    ]

    if not metas:
        linhas.append("Nenhuma meta cadastrada.")

    for meta in metas:
        alvo = numero(meta.get("valor_alvo"))
        acumulado = numero(meta.get("valor_acumulado"))
        restante = max(alvo - acumulado, 0)
        prazo = int(numero(meta.get("prazo_meses")))
        aporte = restante / prazo if prazo > 0 else 0

        linhas.append(
            f"- {meta.get('nome', 'Sem nome')}: alvo {formatar_moeda(alvo)}, "
            f"acumulado {formatar_moeda(acumulado)}, prazo {prazo} meses, "
            f"aporte estimado {formatar_moeda(aporte)} por mês."
        )

    linhas.extend(["", "CONHECIMENTOS EDUCACIONAIS"])
    for item in conteudos[:5]:
        linhas.append(f"- {item.get('titulo')}: {item.get('conteudo')}")

    linhas.extend(["", "REGRAS DE SEGURANÇA"])
    for regra in regras:
        linhas.append(f"- {regra.get('descricao')}")

    return "\n".join(linhas)


def criar_mensagens(
    pergunta: str,
    base: dict[str, Any],
    historico: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Prepara as mensagens enviadas ao Ollama."""
    mensagens = [
        {"role": "system", "content": carregar_system_prompt()},
        {"role": "system", "content": montar_contexto(base)},
    ]

    # Envia somente as últimas 10 mensagens para evitar contexto muito grande.
    for mensagem in historico[-10:]:
        if mensagem.get("role") in {"user", "assistant"}:
            mensagens.append(
                {
                    "role": mensagem["role"],
                    "content": mensagem.get("content", ""),
                }
            )

    mensagens.append({"role": "user", "content": pergunta})
    return mensagens


def responder(
    pergunta: str,
    base: dict[str, Any],
    historico: list[dict[str, str]],
) -> str:
    """Solicita uma resposta ao modelo local do Ollama."""
    if not pergunta.strip():
        return "Digite uma pergunta para continuar."

    mensagens = criar_mensagens(pergunta, base, historico)

    try:
        resposta = chat(
            model=OLLAMA_MODEL,
            messages=mensagens,
        )
        return resposta["message"]["content"]

    except Exception:
        return (
            "Não consegui conectar ao Ollama. Verifique se ele está instalado, "
            "aberto e se o modelo configurado foi baixado.\n\n"
            f"Modelo configurado: `{OLLAMA_MODEL}`\n\n"
            f"Comando para baixar: `ollama pull {OLLAMA_MODEL}`"
        )
