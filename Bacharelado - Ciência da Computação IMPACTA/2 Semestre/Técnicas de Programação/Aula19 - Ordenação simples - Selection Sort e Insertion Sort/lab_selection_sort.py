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

print(selection_sort([10,20,20,10,40,50]))

'''
parte ordenada
    | parte não ordenada
[10,|30a,30b,40,20]
[10,20,|30b,40,30a]
[10,20,30b,30a,40]

O algoritmo de ordenação Selection sort não preserva a ordem relativa de elementos iguais. Portanto é um algoritmo de ordenação instável.'''