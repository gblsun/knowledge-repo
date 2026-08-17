'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 15: técnicas de programação IMPACTA 27 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Análise de eficiência
    de algoritmos

→ Geralmente temos várias soluções possíveis para
um dado problema.
    ↳ Como compará-las?
    ↳ Qual a mais eficiente?
→ Possíveis critérios de comparação:
    ↳ Tempo de execução
    ↳ Uso de memória


→ Como medir o tempo de execução?
Medimos o tempo contando a quantidade de passos/instruções que são executados pelo algoritmo
    ↳ Atenção: não confundir quantidade de passos com
linhas de código
    ↳ Pode variar de acordo com a entrada do algoritmo
→ Cronometrar o tempo no relógio não é uma boa
alternativa
→ Depende de diferentes fatores:
    ↳ Hardware
    ↳ Memória disponível
    ↳ Compilador
    ↳ Linguagem de programação
'''
#%% ---> begin
# seria executado 200 vezes independente do hardware, independete do software, independete da linguagem e IDE.
    for i in range(10):
        for j in range(20):
            if i*j==100:
                break
            print(i*j)
#%% ---> end
# qtd de linhas ≠ qtd de instruções ou qtd de passos.
'''
Pode variar de acordo com a entrada do algoritmo, portanto:
'''
#%%

# → Algoritmo a:
x = x + 1

# → Algoritmo b:
for i in range(0, n):
x = x + 1

# → Algoritmo c:
for i in range(0, n):
    for j in range(0, n):
    x = x + 1

'''
Algoritmo a: instrução executada 1 vez
Algoritmo b: instrução executada n vezes
Algoritmo c: instrução executada n² vezes

1, n e n² são chamados ordens de grandeza ou ordens de complexidade


Notação O grande (Big O)

→ É a notação mais conhecida para descrever o desempenho de um algoritmo. Indica o quão rápido ele é.

→ Ao analisarmos um algoritmo devemos analisar o pior caso do algoritmo, ou seja, a situação em que haverá o maior número de instruções a serem executadas;

→ O tempo de execução nunca ultrapassará esse limite.

+------------+----------------+-------------------------+
| Complexidade |  Classe       | Tempo de Execução      |
+------------+----------------+-------------------------+
| O(1)       |  constante      | ↑ Mais rápido          |
| O(log n)   |  logarítmica    |                        |
| O(log²n)   |  log-quadrática |                        |
| O(n)       |  linear         |                        |
| O(n log n) |  n log n        |                        |
| O(n²)      |  quadrática     |                        |
| O(n³)      |  cúbica         |                        |
| O(2ⁿ)      |  exponencial    |                        |
| O(n!)      |  fatorial       | ↓ Menos rápido         |
+------------+----------------+-------------------------+


Exemplo: considere a seguinte função, que recebe uma lista como parâmetro e faz algumas operações: '''
#%%
def funcao(lista):
    a = 0
    b = 1
    c  lista[a] + b
    return c
# 4 instruções!!
# A complexidade do código independe de números da lista.
# Complexidade constante O(1)
#%%
'''

→ Queremos saber o que acontece quando aumentarmos a lista.

→ Estratégia: vamos comparar o tempo de execução original com o tempo de execução ao dobrarmos a lista.'''

# %%
def funcao(lista):
    a = 0               #
    b = 1               #
    c = lista[a] + b    #
    return c            #

# %%
'''
'''
# %%
def funcao(lista):
    i = 0
    for a in lista:
        i = i + 1 
    return i
# Algoritmo de complexidade linear O(n)
# %%
'''
'''
# %%
def funcao(n):
    cont=0
    for i in range(n):
        for j in range(n):
            cont = cont+1
        return cont
# Algoritmo de complexidade Quadrática O(n²)
# %%
'''
→ Funções O(log n), definem soluções que dividem o problema em problemas menores, em geral, a metade do tamanho anterior (divisão e conquista)
→ É uma função extremamente rápida, que geralmente pode ser usada com “qualquer tamanho” de entrada
→ Já vimos alguma função como esta?
"diminuir complexidade a metade"
E se o algoritmo for uma composição de funções com diferentes complexidades?
→ Se dois algoritmos são executados em sequência, a complexidade será estabelecida pela complexidade do maior algoritmo'''

# %% --> begin
def funcao(n):
    cont=0
# <--------------------------->
    for i in range(n):
        for j in range(n):  # O(n²)
            cont = cont+1
# <--------------------------->
    for i in range(n):
        cont = cont+1       # O(n)
    return cont
# <--------------------------->

# A complexidade do algoritmo é quadrática O(n²)
# %% ----> end
