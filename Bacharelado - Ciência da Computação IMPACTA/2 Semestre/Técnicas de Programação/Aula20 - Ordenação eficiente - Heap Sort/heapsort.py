def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def refazer_heap_maximo(lista, n, i):
    indice_maior = i  # Inicialmente, assumimos que o nó i é o índice do maior elemento
    indice_filho_esquerdo = 2 * i + 1  # Índice do filho à esquerda
    indice_filho_direito = 2 * i + 2  # Índice do filho à direita

    # Se o filho esquerdo for maior que o nó pai, ele passa a ser o maior
    if indice_filho_esquerdo < n and lista[indice_filho_esquerdo] > lista[indice_maior]:
        indice_maior = indice_filho_esquerdo

    # Se o filho direito for maior que o maior até agora, ele passa a ser o maior
    if indice_filho_direito < n and lista[indice_filho_direito] > lista[indice_maior]:
        indice_maior = indice_filho_direito

    # Se o maior elemento não for o nó pai, troca-se o nó pai de posição com o nó filho
    # que possui o maior elemento e continua a construção do heap máximo
    # a partir do índice do maior elemento
    if indice_maior != i:
        troca(lista, i, indice_maior)
        refazer_heap_maximo(lista, n, indice_maior)


def heap_sort(lista):
    n = len(lista)

    # Construir o heap máximo a partir do último nó interno
    for i in range(n // 2 - 1, -1, -1):
        refazer_heap_maximo(lista, n, i)

    # O laço for anterior garante a construção de um um heap máximo
    # no qual o nó raiz é o maior elemento da parte não ordenada da sequência
    # Trocamos o primeiro elemento com o último na parte não ordenada
    for i in range(n - 1, 0, -1):
        troca(lista, i, 0)
        refazer_heap_maximo(lista, i, 0)


# Programa principal
lista = [12, 11, 13, 5, 6, 7]
heap_sort(lista)
print("lista ordenada:", lista)
