# Nexus Din

Assistente financeiro educativo desenvolvido em **Python**, com interface em **Streamlit** e modelo de linguagem executado localmente pelo **Ollama**.

O projeto foi criado como um protótipo simples para:

- visualizar a situação financeira;
- analisar receitas e despesas;
- acompanhar metas;
- estimar aportes mensais;
- consultar conteúdos de educação financeira;
- conversar com uma IA local;
- estudar Python, Streamlit, JSON, CSV e IA generativa.

> [!IMPORTANT]
> Projeto educacional. Não substitui consultoria financeira, contábil, jurídica, tributária ou de investimentos.

---

## Tecnologias

- Python
- Streamlit
- Ollama
- Pandas
- JSON
- CSV
- Git e GitHub

---

## Funcionamento

```text
Usuário abre o aplicativo
        ↓
Streamlit executa src/app.py
        ↓
app.py chama funções de src/agente.py
        ↓
agente.py carrega JSON e CSV
        ↓
Python calcula indicadores financeiros
        ↓
O usuário envia uma pergunta
        ↓
O agente monta o contexto
        ↓
Ollama gera a resposta localmente
        ↓
Streamlit mostra a resposta
```

A IA não lê os arquivos diretamente. O Python carrega, organiza e transforma os dados em texto antes de enviá-los ao Ollama.

---

## Estrutura

```text
agent-ia-financeiro/
├── src/
│   ├── app.py
│   ├── agente.py
│   ├── config.py
│   └── requirements.txt
├── data/
│   ├── perfil_cliente.json
│   ├── situacao_financeira.json
│   ├── metas_financeiras.json
│   ├── transacoes.csv
│   ├── conteudos_educacionais.json
│   └── regras_seguranca.json
├── prompts/
│   └── system_prompt.txt
├── .gitignore
├── README.md
└── LICENSE
```

| Arquivo | Função |
|---|---|
| `src/app.py` | Interface Streamlit |
| `src/agente.py` | Dados, cálculos e comunicação com Ollama |
| `src/config.py` | Caminhos e nome do modelo |
| `src/requirements.txt` | Dependências Python |
| `data/perfil_cliente.json` | Perfil fictício |
| `data/situacao_financeira.json` | Renda, despesas e reserva |
| `data/metas_financeiras.json` | Metas e progresso |
| `data/transacoes.csv` | Receitas, despesas e aportes |
| `data/conteudos_educacionais.json` | Base educacional |
| `data/regras_seguranca.json` | Regras do agente |
| `prompts/system_prompt.txt` | Personalidade e limites |
| `.gitignore` | Arquivos ignorados pelo Git |
| `README.md` | Documentação principal |

---

# Instalação e execução

## Requisitos

Instale:

1. Python 3;
2. Git;
3. Ollama;
4. um modelo local;
5. as bibliotecas do projeto.

---

## 1. Python

Baixe em:

- https://www.python.org/downloads/

No Windows, marque:

```text
Add Python to PATH
```

Teste:

```bash
python --version
```

Ou:

```bash
py --version
```

---

## 2. Git

Baixe em:

- https://git-scm.com/downloads

Teste:

```bash
git --version
```

---

## 3. Ollama

Baixe em:

- https://ollama.com/download

No Windows:

- https://ollama.com/download/windows

Teste:

```bash
ollama --version
```

> [!NOTE]
> O aplicativo Ollama e a biblioteca Python `ollama` são componentes diferentes. Ambos precisam estar instalados.

---

## 4. Clonar o projeto

```bash
git clone https://github.com/SEU-USUARIO/agent-ia-financeiro.git
```

Entre na pasta:

```bash
cd agent-ia-financeiro
```

Troque `SEU-USUARIO` pelo nome da sua conta.

Caso tenha baixado um ZIP, extraia e abra o terminal dentro da pasta.

---

## 5. Ambiente virtual

### Windows — Prompt de Comando

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### Windows — PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Quando ativo, o terminal costuma mostrar:

```text
(.venv)
```

---

## 6. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

---

## 7. Instalar dependências

```bash
python -m pip install -r src/requirements.txt
```

O arquivo deve conter:

```text
streamlit
ollama
pandas
```

Instalação manual:

```bash
python -m pip install streamlit ollama pandas
```

Teste a biblioteca Python do Ollama:

```bash
python -c "import ollama; print('Biblioteca Ollama instalada corretamente')"
```

---

## 8. Baixar o modelo local

O projeto usa inicialmente:

```text
gemma3:4b
```

Baixe:

```bash
ollama pull gemma3:4b
```

Confira:

```bash
ollama list
```

Teste:

```bash
ollama run gemma3:4b
```

Para sair:

```text
/bye
```

O nome deve ser igual ao configurado em `src/config.py`:

```python
OLLAMA_MODEL = "gemma3:4b"
```

---

## 9. Iniciar o Ollama

Normalmente ele inicia automaticamente no Windows.

Caso necessário:

```bash
ollama serve
```

A API local geralmente fica em:

```text
http://localhost:11434
```

---

## 10. Executar o Nexus Din

```bash
python -m streamlit run src/app.py
```

Alternativa:

```bash
streamlit run src/app.py
```

A primeira forma é recomendada porque usa o mesmo Python do ambiente virtual.

Endereço padrão:

```text
http://localhost:8501
```

---

## Comandos rápidos — PowerShell

```powershell
cd C:\caminho\para\agent-ia-financeiro
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r src\requirements.txt
ollama pull gemma3:4b
python -m streamlit run src\app.py
```

## Comandos rápidos — Prompt de Comando

```cmd
cd C:\caminho\para\agent-ia-financeiro
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r src\requirements.txt
ollama pull gemma3:4b
python -m streamlit run src\app.py
```

---

# Como usar

Exemplos:

```text
Quanto sobra da minha renda por mês?
```

```text
Quanto preciso guardar para concluir minha reserva?
```

```text
Minha meta é viável?
```

```text
Quais gastos posso revisar?
```

```text
Explique o que é reserva de emergência.
```

---

# Personalização

## Alterar o perfil

Arquivo:

```text
data/perfil_cliente.json
```

```json
{
  "id_cliente": "CLI-001",
  "nome": "João Silva",
  "idade": 30,
  "situacao_profissional": "assalariado",
  "dependentes": 1,
  "conhecimento_financeiro": "iniciante",
  "origem": "dados_mockados"
}
```

## Alterar renda e despesas

Arquivo:

```text
data/situacao_financeira.json
```

```json
{
  "renda_liquida_mensal": 4200.0,
  "despesas_essenciais": 2300.0,
  "despesas_nao_essenciais": 750.0,
  "parcelas_dividas": 450.0,
  "reserva_atual": 4000.0
}
```

Use:

```json
4200.00
```

Não use:

```json
"R$ 4.200,00"
```

## Adicionar meta

Arquivo:

```text
data/metas_financeiras.json
```

```json
{
  "id_meta": "META-003",
  "nome": "Comprar uma moto",
  "valor_alvo": 25000.0,
  "valor_acumulado": 3000.0,
  "prazo_meses": 30,
  "prioridade": "media",
  "status": "em_planejamento"
}
```

## Adicionar transação

Arquivo:

```text
data/transacoes.csv
```

```csv
2026-07-18,Academia,Saúde,despesa,120.00,false
```

Cabeçalho obrigatório:

```csv
data,descricao,categoria,tipo,valor,essencial
```

Tipos:

```text
receita
despesa
aporte
```

## Trocar modelo

Arquivo:

```text
src/config.py
```

```python
OLLAMA_MODEL = "qwen3:4b"
```

Depois:

```bash
ollama pull qwen3:4b
```

## Alterar comportamento

Arquivo:

```text
prompts/system_prompt.txt
```

Exemplo:

```text
Você é o Nexus Din, um assistente de planejamento financeiro.

Nunca invente dados.

Explique os cálculos de forma simples.

Quando uma meta não for viável, apresente alternativas.
```

---

# Solução de problemas

## `ModuleNotFoundError: No module named 'ollama'`

```bash
python -m pip install ollama
```

Teste:

```bash
python -c "import ollama; print('OK')"
```

Execute:

```bash
python -m streamlit run src/app.py
```

## `No module named 'streamlit'`

```bash
python -m pip install streamlit
```

## `No module named 'pandas'`

```bash
python -m pip install pandas
```

## `ollama` não é reconhecido

```bash
ollama --version
```

Caso não funcione, instale o aplicativo Ollama e reabra o terminal.

## Modelo não encontrado

```bash
ollama pull gemma3:4b
ollama list
```

## Chat não responde

Verifique:

1. Ollama instalado;
2. modelo baixado;
3. nome correto em `config.py`;
4. ambiente virtual ativo;
5. biblioteca Python `ollama` instalada;
6. serviço do Ollama em execução.

Teste:

```bash
ollama run gemma3:4b
```

## Streamlit usando outro Python

```bash
python -c "import sys; print(sys.executable)"
python -m pip list
python -m streamlit run src/app.py
```

## JSON inválido

Correto:

```json
{
  "renda": 4200.00,
  "nome": "João"
}
```

Incorreto:

```json
{
  "renda": "R$ 4.200,00"
  "nome": "João"
}
```

## CSV incorreto

Use o cabeçalho:

```csv
data,descricao,categoria,tipo,valor,essencial
```

Todas as linhas devem ter a mesma quantidade de colunas.

---

# Segurança

Não adicione:

- senhas;
- tokens;
- números completos de cartão;
- códigos de autenticação;
- credenciais bancárias;
- chaves privadas;
- dados financeiros reais de terceiros.

Antes de usar dados reais, implemente:

- autenticação;
- criptografia;
- controle de acesso;
- banco de dados seguro;
- política de privacidade;
- medidas compatíveis com a LGPD.

---

# Limitações

O protótipo ainda não possui:

- cadastro pela interface;
- login;
- banco de dados real;
- múltiplos usuários;
- criptografia;
- categorização automática;
- RAG completo;
- validação avançada;
- sincronização bancária;
- dados em tempo real;
- persistência do chat após fechar o aplicativo.

---

# Próximas melhorias

- formulário de cadastro;
- inclusão de metas pela interface;
- inclusão de transações pela interface;
- persistência com SQLite;
- busca por tema;
- validações;
- testes automatizados;
- relatórios;
- exportação em PDF;
- histórico das metas;
- múltiplos perfis.

---

# Autor

**Davi William**

Projeto para estudo e portfólio em:

- Python;
- inteligência artificial generativa;
- finanças;
- análise de dados;
- Streamlit;
- modelos locais com Ollama.

---

# Licença

Sugestão: licença MIT.

Crie um arquivo `LICENSE` na raiz do projeto.

---

# Referências

- Python: https://www.python.org/
- Streamlit: https://docs.streamlit.io/
- Ollama: https://docs.ollama.com/
- Pandas: https://pandas.pydata.org/docs/
- Git: https://git-scm.com/doc
