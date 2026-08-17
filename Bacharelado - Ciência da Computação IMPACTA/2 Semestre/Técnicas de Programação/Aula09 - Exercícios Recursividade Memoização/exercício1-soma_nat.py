"""
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 9: técnicas de programação IMPACTA 05 de Setembro de 2024                 |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercícios:                                                                |
|        Recursividade e Memoização                                             |
<-------------->x<-------------->x<------------->x<------------->x<------------->

1.
Defina a função soma_nat que recebe como parâmetro um número natural n e retorna a soma de todos os números naturais até n.
"""

# %% --begin
# imports
from functools import lru_cache

# funções
@lru_cache
def soma_nat(n):
    if n == 1:
        return 1
    else:
        return n + soma_nat(n - 1)

# programa principal
print(soma_nat(5)) # 5+4+3+2+1 = 15
print(soma_nat(10)) # 10+9+8+7+6+5+4+3+2+1 = 55
# %% --end
