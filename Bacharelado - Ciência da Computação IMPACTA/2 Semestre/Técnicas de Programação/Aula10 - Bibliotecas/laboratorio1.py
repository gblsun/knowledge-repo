"""
Aula 10: técnicas de programação IMPACTA 06 de Setembro de 2024
Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

------------terminar!!!

Laboratório fibonacci com e sem memoização

utilizando bibliotecas:

line_profile
memory_profiler
"""

# %%
# import

from line_profiler import LineProfiler
from functools import lru_cache
from memory_profiler import profile

# funções


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache
def fibonacci_com_cache(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_com_cache(n - 1) + fibonacci_com_cache(n - 2)

@profile
def profile_fibonacci():
    n = 10
    result = fibonacci(n)
    print(f"Resultado: {result}")



# Programa Principal
profile_fibonacci()
# %%
