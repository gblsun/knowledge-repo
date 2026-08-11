# Função principal que exibe a tabuada de N
def exibir_tabuada(n):
    # Verifica se o valor de n está dentro do intervalo válido
    if 0 <= n <= 10:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("O número deve estar entre 0 e 10.")

# Recebe a entrada do usuário
N = int(input("Digite um número natural (0 <= N <= 10): "))

# Chama a função para exibir a tabuada
exibir_tabuada(N)
