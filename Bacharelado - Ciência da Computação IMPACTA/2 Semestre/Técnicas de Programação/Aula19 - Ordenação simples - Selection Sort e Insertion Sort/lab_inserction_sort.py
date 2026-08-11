# %%
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def move_para_esquerda(s, i):
    while i > 0 and s[i] < s[i - 1]:
        troca(s, i, i - 1)
        i -= 1

def insertion_sort_modificado(s):
    for i in range(1, len(s)):
        move_para_esquerda(s, i)

print(insertion_sort_modificado([10,20,20,10,40,50]))

'''
[10,|30a,30b,40,20]
[10,30a,30b,20,40]
[10,30a,20,30b,40]
[10,20,30a,30b,40]

O algoritmo de ordenação Selection sort preserva a ordem relativa de elementos iguais. Portanto é um algoritmo de ordenação estável.
'''
# %%
