def desenhar_triangulo_alfabetico(n):
    # Verifica se o valor de n está dentro do intervalo permitido
    if 1 <= n <= 26:
        # Itera de 1 até n para gerar as linhas do triângulo
        for i in range(1, n + 1):
            # Calcula o caractere correspondente no alfabeto
            caractere = chr(64 + i)
            # Imprime o caractere repetido i vezes
            print(caractere * i)
    else:
        print("O número deve estar entre 1 e 26.")

# Recebe a entrada do usuário
N = int(input("Digite um número inteiro (1 <= N <= 26): "))

# Chama a função para desenhar o triângulo alfabético
desenhar_triangulo_alfabetico(N)
