chamadas_recursivas = 0
def fibonacci_recursivo(n):
    global chamadas_recursivas # Indica que estamos usando a variável global 'chamadas'
    chamadas_recursivas += 1 # Incrementa a contagem de chamadas
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fibonacci_recursivo(n-1)+ fibonacci_recursivo(n-2))