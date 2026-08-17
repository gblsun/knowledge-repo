'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 25: técnicas de programação IMPACTA 01 de Novembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

continuando...
→
↳
→ Quick select'''
# %%
# → Implementação iterativa:

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
# Função Quick_select (iterativa)
def quick_select(lista, k):

    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        posicao_pivo = particiona(lista, inicio, fim)

        if posicao_pivo == k:
            return lista[k]
        elif posicao_pivo < k:
            inicio = posicao_pivo + 1
        else:
            fim = posicao_pivo - 1

    return None

import random

lista = random.sample(range(1, 101), 10)
print("Lista desordenada:", lista)
print(quick_select(lista, 2))
# %%