# # Aula: técnicas de programação IMPACTA 16 e 17 de Agosta de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Novas estruturas de Dados:
# Dicionários

# Exercício I
# Elabore um programa que crie um dicionário de produtos, inicialmente vazio. Preencha o dicionário com as informações de 5 produtos. Utilize o nomedo produto como chave e o preço como valor. Solicite os dados ao usuário. Percorra o dicioná    rio e exiba o nome dos produtos com preço superior a R$ 50,00.

# %% ---begin
produtos = {}

for i in range(5):
    produto = input(f'Digite o seu {i+1}° produto: ')
    valor = float(input(f'Digite o valor de {produto} '))
    produtos[produto] = valor
    
for produto, valor in produtos.items():
    if valor >= 50: 
        print(produtos) 
# %% ---end