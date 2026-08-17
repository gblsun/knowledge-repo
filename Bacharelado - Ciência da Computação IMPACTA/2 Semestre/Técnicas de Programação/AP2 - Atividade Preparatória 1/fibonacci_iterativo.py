def fibonacci_iterativo(n):
    if n == 1:
        return 0, 1  # Retorna o valor e a contagem de iterações
    elif n == 2:
        return 1, 1  # Retorna o valor e a contagem de iterações

    anterior, atual = 0, 1
    iteracoes = 1  # Inicializa o contador de iterações
    for _ in range(3, n + 1):
        anterior, atual = atual, anterior + atual
        iteracoes += 1  # Incrementa a contagem a cada iteração
    return atual, iteracoes  # Retorna o valor e o número de iterações
