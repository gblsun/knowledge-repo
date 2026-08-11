# Atividade - Semana 9 - Paradigma Funcional - Elixir

Este diretório contém a atividade desenvolvida na disciplina de **Paradigmas da Computação**, com foco na aplicação de conceitos do **Paradigma Funcional** utilizando a linguagem **Elixir**.

O trabalho consistiu na evolução de um sistema simples de chat, partindo de uma versão inicial para uma versão refatorada, aplicando princípios fundamentais da programação funcional.

---

## Estrutura do Diretório

```bash
Atividade - Semana 9 - Paradigma Funcional - Elixir/
├── chat.exs
└── chat v2.exs
```
## Objetivo da Atividade

Evoluir um sistema funcional aplicando os seguintes conceitos:

- Funções puras
- Imutabilidade
- Recursão
- Separação de responsabilidades

---

## Arquivos

### `chat.exs`

Versão inicial do sistema de chat.

#### Características

- Processamento sequencial de mensagens
- Armazenamento de mensagens em lista
- Exibição no terminal
- Encerramento ao receber `"sair"`

#### Limitação identificada

A função principal concentra múltiplas responsabilidades, como:

- leitura de entradas
- validação
- adição de mensagens
- exibição
- encerramento do sistema

Essa abordagem reduz a legibilidade e dificulta futuras manutenções.

---

### `chat v2.exs`

Versão refatorada com aplicação dos princípios do paradigma funcional.

#### Melhorias implementadas

- Separação de responsabilidades
- Modularização do código
- Uso estruturado de recursão
- Validação de mensagens
- Inclusão de comandos adicionais

#### Comandos disponíveis

| Comando  | Função                          |
| -------- | ------------------------------- |
| `/count` | Exibe a quantidade de mensagens |
| `/clear` | Limpa o histórico               |
| `sair`   | Encerra o programa              |

#### Regras de validação

- A mensagem não pode ser vazia
- Máximo de 10 caracteres

---

## Etapas Desenvolvidas

### Parte 1 — Separação de responsabilidades

Criação de funções específicas para:

- validar mensagem
- adicionar mensagem
- processar entrada

Exemplo:

```elixir
def adicionar(mensagens, msg), do: mensagens ++ [msg]
```

### Parte 2 — Validação funcional

Implementação das regras de negócio em função isolada.

```elixir
def valida?(msg) do
  msg != "" and String.length(msg) <= 10
end
```

### Parte 3 — Redução de lógica duplicada

Criação da função:    
processar(entrada, mensagens, resto)    

Com isso, a função principal passou a delegar responsabilidades.

### Parte 4 — Uso de recursão no lugar de Enum.each

Substituição de estruturas iterativas por recursão.
```elixir
def mostrar([]), do: :ok

def mostrar([h | t]) do
  IO.puts(h)
  mostrar(t)
end
```

### Parte 5 — Comandos adicionais

Implementação de funcionalidades extras:

- clear
- count

### Restrições da Atividade
#### Não utilizar:
- IO.gets
- variáveis globais
- laços imperativos
#### Utilizar obrigatoriamente:
- listas de entradas
- recursão
- funções puras
- Execução

### Versão inicial
```elixir
elixir chat.exs
```
### Versão refatorada
```elixir

elixir "chat v2.exs"
```

## Conceitos Aplicados
- Programação funcional
- Imutabilidade
- Recursão
- Pattern Matching
- Modularização
- Separação de responsabilidades
- Funções puras

---
### Autor

Gabriel Muchon Pavanelli   
Ciência da Computação - Faculdade Impacta