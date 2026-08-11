'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 22: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Análise de complexidade de algoritmo. (Big O)
'''
from bigO import BigO

big_o = BigO()

# Função troca
def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# Função particionamento
def particiona(lista, inicio, fim):
    pivo = lista[inicio]
    i = inicio
    for j in range(inicio + 1, fim + 1):
        if lista[j] <= pivo:
            i += 1
            troca(lista, i, j)
    troca(lista, inicio, i)
    return i

# Função quick_sort
def quick_sort(lista, inicio, fim):
    if inicio < fim:  # Verifica se o intervalo é válido
        posicao = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)  # Ordena a parte esquerda
        quick_sort(lista, posicao + 1, fim)     # Ordena a parte direita

# Função wrapper para o bigO
def quick_sort_wrapper(nums):
    # Criar uma cópia da lista para não modificar a original
    nums_copy = nums.copy()
    quick_sort(nums_copy, 0, len(nums_copy) - 1)
    return nums_copy  # Retornar a lista ordenada

# Exemplo de uso
lista = [4, 2, 3, 5, 6, 9]
quick_sort(lista, 0, len(lista) - 1)
print(lista)

# Testando a complexidade do algoritmo
print(big_o.test(quick_sort_wrapper, "random"))
