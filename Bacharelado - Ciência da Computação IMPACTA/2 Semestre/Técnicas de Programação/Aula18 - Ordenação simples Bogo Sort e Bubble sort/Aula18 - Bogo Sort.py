'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 18: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Ordenação simples
    Bogo Sort e
        Bubble sort

Bogo Sort

→ Bogo Sort: bogus + sort (ordenação)
→ Algoritmo de ordenação mais ineficiente e sem aplicações práticas

→ Ideia: “embaralhar” aleatoriamente os elementos da sequência até que ela fique ordenada
→ Considere uma sequência com 10 números inteiros. De quantas formas diferentes podemos embaralhar a sequência?
→ Ao embaralhar aleatoriamente a sequência, existem 10 opções para o primeiro elemento, 9 para o segundo, 8 para o terceiro e assim por diante
→ Ao todo, existem 10! possíveis permutações dos elementos
→ A probabilidade de que a sequência seja ordenada é 1/10!

→ O que é mais provável?
    I. Ganhar na Mega-Sena (escolher 6 números corretamente entre 60 opções)
    II. O Bogo Sort  ordenar uma sequência com 60 elementos?
        ↳ Mega-Sena: Aproximadamente 50 milhões (5x10^6) de combinações, uma correta
        ↳ Bogo Sort: Aproximadamente 8 centilhões (8x10^81) de combinações, uma correta
'''

# %%
import random
def esta_ordenado(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False
        i += 1
    return True

def bogosort(lista):
    while not esta_ordenado(lista):
        random.shuffle(lista)
    return lista

print(bogosort([10,40,20,30]))
