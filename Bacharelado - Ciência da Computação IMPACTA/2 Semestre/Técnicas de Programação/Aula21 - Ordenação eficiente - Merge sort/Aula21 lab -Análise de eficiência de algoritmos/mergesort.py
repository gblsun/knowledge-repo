def combinar_subvetores(subvetor_esquerdo, subvetor_direito):
    vetor_ordenado = []
    i = 0
    j = 0

    while i < len(subvetor_esquerdo) and j < len(subvetor_direito):
        if subvetor_esquerdo[i] <= subvetor_direito[j]:
            vetor_ordenado.append(subvetor_esquerdo[i])
            i += 1
        else:
            vetor_ordenado.append(subvetor_direito[j])
            j += 1

    vetor_ordenado.extend(subvetor_esquerdo[i:])
    vetor_ordenado.extend(subvetor_direito[j:])
    return vetor_ordenado


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    subvetor_esquerdo = merge_sort(lista[:meio])
    subvetor_direito = merge_sort(lista[meio:])

    return combinar_subvetores(subvetor_esquerdo, subvetor_direito)


# # Programa principal
# v = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(merge_sort(v))
