def fibo_recursivo_sem_cache(n):
    global cont_recursivo_sem_cache
    cont_recursivo_sem_cache += 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_recursivo_sem_cache(n - 1) + fibo_recursivo_sem_cache (n - 2)

cont_recursivo_sem_cache=0