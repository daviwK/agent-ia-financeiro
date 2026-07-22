# Guia completo do código do Nexus Din

## Objetivo deste guia

Este guia explica o projeto `Nexus Din` desde os elementos mais básicos da linguagem Python até o funcionamento conjunto de Streamlit, Ollama, JSON, CSV e Pandas.

A explicação não presume experiência prévia em programação. Por isso, além de explicar cada linha, o texto apresenta o significado de palavras como `from`, `import`, `def`, `return`, `if`, `not`, `in`, `with`, `try`, `except`, `for`, `as`, `None`, `or`, `and`, `str`, `float`, `dict`, `list`, colchetes, chaves, parênteses, dois-pontos, pontos, vírgulas e operadores.

Ao final de cada arquivo existe uma seção chamada **O que você pode mudar**, com alterações seguras e cuidados para não quebrar o projeto.

---

# 1. Visão geral do projeto

O Nexus Din é um protótipo local de assistente financeiro. Ele utiliza:

- **Python**: linguagem usada para escrever a lógica;
- **Streamlit**: biblioteca que cria a interface no navegador;
- **Ollama**: programa que executa um modelo de linguagem no computador;
- **Pandas**: biblioteca para ler e analisar tabelas;
- **JSON**: formato usado para guardar dados estruturados;
- **CSV**: formato usado para guardar transações em forma de tabela;
- **Markdown**: formatação de textos exibidos na interface e da documentação.

O fluxo principal é:

```text
Arquivos JSON e CSV
        ↓
agente.py carrega os dados
        ↓
Python calcula os indicadores
        ↓
app.py cria a interface Streamlit
        ↓
Usuário envia uma pergunta
        ↓
agente.py monta o contexto e o histórico
        ↓
Ollama gera uma resposta local
        ↓
Streamlit mostra a resposta
```

---

# 2. Estrutura de pastas

```text
nexus_din_ollama_streamlit/
├── src/
│   ├── app.py
│   ├── agente.py
│   ├── config.py
│   └── requirements.txt
├── data/
│   ├── perfil_cliente.json
│   ├── situacao_financeira.json
│   ├── metas_financeiras.json
│   ├── conteudos_educacionais.json
│   ├── regras_seguranca.json
│   └── transacoes.csv
├── prompts/
│   └── system_prompt.txt
├── .gitignore
└── README.md
```

## Significado dos nomes

### `src`

É uma abreviação de *source*, que significa “fonte”. Essa pasta guarda o código-fonte.

### `data`

Significa “dados”. Guarda os dados fictícios usados pelo agente.

### `prompts`

Guarda as instruções fornecidas ao modelo de inteligência artificial.

### `.py`

Extensão de arquivos Python.

### `.json`

Extensão de arquivos JSON.

### `.csv`

Extensão de arquivos de valores separados por vírgula.

### `.txt`

Arquivo de texto puro.

### `.md`

Arquivo Markdown.

---

# 3. Fundamentos de sintaxe necessários

Antes de analisar os arquivos, é importante entender os símbolos mais usados.

## 3.1 Parênteses: `()`

São usados para:

- chamar uma função;
- definir os parâmetros de uma função;
- agrupar expressões;
- quebrar uma instrução longa em várias linhas.

Exemplo:

```python
print("Olá")
```

`print` é a função e `("Olá")` contém o argumento enviado a ela.

## 3.2 Colchetes: `[]`

São usados para:

- criar listas;
- acessar uma posição de uma lista;
- acessar um valor de dicionário pela chave;
- fazer recortes, chamados de *slices*.

Exemplo de lista:

```python
nomes = ["Ana", "Bruno"]
```

Exemplo de acesso:

```python
nomes[0]
```

Retorna `"Ana"`, pois a contagem começa em zero.

## 3.3 Chaves: `{}`

São usadas para criar dicionários e conjuntos.

Dicionário:

```python
cliente = {"nome": "João", "idade": 30}
```

A chave `"nome"` está associada ao valor `"João"`.

## 3.4 Dois-pontos: `:`

Podem indicar:

- início de um bloco após `if`, `for`, `def`, `with`, `try` e `except`;
- separação entre chave e valor de um dicionário;
- anotação de tipo;
- recorte de uma lista.

Exemplos:

```python
if idade >= 18:
    print("Maior de idade")
```

```python
{"nome": "João"}
```

```python
nome: str
```

```python
historico[-10:]
```

## 3.5 Vírgula: `,`

Separa itens, argumentos, variáveis, chaves e valores.

```python
st.metric("Saldo", "R$ 700,00")
```

## 3.6 Ponto: `.`

Acessa um atributo ou método de um objeto.

```python
caminho.exists()
```

`exists` é um método do objeto `caminho`.

## 3.7 Sinal de igual: `=`

Faz uma atribuição.

```python
saldo = 700
```

Leia como: “a variável `saldo` recebe o valor `700`”.

Não significa comparação. Para comparar igualdade, usa-se `==`.

```python
tipo == "despesa"
```

## 3.8 Seta: `->`

Indica o tipo que uma função pretende retornar.

```python
def numero(valor: Any) -> float:
```

Significa que a função pretende retornar um número decimal.

## 3.9 Aspas

Textos são escritos entre aspas.

```python
"Nexus Din"
```

Aspas simples também funcionam:

```python
'Nexus Din'
```

## 3.10 Identação

Python usa espaços no início da linha para indicar que uma instrução pertence a um bloco.

```python
if saldo > 0:
    print("Saldo positivo")
```

A linha `print` possui quatro espaços e pertence ao `if`.

---

# 4. Palavras reservadas e termos usados no projeto

## `from`

Significa “de”. É usado para indicar de qual módulo algo será importado.

```python
from pathlib import Path
```

Leia como: “do módulo `pathlib`, importe `Path`”.

## `import`

Significa importar ou trazer um módulo, objeto ou função para o arquivo atual.

```python
import json
```

Carrega o módulo `json` para que suas funções possam ser usadas.

## `as`

Cria um apelido.

```python
import pandas as pd
```

O módulo `pandas` poderá ser chamado por `pd`.

Também aparece em:

```python
with caminho.open(...) as arquivo:
```

Nesse caso, o arquivo aberto recebe o nome temporário `arquivo`.

## `def`

Define uma função.

```python
def calcular():
```

## `return`

Interrompe a função e devolve um valor.

```python
return saldo
```

## `if`

Cria uma condição: “se”.

```python
if saldo > 0:
```

## `else`

Significa “caso contrário”.

```python
saldo / renda if renda > 0 else 0
```

## `not`

Inverte um valor lógico.

```python
if not caminho.exists():
```

Se `caminho.exists()` for verdadeiro, `not` o transforma em falso. Se for falso, transforma em verdadeiro.

## `in`

Verifica pertencimento ou é usado para percorrer uma coleção.

```python
if role in {"user", "assistant"}:
```

```python
for meta in metas:
```

## `for`

Cria uma repetição.

```python
for meta in metas:
```

Leia como: “para cada `meta` dentro de `metas`”.

## `with`

Cria um contexto controlado. É muito usado para abrir arquivos ou componentes temporários.

```python
with caminho.open(...) as arquivo:
```

O Python fecha o arquivo automaticamente ao sair do bloco.

## `try`

Significa “tente executar”.

## `except`

Define o que fazer se o bloco `try` causar uma exceção.

## `or`

Retorna o primeiro valor considerado verdadeiro.

```python
valor or 0
```

Se `valor` estiver vazio ou for `None`, será utilizado `0`.

## `and`

Exige que duas condições sejam verdadeiras. Não aparece muito no código atual, mas é importante.

```python
if renda > 0 and prazo > 0:
```

## `None`

Representa ausência de valor.

## `True` e `False`

Representam verdadeiro e falso em Python.

## `str`

Tipo texto.

## `int`

Tipo número inteiro.

## `float`

Tipo número decimal.

## `dict`

Tipo dicionário.

## `list`

Tipo lista.

## `Any`

Indica que o valor pode ser de qualquer tipo.

---

# 5. Explicação completa de `config.py`

Código original:

```python
"""Configurações simples do Nexus Din."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROMPT_DIR = BASE_DIR / "prompts"

# Modelo local usado pelo Ollama.
# Para trocar, altere este valor e baixe o modelo com: ollama pull nome_do_modelo
OLLAMA_MODEL = "gemma3:4b"
```

## Linha 1

```python
"""Configurações simples do Nexus Din."""
```

### `"""`

Três aspas iniciam ou encerram uma string multilinha.

Quando aparecem no começo de um arquivo, formam uma **docstring de módulo**, isto é, uma descrição do arquivo.

### `Configurações simples do Nexus Din.`

Texto que explica o objetivo do módulo.

### Efeito prático

Não altera a lógica. Serve para documentação, ferramentas de ajuda e leitores do código.

---

## Linha 3

```python
from pathlib import Path
```

### `from`

Indica a origem da importação.

### `pathlib`

É um módulo da biblioteca padrão do Python. O nome vem de *path library*, isto é, “biblioteca de caminhos”.

Ele ajuda a criar, unir, ler e verificar caminhos de arquivos de maneira compatível com Windows, Linux e macOS.

Não precisa ser instalado com `pip`, porque já acompanha o Python.

### `import`

Pede ao Python para disponibilizar algo no arquivo atual.

### `Path`

É uma classe definida dentro de `pathlib`.

Uma classe funciona como um molde para criar objetos. `Path` cria objetos que representam caminhos.

### Por que não escrever apenas `import pathlib`?

Seria possível:

```python
import pathlib
```

Mas depois seria necessário escrever:

```python
pathlib.Path(...)
```

Com:

```python
from pathlib import Path
```

é possível escrever apenas:

```python
Path(...)
```

### O que você pode mudar

Não deve remover essa linha, pois as linhas seguintes usam `Path`.

---

## Linha 5

```python
BASE_DIR = Path(__file__).resolve().parent.parent
```

### `BASE_DIR`

Nome da variável.

- `BASE` significa base;
- `DIR` é abreviação de *directory*, que significa diretório ou pasta;
- letras maiúsculas indicam, por convenção, uma constante de configuração.

Python não impede a alteração, mas o estilo comunica: “este valor deveria permanecer fixo durante a execução”.

### `=`

Operador de atribuição. A variável à esquerda recebe o resultado da expressão à direita.

### `Path(...)`

Cria um objeto de caminho.

### `__file__`

Variável especial criada pelo Python. Contém o caminho do arquivo que está sendo executado ou importado.

Dentro de `config.py`, aponta para algo parecido com:

```text
C:\projetos\nexus_din\src\config.py
```

Os dois sublinhados antes e depois indicam um nome especial do Python, frequentemente chamado de *dunder*.

### `.resolve()`

`resolve` é um método do objeto `Path`.

- o ponto acessa o método;
- os parênteses chamam o método;
- ele produz um caminho absoluto e normalizado.

### `.parent`

`parent` é uma propriedade que representa a pasta imediatamente acima.

Primeiro `.parent`:

```text
.../nexus_din/src
```

Segundo `.parent`:

```text
.../nexus_din
```

### Resultado

`BASE_DIR` passa a representar a raiz do projeto.

### O que você pode mudar

Normalmente nada. Se mudar a estrutura de pastas, talvez precise ajustar a quantidade de `.parent`.

Exemplo: se `config.py` fosse movido para a raiz, seria necessário usar apenas o caminho do próprio diretório.

---

## Linha 6

```python
DATA_DIR = BASE_DIR / "data"
```

### `DATA_DIR`

Variável que representa a pasta `data`.

### `/`

Quando usado entre objetos `Path` e textos, une partes de um caminho. Não é divisão matemática nesse contexto.

### `"data"`

Nome literal da pasta.

### Resultado

```text
raiz_do_projeto/data
```

### O que você pode mudar

Se renomear a pasta `data`, altere também o texto.

Exemplo:

```python
DATA_DIR = BASE_DIR / "dados"
```

Mas todos os arquivos precisam estar na nova pasta.

---

## Linha 7

```python
PROMPT_DIR = BASE_DIR / "prompts"
```

Funciona da mesma forma que `DATA_DIR`, mas aponta para a pasta de prompts.

### O que você pode mudar

Somente se renomear ou mover a pasta `prompts`.

---

## Linhas 9 e 10

```python
# Modelo local usado pelo Ollama.
# Para trocar, altere este valor e baixe o modelo com: ollama pull nome_do_modelo
```

### `#`

Inicia um comentário de uma linha. O Python ignora tudo depois do `#` naquela linha.

Comentários explicam decisões, instruções e contexto para humanos.

---

## Linha 11

```python
OLLAMA_MODEL = "gemma3:4b"
```

### `OLLAMA_MODEL`

Nome da configuração que guarda o identificador do modelo.

### `"gemma3:4b"`

String com o nome exato do modelo no Ollama.

- `gemma3` é a família do modelo;
- `4b` indica aproximadamente quatro bilhões de parâmetros;
- `:` separa o nome da etiqueta ou variante.

### O que você pode mudar

Pode trocar por um modelo instalado no Ollama:

```python
OLLAMA_MODEL = "qwen3:4b"
```

Depois precisa baixar o mesmo nome:

```bash
ollama pull qwen3:4b
```

Se o nome do código e o modelo instalado não coincidirem, a conexão falhará.

---

# 6. Explicação completa de `agente.py`

## 6.1 Docstring inicial

```python
"""Lógica do agente financeiro Nexus Din.

O arquivo carrega os dados, realiza cálculos simples e conversa
com um modelo local executado pelo Ollama.
"""
```

É uma string multilinha usada como documentação do módulo.

A quebra de linha dentro da string é preservada.

---

## 6.2 Importação de `json`

```python
import json
```

### `import`

Importa um módulo completo.

### `json`

Módulo da biblioteca padrão usado para converter entre:

- texto JSON;
- estruturas Python, como dicionários e listas.

Depois da importação, suas funções são acessadas pelo prefixo:

```python
json.load(...)
```

### O que você pode mudar

Não remova enquanto o projeto usar arquivos JSON.

---

## 6.3 Importação de `Any`

```python
from typing import Any
```

### `typing`

Módulo da biblioteca padrão voltado para anotações de tipos.

### `Any`

Representa “qualquer tipo”.

É útil porque os dicionários JSON podem conter textos, números, listas, valores booleanos e outros dicionários.

### O que você pode mudar

Pode remover as anotações de tipo, mas isso reduz a clareza. Não altera diretamente a execução normal.

---

## 6.4 Importação do Pandas

```python
import pandas as pd
```

### `pandas`

Biblioteca externa usada para manipular tabelas.

Precisa ser instalada por `pip`.

### `as`

Cria um apelido.

### `pd`

Apelido convencional para `pandas`.

Assim:

```python
pd.read_csv(...)
```

é equivalente a:

```python
pandas.read_csv(...)
```

### O que você pode mudar

Não é recomendado trocar o apelido, pois `pd` é padrão na comunidade. Se trocar, precisa alterar todas as ocorrências.

---

## 6.5 Importação do chat do Ollama

```python
from ollama import chat
```

### `ollama`

Biblioteca Python que conversa com o serviço local do Ollama.

### `chat`

Função que envia uma lista de mensagens ao modelo.

### Por que usar `from`?

Porque somente a função `chat` é necessária.

A alternativa seria:

```python
import ollama
```

E depois:

```python
ollama.chat(...)
```

### O que você pode mudar

Não remova sem substituir a integração com outra ferramenta.

---

## 6.6 Importação das configurações

```python
from config import DATA_DIR, OLLAMA_MODEL, PROMPT_DIR
```

### `config`

Nome do arquivo `config.py` sem a extensão `.py`.

### Itens após `import`

Três variáveis são importadas:

- `DATA_DIR`;
- `OLLAMA_MODEL`;
- `PROMPT_DIR`.

### Vírgulas

Separam os nomes importados.

### O que você pode mudar

Se renomear `config.py`, precisará alterar `from config`.

---

# 7. Função `carregar_json`

Código:

```python
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
```

## Cabeçalho

```python
def carregar_json(nome_arquivo: str) -> dict[str, Any]:
```

### `def`

Inicia a definição de uma função.

### `carregar_json`

Nome escolhido para a função.

### `(` e `)`

Delimitam os parâmetros recebidos.

### `nome_arquivo`

Variável local que receberá o nome do arquivo.

### `: str`

Anotação de tipo: espera-se um texto.

### `-> dict[str, Any]`

Anotação do retorno.

- `dict` significa dicionário;
- `[str, Any]` indica chaves de texto e valores de qualquer tipo.

### `:` final

Inicia o bloco indentado da função.

---

## Docstring da função

```python
"""Abre um arquivo JSON da pasta data."""
```

É uma descrição da função. Pode ser exibida por ferramentas de ajuda.

---

## Construção do caminho

```python
caminho = DATA_DIR / nome_arquivo
```

- `caminho` é uma variável local;
- `DATA_DIR` aponta para a pasta de dados;
- `/` une o diretório ao nome recebido.

Exemplo:

```python
carregar_json("perfil_cliente.json")
```

produz um caminho equivalente a:

```text
.../data/perfil_cliente.json
```

---

## Verificação de existência

```python
if not caminho.exists():
    return {}
```

### `if`

Executa o bloco somente se a condição for verdadeira.

### `caminho.exists()`

- `caminho` é um objeto `Path`;
- `.` acessa o método;
- `exists` verifica se o caminho existe;
- `()` executa o método.

### `not`

Inverte o resultado.

Logo, a condição significa: “se o caminho não existir”.

### `return {}`

Devolve um dicionário vazio e encerra a função.

### Motivo

Evita que o aplicativo pare ao tentar abrir um arquivo ausente.

### Limitação

O erro fica silencioso. O usuário não sabe qual arquivo faltou.

---

## Bloco de tentativa

```python
try:
```

Inicia um bloco que pode causar exceção.

---

## Abertura do arquivo

```python
with caminho.open("r", encoding="utf-8") as arquivo:
```

### `with`

Gerencia o recurso automaticamente.

### `caminho.open(...)`

Abre o arquivo representado pelo objeto `Path`.

### `"r"`

Modo de leitura. A letra vem de *read*.

Outros modos comuns:

- `"w"`: escrita, apagando o conteúdo anterior;
- `"a"`: acrescentar ao final;
- `"rb"`: leitura binária.

### `encoding="utf-8"`

É um argumento nomeado.

- `encoding` é o nome do parâmetro;
- `=` associa o valor;
- `utf-8` define a codificação de caracteres.

Isso evita problemas com `ç`, `ã`, `é` e outros caracteres.

### `as arquivo`

O objeto aberto recebe o nome local `arquivo` dentro do bloco.

### `:`

Inicia o bloco controlado pelo `with`.

---

## Conversão do JSON

```python
return json.load(arquivo)
```

### `json`

Módulo importado.

### `.load`

Função que lê JSON de um arquivo já aberto.

Não confundir:

- `json.load(arquivo)`: lê um arquivo;
- `json.loads(texto)`: lê uma string JSON.

### `return`

Devolve o dicionário ou lista resultante.

---

## Tratamento de exceções

```python
except (json.JSONDecodeError, OSError):
    return {}
```

### `except`

Captura exceções lançadas no `try`.

### Parênteses

Agrupam mais de um tipo de exceção.

### `json.JSONDecodeError`

Ocorre quando o JSON está malformado.

### `OSError`

Categoria de erros relacionados ao sistema operacional e arquivos.

### Resultado

Em qualquer um dos dois casos, retorna dicionário vazio.

---

## O que mudar nessa função

### Melhoria recomendada: mostrar o erro

Em vez de esconder totalmente:

```python
def carregar_json(nome_arquivo: str) -> dict[str, Any]:
    caminho = DATA_DIR / nome_arquivo

    if not caminho.exists():
        print(f"Arquivo não encontrado: {caminho}")
        return {}

    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError as erro:
        print(f"JSON inválido em {nome_arquivo}: {erro}")
        return {}
    except OSError as erro:
        print(f"Erro ao abrir {nome_arquivo}: {erro}")
        return {}
```

### Não mude

- o nome das chaves dos arquivos sem atualizar o código;
- `encoding="utf-8"`;
- o modo `"r"` enquanto a função for somente de leitura.

---

# 8. Função `carregar_transacoes`

```python
def carregar_transacoes() -> pd.DataFrame:
    """Abre o arquivo CSV de transações."""
    caminho = DATA_DIR / "transacoes.csv"

    if not caminho.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(caminho)
    except (pd.errors.ParserError, OSError):
        return pd.DataFrame()
```

## `carregar_transacoes()`

Não recebe parâmetros, por isso os parênteses estão vazios.

## `-> pd.DataFrame`

Indica retorno de um `DataFrame`, estrutura tabular do Pandas.

## `pd.DataFrame()`

Cria uma tabela vazia.

## `pd.read_csv(caminho)`

- `pd`: apelido do Pandas;
- `read_csv`: função de leitura de CSV;
- `caminho`: local do arquivo.

## `pd.errors.ParserError`

Erro gerado quando o Pandas não consegue interpretar a estrutura do CSV.

## O que mudar

### Converter datas e valores explicitamente

```python
df = pd.read_csv(caminho)
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df["valor"] = pd.to_numeric(df["valor"], errors="coerce").fillna(0)
return df
```

### `errors="coerce"`

Converte valores inválidos em `NaT` para datas ou `NaN` para números, em vez de parar o programa.

---

# 9. Função `carregar_base`

```python
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
```

## `return { ... }`

Cria e devolve um dicionário.

Cada linha segue o padrão:

```python
"chave": valor
```

Exemplo:

```python
"perfil": carregar_json("perfil_cliente.json")
```

A função é chamada imediatamente. O resultado é armazenado na chave `perfil`.

## Vírgula final

A última entrada também possui vírgula:

```python
"transacoes": carregar_transacoes(),
```

Python permite e recomenda vírgula final em estruturas multilinha, pois facilita alterações futuras.

## O que mudar

Se criar `dividas.json`, adicione:

```python
"dividas": carregar_json("dividas.json"),
```

Depois será necessário usar `base.get("dividas", {})` em outra parte.

---

# 10. Função `carregar_system_prompt`

```python
def carregar_system_prompt() -> str:
    """Lê o comportamento principal do agente."""
    caminho = PROMPT_DIR / "system_prompt.txt"

    if not caminho.exists():
        return "Você é o Nexus Din, um agente financeiro educativo."

    return caminho.read_text(encoding="utf-8")
```

## `-> str`

A função devolve texto.

## Fallback

O texto retornado quando o arquivo não existe é um **fallback**, ou alternativa de emergência.

## `.read_text`

Método de `Path` que abre, lê e fecha um arquivo de texto em uma única chamada.

## O que mudar

Pode renomear o arquivo, mas precisa alterar:

```python
"system_prompt.txt"
```

O melhor local para mudar personalidade e regras é o próprio arquivo de prompt, não essa função.

---

# 11. Função `numero`

```python
def numero(valor: Any) -> float:
    """Converte um valor para número. Se falhar, retorna zero."""
    try:
        return float(valor or 0)
    except (TypeError, ValueError):
        return 0.0
```

## `valor: Any`

Aceita qualquer tipo.

## `float(...)`

Converte para número decimal.

## `valor or 0`

O operador `or` devolve o primeiro operando considerado verdadeiro.

Valores considerados falsos incluem:

- `None`;
- `0`;
- `""`;
- `False`;
- listas vazias;
- dicionários vazios.

Se `valor` for `None`, a expressão vira `0`.

## `TypeError`

O tipo não pode ser convertido.

## `ValueError`

O tipo pode ser texto, mas o conteúdo não representa número.

Exemplo:

```python
float("abc")
```

## O que mudar

Para não esconder dados inválidos, uma versão mais rigorosa poderia retornar `None` ou lançar erro.

Para iniciante, a versão atual é simples, mas pode mascarar erros ao transformar qualquer problema em zero.

---

# 12. Função `formatar_moeda`

```python
def formatar_moeda(valor: float) -> str:
    """Transforma 4200.5 em R$ 4.200,50."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"
```

## `f"..."`

É uma f-string, string formatada.

Permite inserir expressões dentro de `{}`.

## `{valor:,.2f}`

- `valor`: variável inserida;
- `:`: inicia a especificação de formato;
- `,`: separador de milhar no padrão americano;
- `.2f`: duas casas decimais em ponto flutuante.

`4200.5` vira inicialmente:

```text
4,200.50
```

## `.replace`

Substitui trechos de texto.

As chamadas são encadeadas porque cada `.replace` devolve uma nova string.

1. vírgula vira `X`;
2. ponto vira vírgula;
3. `X` vira ponto.

Resultado:

```text
4.200,50
```

## O que mudar

Pode usar a biblioteca `locale`, mas a configuração depende do sistema. A solução atual é simples e previsível.

---

# 13. Função `calcular_indicadores`

```python
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
```

## `.get("situacao", {})`

Método de dicionário.

- primeiro argumento: chave procurada;
- segundo argumento: valor padrão se a chave não existir.

## Nomes com sublinhado

`nao_essenciais` usa *snake_case*, estilo padrão do Python para variáveis e funções.

## Operadores

- `+`: soma;
- `-`: subtração;
- `/`: divisão;
- `*`: multiplicação;
- `>`: maior que.

## Expressão condicional

```python
total_despesas / renda * 100 if renda > 0 else 0
```

Ordem de leitura:

1. se `renda > 0`;
2. calcule o percentual;
3. caso contrário, use zero.

Isso evita `ZeroDivisionError`.

## `round(valor, 2)`

Arredonda para duas casas decimais.

## O que mudar

Pode acrescentar:

```python
taxa_sobra = saldo / renda * 100 if renda > 0 else 0
```

E no retorno:

```python
"taxa_sobra": round(taxa_sobra, 2),
```

---

# 14. Função `montar_contexto`

Essa função converte os dados em texto para o modelo.

## Recuperação dos dados

```python
perfil = base.get("perfil", {})
situacao = base.get("situacao", {})
metas = base.get("metas", {}).get("metas", [])
conteudos = base.get("conteudos", {}).get("conteudos", [])
regras = base.get("regras", {}).get("regras", [])
```

### Encadeamento de `.get`

```python
base.get("metas", {}).get("metas", [])
```

Primeiro busca o dicionário externo. Depois busca a lista interna.

Se qualquer parte estiver ausente, usa estrutura vazia.

## Lista `linhas`

```python
linhas = [ ... ]
```

Cada elemento será uma linha do contexto.

## F-strings complexas

```python
f"Renda líquida: {formatar_moeda(numero(situacao.get('renda_liquida_mensal')))}"
```

A execução acontece de dentro para fora:

1. `situacao.get(...)` busca o valor;
2. `numero(...)` converte para número;
3. `formatar_moeda(...)` formata;
4. a f-string insere o resultado.

## Acesso com colchetes

```python
indicadores['total_despesas']
```

Acessa uma chave obrigatória. Diferente de `.get`, gera erro se não existir.

Nesse caso é aceitável porque a própria função `calcular_indicadores` sempre cria a chave.

## Linha vazia

```python
""
```

Adiciona uma linha em branco ao texto final.

## Condição de lista vazia

```python
if not metas:
```

Listas vazias são consideradas falsas. `not` transforma em verdadeiro.

## `.append`

Adiciona um item ao final da lista.

```python
linhas.append("Nenhuma meta cadastrada.")
```

## Laço `for`

```python
for meta in metas:
```

A variável `meta` recebe cada dicionário da lista, um por vez.

## `max(alvo - acumulado, 0)`

Retorna o maior valor entre o restante calculado e zero.

Impede valor negativo.

## `int(...)`

Converte para inteiro.

## `.extend`

Adiciona vários itens de uma vez.

```python
linhas.extend(["", "CONHECIMENTOS EDUCACIONAIS"])
```

Diferença:

- `append(lista)` adicionaria a lista como um único item;
- `extend(lista)` adiciona cada elemento separadamente.

## Recorte `conteudos[:5]`

Significa do início até a posição 5, sem incluir a posição 5.

Resultado: no máximo cinco itens.

## `"\n".join(linhas)`

- `"\n"` é o caractere de nova linha;
- `.join` une todos os elementos;
- cada elemento é separado por nova linha.

## O que mudar

A principal melhoria é selecionar conteúdos conforme a pergunta, em vez de sempre usar os cinco primeiros.

---

# 15. Função `criar_mensagens`

```python
def criar_mensagens(
    pergunta: str,
    base: dict[str, Any],
    historico: list[dict[str, str]],
) -> list[dict[str, str]]:
```

## Quebra do cabeçalho em várias linhas

Os parênteses permitem continuar a instrução em novas linhas.

## `list[dict[str, str]]`

Significa lista de dicionários cujas chaves e valores são textos.

## Estrutura inicial

```python
mensagens = [
    {"role": "system", "content": carregar_system_prompt()},
    {"role": "system", "content": montar_contexto(base)},
]
```

Cada mensagem possui:

- `role`: papel;
- `content`: conteúdo.

## `historico[-10:]`

- `-10` começa dez posições antes do final;
- `:` vai até o final.

## Conjunto

```python
{"user", "assistant"}
```

Sem pares de chave e valor, chaves representam um conjunto.

## Acesso obrigatório

```python
mensagem["role"]
```

É usado depois de verificar que `role` existe e possui valor permitido.

## O que mudar

Pode aumentar ou reduzir a quantidade de histórico:

```python
historico[-20:]
```

Mais histórico usa mais memória e pode deixar o modelo lento.

---

# 16. Função `responder`

```python
if not pergunta.strip():
```

## `.strip()`

Remove espaços, tabulações e quebras de linha das extremidades.

Se restar string vazia, `not` será verdadeiro.

## Chamada ao Ollama

```python
resposta = chat(
    model=OLLAMA_MODEL,
    messages=mensagens,
)
```

### Argumentos nomeados

- `model=` informa o modelo;
- `messages=` informa a conversa.

## Resposta aninhada

```python
resposta["message"]["content"]
```

Primeiro acessa `message`, depois `content` dentro dela.

## `except Exception`

Captura qualquer exceção derivada de `Exception`.

É amplo e simples, mas dificulta identificar a causa.

## Strings adjacentes

```python
return (
    "texto 1 "
    "texto 2"
)
```

Python une automaticamente strings literais adjacentes dentro de parênteses.

## `\n\n`

Duas quebras de linha.

## Crases no texto

```python
f"Modelo configurado: `{OLLAMA_MODEL}`"
```

As crases são Markdown e fazem o Streamlit mostrar o conteúdo como código.

## O que mudar

Durante desenvolvimento, capture o erro:

```python
except Exception as erro:
    print(f"Erro do Ollama: {erro}")
```

Não exponha detalhes sensíveis em produção.

---

# 17. Explicação completa de `app.py`

## Importação do Streamlit

```python
import streamlit as st
```

- `streamlit`: biblioteca externa;
- `as st`: apelido padrão.

## Importação entre parênteses

```python
from agente import (
    calcular_indicadores,
    carregar_base,
    formatar_moeda,
    numero,
    responder,
)
```

Parênteses permitem uma importação multilinha.

A vírgula após o último item facilita adicionar outros itens.

## Configuração da página

```python
st.set_page_config(
    page_title="Nexus Din",
    page_icon="💰",
    layout="wide",
)
```

- `st`: módulo Streamlit;
- `.`: acesso à função;
- `set_page_config`: configura a página;
- argumentos nomeados evitam depender da ordem.

## Chamadas sem atribuição

```python
st.title("💰 Nexus Din")
```

A função tem o efeito de desenhar algo na interface. Não é necessário guardar retorno.

## Carregamento dos dados

```python
base = carregar_base()
```

Os parênteses vazios executam a função sem argumentos.

## `with st.sidebar:`

`st.sidebar` é um objeto de contexto. Tudo indentado dentro aparece na barra lateral.

Não possui parênteses porque não está sendo chamado como função nesse uso.

## `st.metric`

Recebe rótulo e valor.

## F-string percentual

```python
f"{indicadores['comprometimento_renda']:.1f}%"
```

- `:.1f`: uma casa decimal;
- `%` fora das chaves é texto literal.

## Desempacotamento de múltiplos valores

```python
aba_chat, aba_metas, aba_transacoes = st.tabs(...)
```

`st.tabs` devolve três objetos. Cada um é atribuído à variável correspondente.

A quantidade de variáveis deve coincidir com a quantidade de abas.

## `session_state`

```python
st.session_state.mensagens
```

`session_state` é uma estrutura persistente durante a sessão do usuário.

O acesso por ponto funciona como alternativa ao acesso por chave:

```python
st.session_state["mensagens"]
```

## Inicialização

```python
if "mensagens" not in st.session_state:
```

Verifica se a chave ainda não existe.

## String entre parênteses

```python
"Olá... "
"seu saldo..."
```

Strings literais adjacentes são unidas automaticamente.

## Exibição de mensagens

```python
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])
```

O papel define o estilo do balão.

## `st.chat_input`

Retorna:

- texto quando o usuário envia;
- `None` quando nada foi enviado.

Por isso:

```python
if pergunta:
```

somente entra quando há conteúdo.

## `.copy()`

Cria uma cópia superficial da lista.

É usada para guardar o histórico anterior antes de acrescentar a pergunta atual.

## Botão

```python
if st.button("Limpar conversa"):
```

`st.button` devolve `True` no clique e `False` nos outros momentos.

## `st.rerun()`

Solicita nova execução do script.

## Correção recomendada do botão

O código atual usa:

```python
st.session_state.mensagens = []
```

Melhor:

```python
del st.session_state.mensagens
st.rerun()
```

### `del`

Remove a variável ou chave. Na próxima execução, o bloco de inicialização recriará a saudação.

## Cálculo do progresso

```python
progresso = min(acumulado / alvo, 1.0) if alvo > 0 else 0
```

`min` escolhe o menor valor. Se a meta ultrapassar 100%, a barra continua em `1.0`.

## Markdown dinâmico

```python
st.markdown(f"### {meta.get('nome', 'Meta sem nome')}")
```

`###` é um título de nível três em Markdown.

## Negrito

```python
st.write(f"**Progresso:** ...")
```

`**texto**` é negrito em Markdown.

## Condição composta

```python
if transacoes is None or transacoes.empty:
```

- `is None`: verifica identidade com ausência de valor;
- `or`: basta uma condição ser verdadeira;
- `.empty`: propriedade do DataFrame que indica tabela sem linhas.

## Filtro Pandas

```python
despesas = transacoes[transacoes["tipo"] == "despesa"]
```

Passos:

1. `transacoes["tipo"]` seleciona a coluna;
2. `== "despesa"` produz uma série de verdadeiros e falsos;
3. `transacoes[...]` mantém somente linhas verdadeiras.

## Agrupamento

```python
despesas.groupby("categoria")["valor"].sum().sort_values(ascending=False)
```

- `groupby`: agrupa;
- `["valor"]`: seleciona a coluna;
- `sum`: soma;
- `sort_values`: ordena;
- `ascending=False`: ordem decrescente.

---

# 18. Arquivos JSON

## Regras de sintaxe JSON

- objetos usam `{}`;
- listas usam `[]`;
- chaves ficam entre aspas duplas;
- chave e valor são separados por `:`;
- itens são separados por vírgula;
- textos usam aspas duplas;
- números não usam aspas;
- booleanos são `true` e `false` em minúsculas;
- ausência de valor é `null`.

## Exemplo

```json
{
  "nome": "João",
  "idade": 30,
  "ativo": true
}
```

## Diferença entre JSON e Python

| JSON | Python |
|---|---|
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

## O que mudar

Pode alterar valores, mas mantenha as chaves usadas pelo código.

Exemplo seguro:

```json
"renda_liquida_mensal": 5000.0
```

Exemplo que quebra a conversão:

```json
"renda_liquida_mensal": "R$ 5.000,00"
```

---

# 19. Arquivo CSV

Cabeçalho:

```csv
data,descricao,categoria,tipo,valor,essencial
```

Cada vírgula separa uma coluna.

Cada nova linha representa uma transação.

## Cuidados

- mantenha os mesmos nomes de coluna;
- use ponto decimal;
- use `despesa` em minúsculas, pois o filtro atual é exato;
- evite vírgulas dentro da descrição sem colocar o campo entre aspas.

Exemplo com vírgula na descrição:

```csv
2026-07-20,"Mercado, produtos de limpeza",Alimentação,despesa,200.00,true
```

---

# 20. `requirements.txt`

```text
streamlit>=1.40
ollama>=0.4
pandas>=2.0
```

## `>=`

Significa “versão maior ou igual”.

## Vantagem

Permite instalar versões mais novas.

## Risco

Uma versão futura pode introduzir incompatibilidade.

## Alternativa reprodutível

Após testar o ambiente:

```bash
pip freeze > requirements.txt
```

Isso grava versões exatas.

---

# 21. `.gitignore`

```text
.venv/
__pycache__/
*.pyc
```

## `.venv/`

Ignora o ambiente virtual.

## `__pycache__/`

Ignora cache do Python.

## `*.pyc`

`*` é curinga. Ignora qualquer arquivo terminado em `.pyc`.

---

# 22. `system_prompt.txt`

Esse arquivo não é código Python. É uma instrução textual enviada ao modelo com papel `system`.

## O que mudar

Pode alterar:

- nome;
- personalidade;
- tom;
- regras;
- formato da resposta;
- limites.

Não coloque dados secretos no prompt.

---

# 23. O que modificar primeiro

## 1. Corrigir o botão de limpeza

```python
if st.button("Limpar conversa"):
    del st.session_state.mensagens
    st.rerun()
```

## 2. Exibir erros de arquivo no terminal

Melhore `carregar_json` e `carregar_transacoes` para imprimir erros durante o desenvolvimento.

## 3. Adicionar validação das colunas do CSV

```python
colunas_obrigatorias = {
    "data", "descricao", "categoria", "tipo", "valor", "essencial"
}

if not colunas_obrigatorias.issubset(df.columns):
    raise ValueError("CSV sem as colunas obrigatórias")
```

## 4. Permitir cadastro pela interface

Criar formulários com `st.form`, `st.number_input` e `st.text_input`.

## 5. Salvar alterações

Hoje os dados são somente lidos. Para salvar, será preciso criar funções de escrita em JSON e CSV.

## 6. Buscar conteúdos por tema

Hoje os cinco primeiros conteúdos são enviados sempre. O ideal é selecionar os mais relevantes para a pergunta.

## 7. Criar proteção programática

Não dependa apenas do prompt para impedir solicitações sensíveis.

---

# 24. Modificações que podem quebrar o projeto

- renomear `config.py` sem atualizar os imports;
- renomear chaves JSON usadas no código;
- escrever números com `R$`;
- trocar `despesa` por `Despesa` sem normalizar;
- colocar nome de modelo não instalado;
- remover o Ollama do `requirements.txt`;
- remover `Path` do import;
- alterar a estrutura das mensagens esperada pelo Ollama;
- apagar a coluna `valor` do CSV;
- usar prazo zero e esperar um cálculo real de aporte.

---

# 25. Glossário final

| Termo | Significado |
|---|---|
| módulo | arquivo ou pacote importável |
| biblioteca | conjunto de módulos e ferramentas |
| classe | molde para criar objetos |
| objeto | valor que possui dados e comportamentos |
| função | bloco reutilizável de instruções |
| método | função associada a um objeto |
| argumento | valor enviado a uma função |
| parâmetro | variável declarada na função |
| retorno | valor devolvido por uma função |
| exceção | erro detectado durante a execução |
| variável | nome que referencia um valor |
| constante | variável que, por convenção, não deve mudar |
| lista | coleção ordenada e mutável |
| dicionário | coleção de pares chave-valor |
| conjunto | coleção sem duplicatas |
| DataFrame | tabela do Pandas |
| string | texto |
| booleano | verdadeiro ou falso |
| contexto | informações fornecidas ao modelo |
| histórico | mensagens anteriores da conversa |
| prompt | instrução textual enviada ao modelo |
| importação | disponibilização de código de outro módulo |
| indentação | espaços que delimitam blocos em Python |
| fallback | alternativa usada quando a opção principal falha |
| API local | interface acessada no próprio computador |

---

# 26. Sequência recomendada de estudo

1. Execute o projeto sem mudar nada.
2. Altere somente os dados JSON.
3. Acrescente uma transação no CSV.
4. Troque o texto da saudação.
5. Troque o modelo do Ollama.
6. Corrija o botão de limpar.
7. Acrescente um indicador simples.
8. Crie um formulário sem salvar.
9. Aprenda a salvar JSON.
10. Implemente busca de conteúdo por tema.
11. Separe cálculos em um novo arquivo.
12. Escreva testes automatizados.

Esse caminho reduz a chance de alterar muitas partes ao mesmo tempo e não saber onde ocorreu o erro.
