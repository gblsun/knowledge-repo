'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 19: técnicas de programação IMPACTA 11 de Outubro de 2024                       |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Ordenação simples:

    Selection Sort
        e 
            Interstion Sort

Selection Sort:
→ Ideia: identificar o menor elemento da parte não ordenada da sequência e trocá-lo de posição com o primeiro elemento desta parte (acrescentando-o na parte ordenada da sequência)
→ Repetir a etapa anterior até que toda a sequência esteja ordenada '''

# OBS: Relembrando...
# Desenvolvemos uma função que realiza a troca da posição de dois elementos em uma sequência:
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

# Em seguida, desenvolvemos uma função que percorre a sequência e “empurra” o maior item da sequência para o final a partir da troca de posição dos elementos dois a dois:
def empurra(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

# %%
# Função que retorna o menor valor da sequência
def indice_menor_elemento(s, n):
    indice_menor = n
    for i in range(n, len(s)):
        if s[i] < s[indice_menor]:
            indice_menor = i
    return indice_menor

print(indice_menor_elemento([10,40,30,50,20], 1))
# %%
# Função que implementa o algoritmo selection sort

def selection_sort(s):
    n = 0
    while n < len(s):
        indice_menor = indice_menor_elemento(s, n)
        if indice_menor != n:
            troca(s, n, indice_menor)
        n += 1

# %%
# Removendo efeito colateral

def selection_sort(s):
    lista2 = s[:]
    n = 0
    while n < len(lista2):
        indice_menor = indice_menor_elemento(lista2, n)
        if indice_menor != n:
            troca(lista2, n, indice_menor)
        n += 1
    return lista2

# %%
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def indice_menor_elemento(s, n):
    indice_menor = n
    for i in range(n, len(s)):
        if s[i] < s[indice_menor]:
            indice_menor = i
    return indice_menor

def selection_sort(s):
    n = 0
    while n < len(s):
        indice_menor = indice_menor_elemento(s, n)
        if indice_menor != n:
            troca(s, n, indice_menor)
        n += 1

print(selection_sort([10,40,30,50,20], 1))