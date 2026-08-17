# Atividade - Semana 9 - Paradigma Funcional - Elixir

Atividade da disciplina **Paradigmas da Computação**, com foco na aplicação de conceitos do **paradigma funcional** usando **Elixir**.

O trabalho consiste na evolução de um sistema simples de chat em modo texto: uma primeira versão ingênua, e uma segunda versão refatorada aplicando princípios de programação funcional (funções puras, imutabilidade, recursão e separação de responsabilidades).

## Estrutura do diretório

```text
Atividade - Semana 9 - Paradigma Funcional - Elixir/
├── chat.exs        # versão inicial
└── chat v2.exs      # versão refatorada
```

## Objetivo

Evoluir um pequeno sistema funcional aplicando:

- Funções puras
- Imutabilidade
- Recursão
- Separação de responsabilidades

### Restrições da atividade

| Não pode usar | Deve usar |
| --- | --- |
| `IO.gets` | listas de entradas |
| variáveis globais | recursão |
| laços imperativos (`for`, `while`) | funções puras |

Como Elixir não tem `for`/`while` nem variáveis mutáveis, as entradas do chat são simuladas como uma lista fixa processada recursivamente — cada mensagem "digitada" é apenas o próximo elemento da lista.

## `chat.exs` — versão inicial

Versão ingênua, tudo resolvido dentro de uma única função `loop/2`:

- processamento sequencial das entradas (lista fixa, sem `IO.gets`)
- mensagens acumuladas numa lista (`mensagens ++ [entrada]`)
- toda a lista é reimpressa a cada mensagem nova (`Enum.each`)
- encerra ao encontrar `"sair"`

**Limitação:** a função `loop/2` mistura leitura, validação, acúmulo, exibição e encerramento — difícil de estender ou testar isoladamente.

## `chat v2.exs` — versão refatorada

Mesma ideia, com responsabilidades separadas em funções pequenas e uso de *pattern matching* no lugar de `if/else` aninhado.

### Comandos disponíveis

| Comando | Efeito |
| --- | --- |
| `/count` | exibe a quantidade de mensagens armazenadas |
| `/clear` | limpa o histórico de mensagens |
| `sair` | encerra o programa |

### Regras de validação

- a mensagem não pode ser vazia
- no máximo 10 caracteres

### Funções

| Função | Responsabilidade |
| --- | --- |
| `loop/2` | laço principal recursivo — só decide "acabou ou continua" |
| `processar/3` | decide o que fazer com a entrada (comando, mensagem válida ou inválida) via *pattern matching* |
| `valida?/1` | função pura que valida uma mensagem |
| `adicionar/2` | função pura que retorna a lista de mensagens com o novo item |
| `mostrar/1` | exibe a lista de mensagens de forma recursiva, sem `Enum.each` |

```elixir
def valida?(msg) do
  msg != "" and String.length(msg) <= 10
end

def adicionar(mensagens, msg), do: mensagens ++ [msg]

def mostrar([]), do: :ok
def mostrar([h | t]) do
  IO.puts(h)
  mostrar(t)
end
```

### `chat.exs` vs `chat v2.exs`

| Aspecto | `chat.exs` | `chat v2.exs` |
| --- | --- | --- |
| Responsabilidades | tudo em `loop/2` | separadas por função (`processar`, `valida?`, `adicionar`, `mostrar`) |
| Decisão de fluxo | `if/else` | *pattern matching* em `processar/3` |
| Exibição | `Enum.each` | recursão manual (`mostrar/1`) |
| Validação de mensagem | nenhuma | tamanho máximo e não-vazia |
| Comandos | só `sair` | `sair`, `/count`, `/clear` |

## Execução

Pré-requisito: [Elixir](https://elixir-lang.org/install.html) instalado (`elixir --version`).

```bash
# versão inicial
elixir chat.exs

# versão refatorada (nome de arquivo com espaço precisa de aspas)
elixir "chat v2.exs"
```

## Conceitos aplicados

- Programação funcional
- Imutabilidade
- Recursão
- Pattern matching
- Modularização e separação de responsabilidades
- Funções puras

---

### Autor

Gabriel Muchon Pavanelli
Ciência da Computação — Faculdade Impacta
