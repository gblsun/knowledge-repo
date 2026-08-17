"""
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 9: técnicas de programação IMPACTA 05 de Setembro de 2024                 |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercícios:                                                                |
|        Recursividade e Memoização                                             |
<-------------->x<-------------->x<------------->x<------------->x<------------->

3.
Defina a função num_it que recebe como parâmetro um número natural n e retorna o número de vezes que a função f tem que ser aplicada recursivamente a n até se atingir o número 1, isto é, devolve o número k tal que:

Obs: a polêmica conjectura de Collatz afirma que tal programa sempre termina.

<-------------->x<-------------->x<------------->x<------------->x<------------->
seja a função:

f de x é igual  

se x for um número par 
    x/2
caso contrário
    3x+1

ou melhor

f(n):
    if n % 2 == 0
        return x/2
    else:
        return 3n+1
        

num_it(k, n):
    if n == 1:
        return k:
    else:
        return f(n) 
        k+=1
        
se n = 6:

f(6) = 6 / 2 = 3 (1ª vez)
f(3) = 3 * 3 + 1 = 10 (2ª vez)
f(10) = 10 / 2 = 5 (3ª vez)
f(5) = 3 * 5 + 1 = 16 (4ª vez)
f(16) = 16 / 2 = 8 (5ª vez)
f(8) = 8 / 2 = 4 (6ª vez)
f(4) = 4 / 2 = 2 (7ª vez)
f(2) = 2 / 2 = 1 (8ª vez)
"""

# %% --begin
# imports
from functools import lru_cache

# funções
@lru_cache
def f(x):
    if x % 2 == 0:
        return x/2
    else:
        return 3 * x + 1

@lru_cache
def num_it(n):
    if n == 1:
        return 0
    else:
        return 1 + num_it(f(n))

print(num_it(6))
# %%
