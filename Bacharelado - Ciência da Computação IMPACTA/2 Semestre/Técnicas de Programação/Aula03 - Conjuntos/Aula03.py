# Aula 03: técnicas de programação IMPACTA 15 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Novas estruturas de dados:  Conjuntos
'''
Sintaxe básica:

nome = {
    elemento1,
    elemento2,
    elemento3
}

ou

nome = set(
    elemento1,
    elemento2,
    elemento3
)

Exemplo: turmas e alunos (poo e sql)

poo = {
    estudante1,
    estudante2,
    estudante3
}

sql = {
    estudante1,
    estudante2,
    estudante3
}'''

# %% Função Add
# Pode-se adicionar elementos ao conjunto por meio da função add:

numeros = {21, 34, 54, 12}
numeros.add(32)

# Função update
# A função update também pode ser utilizada Conjuntos em Python

empresas = {'Lacoste', 'Ralph Lauren'}
big_techs = ['apple', 'google', 'apple']
empresas.update(big_techs)

# %% Função remove
# Para remover elementos de um conjunto, pode-se utilizar a função remove:

linguagens = {'C', 'Java', 'Python'}
valor_removido = linguagens.discard('Java')

# %% Percorrer conjunto utilizando for
# Para percorrer um conjunto, pode-se utilizar for

linguagens = {'C', 'Java', 'Python'}
for l in linguagens:
    print(l)

# %% Verificação de elemento (operador in)
# Para verificar se um elemento pertence a um conjunto, pode-se usar o operador in

linguagens = {'C', 'Java', 'Python'}
'C' in linguagens #True

# %% verificação de conjunto é subconjunto de outro (issubset)
# Verificar se um conjunto é subconjunto de outro, pode-se usar o método issubset

N5 = {0, 1, 2, 3, 4, 5} # {n∈N∣n<10}
Z5 = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5} # {z∈Z∣|z|<5}
N5.issubset(Z5) #True


# %% Operações com conjuntos

# União

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1 | conjunto2

# Interseção

intersecao = conjunto1 & conjunto2

# Diferença 

diferenca = conjunto1 - conjunto2
# %% --end