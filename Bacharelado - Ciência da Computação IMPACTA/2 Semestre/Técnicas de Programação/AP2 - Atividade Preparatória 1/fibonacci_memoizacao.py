from functools import lru_cache

# Variável global para contar o número de chamadas recursivas
chamadas_recursivas_memoizacao = 0

# Função Fibonacci com memoização
@lru_cache(maxsize=None)  #--------> andei pesquisando e disseram que é mais correto assim.
def fibonacci_memoizacao(n):
    global chamadas_recursivas_memoizacao  # Indica que estamos usando a variável global
    chamadas_recursivas_memoizacao += 1  # Incrementa a contagem de chamadas

    # Casos base do Fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Chamada recursiva com memoização
        return fibonacci_memoizacao(n-1) + fibonacci_memoizacao(n-2)
