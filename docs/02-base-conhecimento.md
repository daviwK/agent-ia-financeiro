# Base de Conhecimento

## Visão Geral

A base de conhecimento do **Nexus Din** foi criada para apoiar o planejamento de metas financeiras de curto, médio e longo prazo.

Os arquivos da pasta `data` utilizam dados fictícios para fins de desenvolvimento, demonstração e testes. Nenhuma informação representa um cliente real.

---

## Estrutura da Pasta `data`

```text
data/
├── perfil_cliente.json
├── situacao_financeira.json
├── metas_financeiras.json
├── transacoes.csv
├── conteudos_educacionais.json
└── regras_seguranca.json
```

Essa estrutura representa a versão inicial do projeto.

Novos arquivos poderão ser adicionados futuramente, como:

- `dividas.json`;
- `perfil_investidor.json`;
- `historico_atendimento.json`;
- `historico_aportes.csv`;
- `produtos_financeiros.json`;
- `fontes_conhecimento.json`;
- `parametros_simulacao.json`;
- `categorias_financeiras.json`.

---

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---|---|---|
| `perfil_cliente.json` | JSON | Armazena informações gerais e contextuais do cliente fictício. |
| `situacao_financeira.json` | JSON | Registra renda, despesas, reserva atual e capacidade mensal de aporte. |
| `metas_financeiras.json` | JSON | Armazena metas, valores, prazos, prioridades e progresso. |
| `transacoes.csv` | CSV | Permite analisar receitas, despesas, aportes e padrões de consumo. |
| `conteudos_educacionais.json` | JSON | Fornece explicações sobre metas, reserva de emergência e planejamento financeiro. |
| `regras_seguranca.json` | JSON | Define limites, proibições e comportamentos obrigatórios do agente. |

> [!IMPORTANT]
> A documentação deve representar apenas arquivos realmente existentes e utilizados pelo código. Arquivos ainda não implementados devem ser classificados como expansão futura.

---

## Conteúdo dos Arquivos

### `perfil_cliente.json`

```json
{
  "id_cliente": "CLI-001",
  "nome": "João Silva",
  "idade": 30,
  "situacao_profissional": "assalariado",
  "dependentes": 1,
  "estabilidade_renda": "alta",
  "conhecimento_financeiro": "iniciante",
  "origem": "dados_mockados",
  "data_atualizacao": "2026-07-20"
}
```

Esse arquivo permite que o agente adapte a comunicação e contextualize o planejamento financeiro.

---

### `situacao_financeira.json`

```json
{
  "id_cliente": "CLI-001",
  "renda_liquida_mensal": 4200.00,
  "despesas_essenciais": 2300.00,
  "despesas_nao_essenciais": 750.00,
  "parcelas_dividas": 450.00,
  "reserva_atual": 4000.00,
  "capacidade_aporte_mensal": 700.00,
  "origem": "dados_mockados",
  "data_atualizacao": "2026-07-20"
}
```

Esse arquivo é utilizado para:

- calcular o saldo mensal;
- verificar a capacidade de poupança;
- avaliar a viabilidade das metas;
- identificar comprometimento da renda;
- apoiar simulações financeiras.

---

### `metas_financeiras.json`

```json
{
  "id_cliente": "CLI-001",
  "metas": [
    {
      "id_meta": "META-001",
      "nome": "Reserva de emergência",
      "categoria": "seguranca_financeira",
      "valor_alvo": 18000.00,
      "valor_acumulado": 4000.00,
      "prazo_meses": 20,
      "aporte_mensal_planejado": 700.00,
      "prioridade": "alta",
      "status": "em_andamento"
    },
    {
      "id_meta": "META-002",
      "nome": "Viagem",
      "categoria": "lazer",
      "valor_alvo": 8000.00,
      "valor_acumulado": 500.00,
      "prazo_meses": 24,
      "aporte_mensal_planejado": 200.00,
      "prioridade": "media",
      "status": "em_planejamento"
    }
  ]
}
```

Esse arquivo permite que o agente:

- organize metas por prazo;
- classifique prioridades;
- calcule valores restantes;
- estime aportes mensais;
- acompanhe o percentual concluído;
- compare metas concorrentes.

---

### `transacoes.csv`

```csv
data,descricao,categoria,tipo,valor,essencial
2026-07-01,Salário,Renda,receita,4200.00,false
2026-07-02,Aluguel,Moradia,despesa,1200.00,true
2026-07-03,Supermercado,Alimentação,despesa,650.00,true
2026-07-05,Conta de energia,Moradia,despesa,180.00,true
2026-07-06,Streaming,Assinaturas,despesa,55.90,false
2026-07-10,Aporte para reserva,Reserva,aporte,500.00,false
2026-07-15,Parcela do cartão,Dívidas,despesa,450.00,true
```

Esse arquivo é utilizado para:

- categorizar entradas e saídas;
- identificar despesas essenciais;
- localizar gastos ajustáveis;
- verificar aportes realizados;
- analisar padrões financeiros.

---

### `conteudos_educacionais.json`

```json
{
  "conteudos": [
    {
      "id": "EDU-001",
      "tema": "metas_financeiras",
      "titulo": "Estrutura de uma meta financeira",
      "conteudo": "Uma meta financeira deve possuir objetivo, valor, prazo, prioridade, valor já acumulado e capacidade mensal de aporte.",
      "tipo": "educacional",
      "fonte": "Base conceitual do Nexo Financeiro"
    },
    {
      "id": "EDU-002",
      "tema": "reserva_emergencia",
      "titulo": "Finalidade da reserva de emergência",
      "conteudo": "A reserva de emergência protege o orçamento contra despesas inesperadas e redução temporária da renda.",
      "tipo": "educacional",
      "fonte": "Base conceitual do Nexo Financeiro"
    },
    {
      "id": "EDU-003",
      "tema": "planejamento",
      "titulo": "Revisão periódica",
      "conteudo": "O planejamento financeiro deve ser revisado quando houver mudanças relevantes na renda, nas despesas, nas dívidas ou nas metas.",
      "tipo": "educacional",
      "fonte": "Base conceitual do Nexo Financeiro"
    }
  ]
}
```

Esse arquivo fornece explicações e orientações educacionais ao agente.

Seu conteúdo deve ser consultado de acordo com o tema da pergunta.

---

### `regras_seguranca.json`

```json
{
  "regras": [
    {
      "id": "SEG-001",
      "descricao": "Nunca inventar valores financeiros ausentes.",
      "acao": "solicitar_informacao"
    },
    {
      "id": "SEG-002",
      "descricao": "Não solicitar senhas, tokens ou códigos de autenticação.",
      "acao": "bloquear_solicitacao"
    },
    {
      "id": "SEG-003",
      "descricao": "Não prometer rentabilidade ou resultado financeiro.",
      "acao": "adicionar_alerta"
    },
    {
      "id": "SEG-004",
      "descricao": "Não recomendar investimentos sem dados mínimos do usuário.",
      "acao": "limitar_resposta"
    },
    {
      "id": "SEG-005",
      "descricao": "Informar quando uma resposta for baseada em hipótese.",
      "acao": "identificar_simulacao"
    }
  ]
}
```

Esse arquivo funciona como uma camada de proteção para reduzir:

- alucinações;
- promessas indevidas;
- uso inadequado de dados;
- recomendações sem contexto;
- solicitações de informações sensíveis.

---

## Adaptações nos Dados

Os dados mockados foram expandidos para representar um cenário financeiro completo e permitir o funcionamento das principais funcionalidades do agente.

As adaptações incluem:

### Metas financeiras estruturadas

Cada meta possui:

- identificador;
- nome;
- categoria;
- valor-alvo;
- valor acumulado;
- prazo;
- aporte mensal;
- prioridade;
- status.

### Separação de despesas

As despesas foram divididas entre:

- essenciais;
- não essenciais;
- dívidas;
- aportes;
- receitas.

### Inclusão de metadados

Os arquivos podem incluir:

- origem;
- data de atualização;
- status de validação;
- nível de confiança;
- versão do registro.

### Tratamento de dados ausentes

Dados desconhecidos devem ser representados com `null`.

Exemplo:

```json
{
  "renda_liquida_mensal": 4200.00,
  "despesas_totais": null,
  "reserva_atual": 4000.00
}
```

O agente não deve substituir valores ausentes por estimativas não declaradas.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados pela aplicação no início da sessão ou quando alguma funcionalidade específica precisa deles.

A estratégia recomendada é separar o carregamento em três grupos.

#### Dados carregados no início da sessão

- perfil do cliente;
- situação financeira;
- metas;
- regras de segurança.

#### Dados consultados sob demanda

- transações;
- conteúdos educacionais;
- histórico;
- perfil de investidor;
- produtos financeiros.

#### Dados de configuração

- categorias;
- parâmetros de simulação;
- regras de planejamento;
- regras de validação.

---

## Exemplo de Carregamento em Python

```python
import json
from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")


def carregar_json(caminho: Path) -> dict:
    if not caminho.exists():
        return {}

    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_csv(caminho: Path) -> pd.DataFrame:
    if not caminho.exists():
        return pd.DataFrame()

    return pd.read_csv(caminho)


perfil = carregar_json(DATA_DIR / "perfil_cliente.json")
situacao = carregar_json(DATA_DIR / "situacao_financeira.json")
metas = carregar_json(DATA_DIR / "metas_financeiras.json")
conteudos = carregar_json(DATA_DIR / "conteudos_educacionais.json")
regras = carregar_json(DATA_DIR / "regras_seguranca.json")
transacoes = carregar_csv(DATA_DIR / "transacoes.csv")
```

---

## Como os Dados São Usados no Prompt?

Os dados não devem ser enviados integralmente ao modelo em todas as interações.

O agente deve montar um contexto dinâmico contendo apenas as informações relevantes para a pergunta atual.

### Perguntas sobre metas

Utilizam:

- renda;
- despesas;
- capacidade de aporte;
- metas;
- prazos;
- prioridades.

### Perguntas sobre gastos

Utilizam:

- transações;
- categorias;
- recorrência;
- despesas essenciais;
- despesas ajustáveis.

### Perguntas sobre investimentos

Utilizam:

- objetivo;
- prazo;
- liquidez;
- situação financeira;
- tolerância ao risco;
- conhecimento financeiro.

### Perguntas educacionais

Utilizam:

- conteúdos educacionais;
- fontes;
- regras de segurança.

---

## Camadas do Prompt

### System prompt

Contém:

- identidade do agente;
- função;
- tom de voz;
- regras permanentes;
- limitações;
- critérios de segurança.

### Contexto financeiro

Contém apenas os dados necessários para a pergunta atual.

### Conhecimento recuperado

Contém trechos relevantes dos conteúdos educacionais.

### Resultados calculados

Contém valores produzidos pelo motor financeiro.

---

## Exemplo de Contexto Montado

```text
IDENTIDADE DO AGENTE

Você é o Nexus Din, um assistente de educação e
planejamento financeiro especializado em metas de curto,
médio e longo prazo.

OBJETIVO DA INTERAÇÃO

Avaliar a viabilidade da meta "Reserva de emergência".

DADOS DO CLIENTE

- Nome: João Silva
- Perfil financeiro: iniciante
- Renda líquida mensal: R$ 4.200,00
- Despesas essenciais: R$ 2.300,00
- Despesas não essenciais: R$ 750,00
- Parcelas de dívidas: R$ 450,00
- Reserva atual: R$ 4.000,00
- Capacidade mensal de aporte: R$ 700,00

META ANALISADA

- Nome: Reserva de emergência
- Valor-alvo: R$ 18.000,00
- Valor acumulado: R$ 4.000,00
- Prazo: 20 meses
- Prioridade: Alta
- Status: Em andamento

RESULTADOS CALCULADOS

- Saldo mensal estimado: R$ 700,00
- Valor restante da meta: R$ 14.000,00
- Aporte mensal necessário: R$ 700,00
- Percentual concluído: 22,22%

CONHECIMENTO RECUPERADO

- Uma meta financeira deve possuir valor, prazo, prioridade,
  valor acumulado e capacidade de aporte.
- O planejamento deve ser revisado quando houver mudanças
  relevantes na renda, nas despesas ou nas metas.

REGRAS DA RESPOSTA

- Não inventar dados ausentes.
- Explicar os cálculos de forma acessível.
- Não prometer rentabilidade.
- Não recomendar produtos financeiros específicos.
- Informar riscos e limitações.
```

---

## Estratégia de Recuperação de Conhecimento

Na primeira versão, a aplicação pode recuperar conteúdos por:

- tema;
- palavra-chave;
- categoria;
- prioridade;
- tipo de orientação.

Exemplo:

```python
def buscar_conteudo_por_tema(base: dict, tema: str) -> list:
    return [
        item
        for item in base.get("conteudos", [])
        if item.get("tema") == tema
    ]
```

Em versões futuras, pode ser implementado um sistema RAG.

```text
Pergunta do usuário
        ↓
Identificação da intenção
        ↓
Busca na base de conhecimento
        ↓
Seleção dos conteúdos relevantes
        ↓
Montagem do contexto
        ↓
Geração da resposta
        ↓
Validação
```

---

## Regras de Uso dos Dados

O agente deve:

- utilizar somente os dados necessários;
- não inventar valores ausentes;
- não misturar dados de clientes diferentes;
- diferenciar valores confirmados de estimativas;
- verificar datas de atualização;
- solicitar confirmação em caso de conflito;
- proteger informações financeiras;
- evitar inserir dados sensíveis no prompt;
- permitir correção e exclusão de registros;
- identificar quando um dado é fictício;
- informar quando uma conclusão depende de hipótese.

---

## Tratamento de Dados Conflitantes

Quando houver valores diferentes para a mesma informação, o agente deve:

1. verificar o registro mais recente;
2. verificar a origem;
3. identificar se o usuário confirmou o valor;
4. evitar escolher silenciosamente;
5. solicitar confirmação quando a diferença afetar o resultado.

Exemplo:

```text
Encontrei dois valores diferentes para sua renda líquida:

- Registro anterior: R$ 3.800,00
- Registro atual: R$ 4.200,00

Qual valor deve ser utilizado nesta análise?
```

---

## Dados Públicos Complementares

Datasets públicos podem ser utilizados para:

- categorização de transações;
- detecção de padrões;
- testes de classificação;
- detecção de anomalias;
- criação de exemplos;
- avaliação técnica.

Possíveis fontes:

- Hugging Face;
- Kaggle;
- Banco Central do Brasil;
- Comissão de Valores Mobiliários;
- Portal Brasileiro de Dados Abertos.

Antes de usar um dataset, devem ser verificados:

- licença;
- origem;
- data de atualização;
- qualidade;
- finalidade;
- presença de dados pessoais;
- possíveis vieses.

Datasets públicos não devem substituir os dados fornecidos pelo usuário em análises personalizadas.

---

## Limitações da Base de Conhecimento

A base de conhecimento:

- utiliza dados fictícios;
- pode conter informações simplificadas;
- depende da qualidade dos dados;
- não acessa contas bancárias;
- não possui atualização automática;
- não representa todos os produtos financeiros;
- não substitui fontes oficiais;
- não garante resultados;
- não substitui profissionais habilitados;
- não deve ser utilizada isoladamente para decisões críticas.

Quando uma informação estiver ausente, desatualizada ou incerta, o agente deve declarar essa limitação antes de apresentar uma conclusão.

---

## Resultado Esperado

Com essa base, o agente deve ser capaz de:

- compreender a situação financeira do cliente;
- analisar metas;
- calcular aportes;
- identificar falta de margem financeira;
- explicar conceitos;
- localizar padrões de gastos;
- respeitar regras de segurança;
- evitar inventar dados;
- gerar respostas personalizadas;
- apresentar limitações com transparência.