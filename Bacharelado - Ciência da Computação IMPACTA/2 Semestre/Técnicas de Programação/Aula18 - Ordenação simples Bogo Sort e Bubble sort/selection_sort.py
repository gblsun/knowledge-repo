def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def empurra(s, n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

def indice_menor_elemento(s, n):
    indice_menor = n
    for i in range(n, len(s)):
        if s[i] < s[indice_menor]:
            indice_menor = i
    return indice_menor

def selection_sort(s):
    lista2 = s[:]
    n = 0
    while n < len(lista2):
        indice_menor = indice_menor_elemento(lista2, n)
        if indice_menor != n:
            troca(lista2, n, indice_menor)
        n += 1
    return lista2

lista = [40, 30, 20, 50, 10]
lista_ordenada = selection_sort(lista)
print(lista_ordenada)