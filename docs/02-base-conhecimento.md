# Base de Conhecimento

## Dados Utilizados
O Nexus Din utiliza arquivos estruturados armazenados na pasta `data` para contextualizar o atendimento, registrar informações financeiras, consultar regras de planejamento e acompanhar a evolução das metas do usuário.

Os dados são separados por finalidade para reduzir a mistura entre:

* dados pessoais do usuário;
* dados financeiros;
* conteúdo educacional;
* parâmetros de cálculo;
* regras de segurança;
* informações sobre investimentos.

| Arquivo                       | Formato | Utilização no Agente                                                                                                                                      |
| ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `perfil_cliente.json`         | JSON    | Armazenar informações gerais do usuário, como faixa etária, situação profissional, dependentes, estabilidade da renda e nível de conhecimento financeiro. |
| `situacao_financeira.json`    | JSON    | Registrar renda líquida, despesas essenciais, despesas não essenciais, patrimônio, reserva atual e capacidade mensal de poupança.                         |
| `metas_financeiras.json`      | JSON    | Armazenar metas de curto, médio e longo prazo, incluindo valor, prazo, prioridade, valor acumulado e status.                                              |
| `dividas.json`                | JSON    | Registrar dívidas, parcelas, taxas de juros, saldo devedor, prazo restante e prioridade de quitação.                                                      |
| `transacoes.csv`              | CSV     | Analisar padrões de receitas e despesas, frequência de gastos e possíveis categorias com margem para ajuste.                                              |
| `historico_atendimento.json`  | JSON    | Contextualizar interações anteriores e evitar que o usuário precise repetir informações já fornecidas.                                                    |
| `historico_aportes.csv`       | CSV     | Acompanhar os aportes realizados em cada meta financeira.                                                                                                 |
| `perfil_investidor.json`      | JSON    | Registrar objetivo, prazo, necessidade de liquidez, experiência, tolerância a perdas e perfil de risco, quando aplicável.                                 |
| `categorias_financeiras.json` | JSON    | Padronizar categorias de receitas, despesas, dívidas, reservas e metas.                                                                                   |
| `regras_planejamento.json`    | JSON    | Armazenar regras utilizadas para avaliar viabilidade, priorização, reserva de emergência e comprometimento da renda.                                      |
| `parametros_simulacao.json`   | JSON    | Armazenar parâmetros permitidos para simulações, como inflação hipotética, taxas de retorno e margens de segurança.                                       |
| `fontes_conhecimento.json`    | JSON    | Catalogar livros, artigos, documentos oficiais, autores, instituições, temas e referências da base de conhecimento.                                       |
| `conteudos_educacionais.json` | JSON    | Disponibilizar explicações sobre orçamento, juros, inflação, crédito, investimentos e comportamento financeiro.                                           |
| `regras_seguranca.json`       | JSON    | Definir proibições, alertas, dados sensíveis e situações em que o agente deve limitar ou interromper uma orientação.                                      |
| `produtos_financeiros.json`   | JSON    | Armazenar informações educacionais sobre categorias de produtos financeiros, sem realizar recomendação automática de produto específico.                  |


> [!IMPORTANT]
> O arquivo `produtos_financeiros.json` não deve ser utilizado como catálogo comercial nem como mecanismo automático de recomendação. Qualquer análise deve considerar objetivo, prazo, liquidez, situação financeira, conhecimento e tolerância ao risco.

---

## Organização Recomendada da Pasta `data`

```text
data/
├── clientes/
│   ├── perfil_cliente.json
│   ├── situacao_financeira.json
│   ├── metas_financeiras.json
│   ├── dividas.json
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   └── historico_aportes.csv
│
├── conhecimento/
│   ├── fontes_conhecimento.json
│   ├── conteudos_educacionais.json
│   ├── categorias_financeiras.json
│   └── produtos_financeiros.json
│
├── regras/
│   ├── regras_planejamento.json
│   ├── parametros_simulacao.json
│   └── regras_seguranca.json
│
└── historico/
    └── historico_atendimento.json
```

Essa separação facilita:

* manutenção dos arquivos;
* controle de acesso;
* validação dos dados;
* atualização da base de conhecimento;
* proteção das informações pessoais;
* criação de testes automatizados;
* rastreabilidade das informações usadas nas respostas.

---

## Adaptações nos Dados

Os dados mockados foram modificados e expandidos para atender ao objetivo principal do Nexo Financeiro: realizar planejamento de metas de curto, médio e longo prazo.

As adaptações incluem:

### 1. Inclusão de informações sobre metas

Cada meta passou a conter campos específicos para permitir análise, cálculo e acompanhamento.

Exemplo de estrutura:

```json
{
  "id_meta": "META-001",
  "nome": "Reserva de emergência",
  "categoria": "seguranca_financeira",
  "valor_alvo": 18000.00,
  "valor_acumulado": 4000.00,
  "aporte_mensal_planejado": 700.00,
  "prazo_meses": 20,
  "prioridade": "alta",
  "flexibilidade_prazo": "media",
  "status": "em_andamento",
  "data_inicio": "2026-07-01",
  "data_prevista_conclusao": "2028-02-01"
}
```

### 2. Separação entre despesas essenciais e não essenciais

As transações foram categorizadas para permitir que o agente diferencie:

* gastos indispensáveis;
* gastos ajustáveis;
* parcelas de dívidas;
* aportes financeiros;
* receitas recorrentes;
* receitas variáveis.

Exemplo:

```csv
data,descricao,categoria,tipo,valor,essencial
2026-07-01,Salário,Renda,receita,4200.00,false
2026-07-02,Aluguel,Moradia,despesa,1200.00,true
2026-07-03,Supermercado,Alimentação,despesa,650.00,true
2026-07-05,Streaming,Assinaturas,despesa,55.90,false
2026-07-10,Aporte reserva,Investimentos,aporte,500.00,false
```

### 3. Inclusão de dados sobre dívidas

Os dados foram expandidos para registrar:

* tipo da dívida;
* saldo devedor;
* valor da parcela;
* quantidade de parcelas restantes;
* taxa de juros;
* custo efetivo total, quando disponível;
* situação de atraso;
* prioridade de quitação.

Exemplo:

```json
{
  "id_divida": "DIV-001",
  "tipo": "cartao_credito",
  "instituicao": "Instituição fictícia",
  "saldo_devedor": 3200.00,
  "parcela_mensal": 450.00,
  "parcelas_restantes": 8,
  "taxa_juros_mensal": 8.5,
  "em_atraso": false,
  "prioridade_quitacao": "alta"
}
```

### 4. Inclusão de controle de qualidade

Os arquivos passaram a utilizar campos que facilitam a validação, como:

* identificador único;
* data de criação;
* data de atualização;
* origem da informação;
* nível de confiança;
* status de validação;
* consentimento do usuário;
* versão do registro.

Exemplo:

```json
{
  "origem": "informado_pelo_usuario",
  "data_atualizacao": "2026-07-20",
  "status_validacao": "confirmado",
  "nivel_confianca": "alto"
}
```

### 5. Inclusão de dados ausentes

Quando um valor não é conhecido, o sistema utiliza `null` em vez de inventar uma informação.

Exemplo:

```json
{
  "renda_liquida": 4200.00,
  "despesas_totais": null,
  "reserva_emergencia": 4000.00,
  "taxa_poupanca": null
}
```

O agente deve interpretar `null` como informação não fornecida e solicitar o dado quando ele for necessário para a análise.

### 6. Inclusão de fontes e rastreabilidade

Os conteúdos educacionais foram associados às respectivas fontes.

Exemplo:

```json
{
  "id_conteudo": "EDU-001",
  "tema": "planejamento_de_metas",
  "titulo": "Definição e priorização de objetivos financeiros",
  "conteudo": "As metas devem ser específicas, mensuráveis, priorizadas e compatíveis com a capacidade financeira.",
  "tipo_fonte": "documento_institucional",
  "instituicao": "CFP Board",
  "ano": 2025,
  "referencia": "Guia do processo de planejamento financeiro",
  "data_consulta": "2026-07-20"
}
```

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados pela aplicação no início da sessão ou quando uma funcionalidade específica precisa deles.

A estratégia recomendada é separar o carregamento em três grupos.

#### Dados essenciais da sessão

São carregados no início do atendimento:

* perfil do cliente;
* situação financeira;
* metas;
* dívidas;
* histórico resumido;
* regras de segurança.

#### Dados consultados sob demanda

São carregados somente quando necessários:

* transações;
* histórico completo de aportes;
* perfil de investidor;
* produtos financeiros;
* conteúdos educacionais;
* fontes específicas.

#### Dados de configuração

São carregados durante a inicialização da aplicação:

* categorias financeiras;
* regras de planejamento;
* parâmetros de simulação;
* regras de validação;
* regras de segurança.

Fluxo simplificado:

```text
1. A aplicação inicia a sessão.
2. Os arquivos de configuração são carregados.
3. O perfil financeiro do usuário é recuperado.
4. A intenção da mensagem é identificada.
5. Apenas os dados necessários para aquela intenção são consultados.
6. Os cálculos são realizados pelo motor financeiro.
7. O contexto relevante é enviado ao LLM.
8. A resposta passa pela camada de validação.
9. O resultado é apresentado ao usuário.
```

Exemplo conceitual em Python:

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


perfil = carregar_json(DATA_DIR / "clientes" / "perfil_cliente.json")
situacao = carregar_json(
    DATA_DIR / "clientes" / "situacao_financeira.json"
)
metas = carregar_json(DATA_DIR / "clientes" / "metas_financeiras.json")
transacoes = carregar_csv(DATA_DIR / "clientes" / "transacoes.csv")
```

> [!NOTE]
> Em uma aplicação real, dados financeiros pessoais não devem ser armazenados em arquivos locais sem controles adequados. Recomenda-se utilizar banco de dados protegido, autenticação, criptografia e controle de acesso.

---

### Como os dados são usados no prompt?

Os dados não devem ser inseridos integralmente no prompt em todas as interações.

O agente deve utilizar uma estratégia de contexto dinâmico, na qual apenas as informações relevantes para a pergunta atual são recuperadas e enviadas ao modelo.

Por exemplo:

* perguntas sobre metas utilizam dados de metas, renda, despesas e capacidade de aporte;
* perguntas sobre dívidas utilizam saldo devedor, juros, parcelas e orçamento disponível;
* perguntas sobre investimentos utilizam objetivo, prazo, liquidez, situação financeira e perfil do investidor;
* perguntas sobre gastos utilizam transações categorizadas;
* perguntas conceituais utilizam conteúdos educacionais e fontes da base de conhecimento.

O prompt pode ser dividido em quatro camadas.

### 1. System prompt

Contém as instruções permanentes do agente:

* identidade;
* função;
* tom de voz;
* regras de segurança;
* proibições;
* critérios de validação;
* obrigação de declarar hipóteses;
* obrigação de não inventar dados.

### 2. Contexto do usuário

Contém apenas os dados financeiros necessários para a solicitação atual.

Exemplo:

```text
CONTEXTO FINANCEIRO DO USUÁRIO

Renda líquida mensal: R$ 4.200,00
Despesas essenciais: R$ 2.300,00
Despesas não essenciais: R$ 750,00
Parcelas de dívidas: R$ 450,00
Valor livre estimado: R$ 700,00
Reserva atual: R$ 4.000,00
```

### 3. Conhecimento recuperado

Contém trechos selecionados da base documental.

Exemplo:

```text
CONHECIMENTO RECUPERADO

Tema: Planejamento de metas

Orientação:
Uma meta financeira deve possuir valor, prazo, prioridade,
capacidade de aporte e critérios de acompanhamento.

Fonte:
CFP Board — Processo de planejamento financeiro.
```

### 4. Resultado do motor de cálculos

Contém resultados calculados por funções externas ao modelo.

Exemplo:

```text
RESULTADOS CALCULADOS

Valor restante da meta: R$ 14.000,00
Prazo restante: 20 meses
Aporte mensal necessário: R$ 700,00
Percentual concluído: 22,22%
```

Dessa forma, o LLM fica responsável principalmente por:

* interpretar;
* explicar;
* organizar;
* comparar cenários;
* formular perguntas;
* apresentar o plano.

O LLM não deve ser a única camada responsável por cálculos financeiros ou validação dos dados.

---

## Estratégia de Recuperação de Conhecimento

Para uma versão inicial, a aplicação pode utilizar filtros por:

* tema;
* palavra-chave;
* categoria;
* tipo de orientação;
* prazo;
* nível de risco;
* fonte;
* data de atualização.

Em uma versão mais avançada, pode ser utilizado um sistema de recuperação aumentada por geração, conhecido como RAG.

Fluxo de RAG:

```text
Pergunta do usuário
        ↓
Identificação da intenção
        ↓
Busca na base de conhecimento
        ↓
Seleção dos trechos mais relevantes
        ↓
Montagem do contexto
        ↓
Geração da resposta
        ↓
Validação da resposta
```

O sistema de recuperação deve priorizar:

1. fontes oficiais;
2. documentos regulatórios;
3. artigos científicos;
4. livros reconhecidos;
5. materiais educacionais institucionais;
6. conteúdos secundários previamente validados.

---

## Regras de Uso dos Dados

O agente deve seguir estas regras:

* utilizar somente os dados necessários para responder;
* não inventar valores ausentes;
* não utilizar dados de outro usuário;
* não expor informações financeiras completas sem necessidade;
* identificar a origem de cada dado;
* diferenciar informação confirmada de estimativa;
* verificar a data da última atualização;
* solicitar confirmação quando existirem dados conflitantes;
* não substituir dados recentes por registros antigos;
* não utilizar conteúdo sem fonte em decisões críticas;
* não incluir credenciais ou dados sensíveis no prompt;
* não armazenar senhas, tokens ou códigos de autenticação;
* registrar alterações relevantes realizadas pelo usuário;
* permitir correção e exclusão dos dados.

---

## Tratamento de Dados Conflitantes

Quando existirem valores diferentes para a mesma informação, o agente deve:

1. verificar qual registro é mais recente;
2. analisar a origem dos dados;
3. verificar se o dado foi confirmado pelo usuário;
4. evitar escolher um valor silenciosamente;
5. solicitar confirmação quando a diferença afetar o resultado.

Exemplo:

```text
Encontrei dois valores diferentes para sua renda líquida:

- Registro de junho: R$ 3.800,00
- Registro de julho: R$ 4.200,00

Para esta análise, qual valor representa melhor sua renda atual?
```

---

## Exemplo de Contexto Montado

```text
IDENTIDADE DO AGENTE

Você é o Nexo Financeiro, um assistente de educação e
planejamento financeiro especializado em metas de curto,
médio e longo prazo.

OBJETIVO DA INTERAÇÃO

Avaliar a viabilidade da meta "Reserva de emergência".

DADOS FORNECIDOS PELO USUÁRIO

- Nome: João Silva
- Renda líquida mensal: R$ 4.200,00
- Despesas essenciais: R$ 2.300,00
- Despesas não essenciais: R$ 750,00
- Parcelas de dívidas: R$ 450,00
- Reserva atual: R$ 4.000,00
- Meta financeira: R$ 18.000,00
- Prazo desejado: 20 meses
- Capacidade de aporte declarada: R$ 700,00 por mês

RESULTADOS CALCULADOS

- Saldo mensal estimado: R$ 700,00
- Valor restante da meta: R$ 14.000,00
- Aporte mensal necessário: R$ 700,00
- Percentual já concluído: 22,22%
- Previsão sem rentabilidade: 20 meses

ÚLTIMAS TRANSAÇÕES RELEVANTES

- 02/07/2026: Aluguel — R$ 1.200,00
- 03/07/2026: Supermercado — R$ 650,00
- 05/07/2026: Streaming — R$ 55,90
- 10/07/2026: Aporte para reserva — R$ 500,00
- 15/07/2026: Parcela do cartão — R$ 450,00

CONHECIMENTO RECUPERADO

- Metas financeiras devem possuir valor, prazo, prioridade
  e capacidade de aporte.
- A reserva de emergência deve considerar estabilidade da
  renda, despesas essenciais e riscos pessoais.
- Simulações de rentabilidade não devem ser tratadas como
  garantia de resultado.

REGRAS DA RESPOSTA

- Não inventar dados ausentes.
- Explicar os cálculos de forma acessível.
- Informar que a projeção não considera rentabilidade.
- Apresentar riscos e limitações.
- Não recomendar produto financeiro específico.
- Indicar a necessidade de revisão periódica.

FORMATO ESPERADO

1. Resumo da situação.
2. Diagnóstico de viabilidade.
3. Cálculos utilizados.
4. Plano de ação.
5. Riscos e limitações.
6. Próxima revisão recomendada.
```

---

## Exemplo de Saída Baseada no Contexto

```text
João, sua meta de formar uma reserva de R$ 18.000,00 em
20 meses é compatível com os dados informados.

Você já possui R$ 4.000,00, portanto ainda precisa acumular
R$ 14.000,00.

Sem considerar rentabilidade:

R$ 14.000,00 ÷ 20 meses = R$ 700,00 por mês.

Esse valor corresponde exatamente à sua capacidade mensal
de aporte estimada. Isso significa que a meta é viável, mas
possui pouca margem para imprevistos.

Plano inicial:

- manter aportes mensais de R$ 700,00;
- automatizar o aporte após o recebimento da renda;
- revisar despesas não essenciais;
- acompanhar o progresso mensalmente;
- reavaliar a meta a cada três meses.

A projeção não considera inflação, rentabilidade, redução da
renda ou despesas inesperadas. Caso não seja possível realizar
um aporte completo em determinado mês, o prazo deverá ser
recalculado.
```

---

## Dados Públicos Complementares

Datasets públicos podem ser utilizados para:

* testes de classificação de transações;
* desenvolvimento de categorização automática;
* identificação de padrões de gastos;
* testes de detecção de anomalias;
* criação de exemplos educacionais;
* avaliação técnica do sistema.

Entretanto, datasets públicos não devem ser utilizados para:

* presumir o comportamento individual do usuário;
* determinar automaticamente o perfil de risco;
* recomendar produtos financeiros;
* substituir dados fornecidos pelo cliente;
* reproduzir preconceitos ou padrões discriminatórios;
* tomar decisões financeiras individualizadas sem validação.

> [!TIP]
> Datasets do Hugging Face, Kaggle, Banco Central, Comissão de Valores Mobiliários e portais públicos podem apoiar o desenvolvimento técnico, desde que sua licença, qualidade, finalidade e atualização sejam verificadas.

---

## Limitações da Base de Conhecimento

A base de conhecimento:

* pode conter dados mockados ou simplificados;
* depende da qualidade das informações fornecidas;
* pode ficar desatualizada;
* não representa todos os produtos financeiros disponíveis;
* não substitui bases oficiais em tempo real;
* não garante que os valores simulados ocorrerão;
* não deve ser utilizada isoladamente para decisões críticas;
* não possui acesso automático a contas bancárias;
* não confirma informações externas sem integração específica;
* não substitui profissionais legalmente habilitados.

Sempre que uma informação estiver ausente, desatualizada ou incerta, o agente deve declarar essa limitação antes de oferecer uma conclusão.
