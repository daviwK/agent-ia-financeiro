"""Interface do Nexus Din feita com Streamlit."""

import streamlit as st

from agente import (
    calcular_indicadores,
    carregar_base,
    formatar_moeda,
    numero,
    responder,
)
from config import OLLAMA_MODEL


st.set_page_config(
    page_title="Nexus Din",
    page_icon="💰",
    layout="wide",
)

st.title("💰 Nexus Din")
st.caption("Assistente financeiro educativo.")

base = carregar_base()
situacao = base.get("situacao", {})
metas = base.get("metas", {}).get("metas", [])
transacoes = base.get("transacoes")
indicadores = calcular_indicadores(base)

with st.sidebar:
    st.header("Resumo financeiro")
    st.metric(
        "Renda líquida",
        formatar_moeda(numero(situacao.get("renda_liquida_mensal"))),
    )
    st.metric(
        "Despesas totais",
        formatar_moeda(indicadores["total_despesas"]),
    )
    st.metric(
        "Saldo mensal",
        formatar_moeda(indicadores["saldo_mensal"]),
    )
    st.metric(
        "Comprometimento da renda",
        f"{indicadores['comprometimento_renda']:.1f}%",
    )
    st.info(f"Modelo local: {OLLAMA_MODEL}")
    st.warning("Os dados deste protótipo são fictícios.")

aba_chat, aba_metas, aba_transacoes = st.tabs(
    ["Conversar", "Metas", "Transações"]
)

with aba_chat:
    st.subheader("Converse com o Nexus Din")

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": (
                    "Olá! Eu sou o Nexus Din. Posso ajudar a analisar "
                    "seu saldo, suas metas e sua organização financeira."
                ),
            }
        ]

    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

    pergunta = st.chat_input("Digite sua pergunta financeira")

    if pergunta:
        historico_anterior = st.session_state.mensagens.copy()
        st.session_state.mensagens.append(
            {"role": "user", "content": pergunta}
        )

        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            with st.spinner("Analisando com o Ollama..."):
                resposta = responder(pergunta, base, historico_anterior)
                st.markdown(resposta)

        st.session_state.mensagens.append(
            {"role": "assistant", "content": resposta}
        )

    if st.button("Limpar conversa"):
        st.session_state.mensagens = []
        st.rerun()

with aba_metas:
    st.subheader("Metas cadastradas")

    if not metas:
        st.warning("Nenhuma meta encontrada.")

    for meta in metas:
        alvo = numero(meta.get("valor_alvo"))
        acumulado = numero(meta.get("valor_acumulado"))
        restante = max(alvo - acumulado, 0)
        progresso = min(acumulado / alvo, 1.0) if alvo > 0 else 0
        prazo = int(numero(meta.get("prazo_meses")))
        aporte = restante / prazo if prazo > 0 else 0

        st.markdown(f"### {meta.get('nome', 'Meta sem nome')}")
        st.progress(progresso)
        st.write(f"**Progresso:** {progresso * 100:.1f}%")
        st.write(f"**Acumulado:** {formatar_moeda(acumulado)}")
        st.write(f"**Falta:** {formatar_moeda(restante)}")
        st.write(f"**Prazo:** {prazo} meses")
        st.write(f"**Aporte estimado:** {formatar_moeda(aporte)} por mês")
        st.divider()

with aba_transacoes:
    st.subheader("Transações fictícias")

    if transacoes is None or transacoes.empty:
        st.warning("Nenhuma transação encontrada.")
    else:
        st.dataframe(transacoes, use_container_width=True, hide_index=True)

        despesas = transacoes[transacoes["tipo"] == "despesa"]
        if not despesas.empty:
            por_categoria = (
                despesas.groupby("categoria")["valor"]
                .sum()
                .sort_values(ascending=False)
            )
            st.subheader("Despesas por categoria")
            st.bar_chart(por_categoria)

st.divider()
st.caption(
    "Ferramenta educacional. Não substitui consultoria financeira, "
    "contábil, jurídica ou de investimentos."
)
