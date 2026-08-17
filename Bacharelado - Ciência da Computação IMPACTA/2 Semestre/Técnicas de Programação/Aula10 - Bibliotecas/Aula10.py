'''
Aula 10: técnicas de programação IMPACTA 06 de Setembro de 2024
Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

Bibliotecas

→ Conjuntos de funcionalidades pré-implementadas que podem ser facilmente importadas e utilizadas em seus programas;

→ Desenvolvidas para realizar tarefas específicas (manipulação de dados, processamento de texto, acesso a bancos de dados, criação de interfaces gráficas, entre outras);

→ Permitem que os programadores reutilizem código já escrito e se concentrem em resolver os problemas específicos de suas aplicações.

→ Disponíveis no Python Package Index (PyPi) ou em repositórios remotos

→ Você mesmo pode criar sua biblioteca!

    ↳ pip: usado para instalar e gerenciar bibliotecas e pacotes de software escritos em Python que não estão incluídos na biblioteca padrão. Comandos úteis

    ↳ pip install <biblioteca>==<versão>: instala uma determinada versão da biblioteca

    ↳ pip uninstall <biblioteca>: desinstala uma biblioteca

    ↳ pip show <biblioteca>: exibe informações da biblioteca instalada
    
    ↳ pip install --upgrade <biblioteca>: atualiza a biblioteca

        ↳ pip install -U <biblioteca>: idem
    
    ↳ pip freeze: exibe todas bibliotecas instaladas no computador e informações da biblioteca;

Bibliotecas úteis

→ time: biblioteca padrão do Python que permite medir o tempo de execução de partes do código.

→ line_profiler: fornece informações detalhadas sobre o tempo gasto em cada linha do código.

→ memory_profiler: ajuda a medir o uso de memória das funções.




<----->x<------>
→ documento do projeto para identificar bibliotecas e versões

requiriments.txt

numpy==1.0.1
pandas==2.2.2
'''
# %% Biblioteca time

# time: biblioteca padrão do Python que permite medir o tempo de execução de partes do código.
import time

def fib(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fib(n-1)+ fib(n-2))

print(fib(10))

n = 20
start_time = time.time()
result = fib(n)
end_time = time.time()

print(f"Resultado: {result}")
print(f"Tempo de execução: {end_time - start_time} segundos")
# %% Biblioteca line_profiler

# line_profiler: fornece informações detalhadas sobre o tempo gasto em cada linha do código.

from line_profiler import LineProfiler
from functools import lru_cache


def fibonacci(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))


@lru_cache
def fibonacci_com_cache(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fibonacci_com_cache(n-1)+ fibonacci_com_cache(n-2))


profiler = LineProfiler()
profiler.add_function(fibonacci)
profiler.add_function(fibonacci_com_cache)

def profile_fibonacci():
    n = 20
    result = fibonacci(n)
    print(f"Resultado do fibonacci sem cache (s/memoização): {result}")


def profile_fibonacci_com_cache():
    n = 20
    result = fibonacci_com_cache(n)
    print(f"Resultado do fibonacci com cache (c/memoização): {result}")

profiler.enable()
profile_fibonacci()
profiler.disable()
profiler.print_stats()


profiler.enable()
profile_fibonacci_com_cache()
profiler.disable()
profiler.print_stats()

# %% memory_profiler

# memory_profiler: ajuda a medir o uso de memória das funções.
from memory_profiler import profile

def fibonacci(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))
    
@profile
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def profile_fibonacci():
    n = 10
    result = fibonacci(n)
    print(f"Resultado: {result}")

profile_fibonacci()

# %%
