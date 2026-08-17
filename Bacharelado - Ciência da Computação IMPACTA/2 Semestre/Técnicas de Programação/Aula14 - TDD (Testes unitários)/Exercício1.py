'''
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 14: técnicas de programação IMPACTA 26 de Setembro de 2024                |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercícios:                                                                |
|        Teste Unitários TDD                                                    |
<-------------->x<-------------->x<------------->x<------------->x<------------->

1. Crie uma função chamada simular_rendimento, que recebe como parâmetro um número real correspondente a uma taxa de juros anual e um número inteiro correspondente ao número de anos de determinado investimento. Esta função retorna o valor final do investimento com base na taxa de juros e no período de investimento.

a. Crie uma tabela com três cenários de teste para este método

b. Crie funções de teste para estes três cenários

c. A função conforme o enunciado

d. Execute os testes utilizando pytest

→     
↳

→ R$1000,00;
→ 10% de juros;     
→ em 3 anos;

ou seja

→ em 1 ano:
    ↳ R$1000,00 x 0,10 = 100
    ↳ R$1000,00 + 100 = R$1100,00

→ em 3 anos;
    ↳ 100 x 3 = 30/100
    ↳ R$1000,00 x 0,30 = 300
    ↳ R$1000,00 + 300 = R$1300,00

→ em 5 anos;
    ↳ 100 x 5 = 50/100
    ↳ R$1000,00 x 0,50 = 500
    ↳ R$1000,00 + 500 = R$1500,00

'''
# %% 

# import

# funções

def simular_rendimento(n):
    vf = Vi8(1+t)

# def simular_rendimento(valor):
#     # TODO: vf = Vi*(1+t)**n
#     resultado = 0 
#     simulacao = 0
#     n * (juros/100) = resultado
#     resultado + valor = simulacao
#     return simulacao
# Programa Principal
def test_1():
    assert simular_rendimento(x)==1100

def test_1():
    assert simular_rendimento(x)==1100

def test_1():
    assert simular_rendimento(x)==1100
# %%
