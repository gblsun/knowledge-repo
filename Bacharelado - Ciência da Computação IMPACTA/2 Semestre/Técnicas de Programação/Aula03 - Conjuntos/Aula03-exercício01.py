# Aula 03: técnicas de programação IMPACTA 15 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)


# -----ainda não terminado
'''
Suponha que você foi contratado para desenvolver uma funcionalidade no sistema do RH de um novo banco digital. Esse banco teve acesso ao cadastro de clientes de outras três empresas concorrentes (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais clientes. Para isso, pediu que você gerasse um relatório com 12 itens (próximo slide). Responda às questões manualmente e, em seguida, utilize os conjuntos em Python para  comparar as respostas.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6 = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

a) Quais são os clientes de cada uma, separadamente.
b) Quais são os clientes de todas as concorrentes.
c) Quais são os clientes da Nubank que também são clientes do C6.
d) Quais são os clientes da Nubank que também são clientes do Inter.
e) Quais são os clientes do C6 que também são clientes do Inter.
f) Quais são os clientes apenas da Nubank.
g) Quais são os clientes apenas do C6.
h) Quais são os clientes apenas do Inter.
i) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
j) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
k) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
l) Quais são os clientes das três simultaneamente.
'''

#  %% --begin

# Declaração dos conjuntos:

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6 = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# a) Quais são os clientes de cada uma, separadamente.

print(f'Os clientes do banco nubank é: {nubank}')
print(f'Os clientes do banco c6 é: {c6}')
print(f'Os clientes do banco inter é: {inter}')

# b) Quais são os clientes de todas as concorrentes.

uniao = nubank|c6|inter
print()
print(f'Os clientes de todas as concorrentes (união) são: {uniao}')

# c) Quais são os clientes da Nubank que também são clientes do C6.

# %%
