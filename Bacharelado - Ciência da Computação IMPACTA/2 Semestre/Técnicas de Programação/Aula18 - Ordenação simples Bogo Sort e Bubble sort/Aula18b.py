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
→ 
↳
Bubble sort

→ A cada iteração, os itens máximos da lista “flutuam” sobre a sequência (ordenação por flutuação) em direção à última posição não ordenada
→Exemplo de algoritmo de ordenação por flutuação: Bubble-sort
→ Percorrer a sequência várias vezes
→ A cada iteração, comparar cada elemento com seu sucessor (s[i] com s[i+1]) e trocá-los de lugar caso estejam na ordem incorreta

'''
# %%

def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def empurra(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

def bubble_sort(s):
    n = len(s)
    while n > 1:
        empurra(s, n)
        n -= 1
        
lista = [40, 30, 20, 50, 10]
bubble_sort(lista)
print(lista)
# %%
