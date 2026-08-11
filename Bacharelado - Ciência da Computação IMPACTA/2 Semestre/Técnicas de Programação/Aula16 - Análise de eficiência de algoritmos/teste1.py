'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 16: técnicas de programação IMPACTA 03 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳

Análise de eficiência
    de algoritmos
'''
# %%

from bigO import BigO

big_o = BigO()


def constante(lista):
    return [lista[0]]


def linear(lista):
    return [sum(lista)]


def quadratica(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


big_o.test(constante, "random")
big_o.test(linear, "random")
big_o.test(quadratica, "random")
# %%
