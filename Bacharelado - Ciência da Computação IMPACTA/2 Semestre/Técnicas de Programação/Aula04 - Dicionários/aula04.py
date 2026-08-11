# Aula: técnicas de programação IMPACTA 16 e 17 de Agosta de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Novas estruturas de Dados:
# Dicionários

# %%

# Tipo de dados: dict
# Sintaxe
nome = {chave1: valor1, chave3: valor2, chave2: valor3}

# Exemplo:

estudantes = {
    191123: [8.5, 7, 8, 10],
    191124: [9.5, 9, 6, 7.5],
    191125: [5.5, 5, 6, 8.5],
}

# O acesso aos itens é realizado pela chave
# Dicionários não possuem índices sequencias como as listas
# Para inserir um novo item ao dicionário, deve-se atribuir um valor a uma chave inexistente
# Se a chave não existir, ela será criada. Se existir, seu valor será substituído

contatos = {}

contatos["Pedro"] = "94316353"  # cria novo item

contatos["Maria"] = "99991111"  # cria novo item

contatos["Teresa"] = "99992222"  # cria novo item
# %% função POP
# Para remover item do dicionário, pode-se utilizar a função pop

contatos = {}

contatos["Pedro"] = "94316353"  # cria novo item
contatos["Maria"] = "99991111"  # cria novo item
contatos["Teresa"] = "99992222"  # cria novo item

contatos.pop("Pedro")  # remove item

# %% Estrutura FOR em Dict's
# A estrutura for pode ser utilizada para percorrer o dicionário

contatos = {}

contatos["Pedro"] = "94316353"  # cria novo item

contatos["Maria"] = "99991111"  # cria novo item

contatos["Teresa"] = "99992222"  # cria novo item

for k in contatos:

    print(k)  # exibe todas as chaves

print(contatos[k])  # os valores associados às chaves

for k, v in contatos.items():

    print(k, v)  # exibe as chaves e valores
# %% Operador IN
# O operador in pode ser utilizado para verificar se uma chave existe no dicionário

contatos = {
"Maria": "94566655",
"Pedro": "94316353",
"João": "95220233"
}

if "Maria" in contatos :

    print(contatos["Maria"])

else:

    print("Chave não cadastrada")