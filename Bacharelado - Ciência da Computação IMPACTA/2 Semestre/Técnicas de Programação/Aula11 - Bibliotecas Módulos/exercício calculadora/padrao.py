'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 11: técnicas de programação IMPACTA 12 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

→ Crie um pacote chamado calculadora. Dentro deste pacote, inclua três módulos: padrao, cientifica e trigonometrica. As funcionalidades de cada módulo são:

    ↳ Padrão: deve disponibilizar funções de soma, subtração, multiplicação e divisão
'''
# %% --begin
# imports
import os

# funções
def escolha():
    os.system('cls')
    print('Seja bem vindo a calculadora')
    print('Qual o tipo de calculadora você deseja utilizar?')
    print('Digite 1 para calculadora Padrão')
    print('Digite 2 para calculadora Científica')
    print('Digite 3 para calculadora Trigonométrica')
    opcao = int(input('\nQual sua escolha? \n\n'))
# programa principal
escolha()
# %%
