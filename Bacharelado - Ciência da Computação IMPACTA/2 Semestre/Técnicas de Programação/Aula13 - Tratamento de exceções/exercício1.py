"""
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 13: técnicas de programação IMPACTA 05 de Setembro de 2024                |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercício 1                                                                |
|        Tratamento de excessões                                                |
<-------------->x<-------------->x<------------->x<------------->x<------------->

I. Crie um programa que peça ao usuário valores inteiros a fim de preencher uma lista de tamanho 10. Não implemente nenhum tipo controle referente ao tamanho da lista, deixe que o usuário digite valores até que a entrada -1 seja digitada. Uma vez digitado o valor -1, a digitação de novos elementos deve ser interrompida. Feita toda a coleta dos dados, exiba-os em tela. Tratar as seguintes exceções:

    ↳ IndexError: quando o usuário informar mais que 10 valores.
    ↳ TypeError: quando o usuário informar um valor não inteiro."""
# %%
# imports
# funções
def coletar_valores():
    # Inicializa a lista para armazenar os valores
    valores = []

    print("Digite até 10 valores inteiros (digite -1 para encerrar):")

    while len(valores)
        # Solicita um valor ao usuário
        valor = int(input(f"Valor {len(valores) + 1}: "))
        
        # Verifica se o valor é -1 para encerrar a coleta
        if valor == -1:
            break
        
        # Adiciona o valor à lista
        valores.append(valor)

    # Exibe os valores coletados
    print("\nValores digitados:")
    for v in valores:
        print(v)

# programa principal
# Chama a função para coletar e exibir os valores
coletar_valores()

# %%
