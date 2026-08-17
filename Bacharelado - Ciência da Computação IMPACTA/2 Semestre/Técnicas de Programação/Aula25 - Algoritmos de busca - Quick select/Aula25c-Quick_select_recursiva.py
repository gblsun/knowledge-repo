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
# → Implementação recursiva::

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
# Função Quick_select (recursiva)
def quick_select(lista, k, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio <= fim:
        posicao_pivo = particiona(lista, inicio, fim)

        if posicao_pivo == k:
            return lista[k]
        elif posicao_pivo < k:
            return quick_select(lista, k, posicao_pivo + 1, fim)
        else:
            return quick_select(lista, k, inicio, posicao_pivo - 1)

    return None


import random

lista = random.sample(range(1, 101), 10)
print("Lista desordenada:", lista)
print(quick_select(lista, 2))
