'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 22: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Quick sort

O algoritmo é composto por duas funções:
particionamento: particiona o vetor
quick_sort: repete recursivamente a operação de particionamento para cada subvetor gerado

'''
# função troca
def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# função particionamento
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
    if inicio < fim:
        posicao = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)
        quick_sort(lista, posicao + 1, fim)
# Exemplo de uso:
    
lista = [4, 2, 3, 5, 6, 9]
quick_sort(lista, 0, len(lista) - 1)
print(lista)

