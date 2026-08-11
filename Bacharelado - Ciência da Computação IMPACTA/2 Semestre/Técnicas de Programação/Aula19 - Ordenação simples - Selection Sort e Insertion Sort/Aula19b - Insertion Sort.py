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
            Insertion Sort

Para maior compreensão desses algoritmos, utilize teste de mesa do pythontutor:
https://pythontutor.com/

Insertion Sort:
→ Ideia: Comparar um item com os itens à sua esquerda e, se esse item for menor, trocar esses itens de posição
→ Essas comparações e trocas só devem parar quando o item for maior que o item à sua esquerda ou quando o item estiver na primeira posição da lista
'''

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
# Função que move o mais à esquerda possível um dado elemento da sequência
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    
def move_para_esquerda(s, i):
    while i > 0 and s[i] < s[i - 1]:
        troca(s, i, i - 1)
        i -= 1

print(move_para_esquerda([10,40,30,50,20], 4))

# %% 
# Função que implementa o algoritmo insertion sort

def insertion_sort_modificado(s):
    for i in range(1, len(s)):
        move_para_esquerda(s, i)

# %% Ou seja:

def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    
def move_para_esquerda(s, i):
    while i > 0 and s[i] < s[i - 1]:
        troca(s, i, i - 1)

def insertion_sort_modificado(s):
    for i in range(1, len(s)):
        move_para_esquerda(s, i)
        i -= 1

print(insertion_sort_modificado([10,40,30,50,20], 4))

# %%
