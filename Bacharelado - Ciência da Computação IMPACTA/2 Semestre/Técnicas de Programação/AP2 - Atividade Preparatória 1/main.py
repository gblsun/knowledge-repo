'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| AP2 - Atividade Preparatória 1: técnicas de programação                              |
| IMPACTA 10 de Setembro de 2024 - entrega para 10/10                                  |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+


O objetivo deste exercício é implementar duas abordagens para calcular a sequência de Fibonacci: uma abordagem recursiva e outra iterativa. Em seguida, você irá avaliar empiricamente a complexidade de cada algoritmo, contando o número de iterações ou chamadas realizadas durante a execução.

I. Implemente a função fibonacci_recursivo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem recursiva. A função deve também contar e retornar o número de chamadas feitas durante o cálculo.

    ✔

II. Implemente a função fibonacci_iterativo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem iterativa. A função deve também contar e retornar o número de iterações realizadas durante o cálculo.

    ✔
    
III. No programa principal, teste ambas as funções para valores de  n variando de 1 a 10 (ou um intervalo maior se preferir) e armazene o número de iterações/chamadas realizadas para cada valor de n em um dicionário com o seguinte formato:
{n: qtde de iterações/chamadas}

    ✔

IV. Use a biblioteca matplotlib para plotar gráficos que representem a relação entre n e o número de iterações/chamadas para ambas as abordagens. No gráfico, o eixo x deve representar o valor de n e o eixo y deve representar o número de iterações/chamadas. Veja o exemplo de código anexado na aula 15 se necessário.

    ✔
V. Pesquise pela complexidade teórica das funções e compare os resultados obtidos. Discuta como o número de iterações ou chamadas muda à medida que n aumenta e como isso reflete na complexidade dos algoritmos.
Aplique a técnica de memoização à função recursiva e analise novamente a complexidade. Discuta a respeito do resultado obtido.

    ✔
'''
# %% ---> início
# imports
import matplotlib.pyplot as plt
from matplotlib import style
from fibonacci_recursivo import fibonacci_recursivo 
from fibonacci_memoizacao import fibonacci_memoizacao
from fibonacci_iterativo import fibonacci_iterativo



# ---> testes das funções:
# ------> Abordagem recursiva e 
# ---------> Abordagem iterativa 
# ------------> Abordagem recursiva com memoização 

# Dicionários para armazenar os resultados de cada abordagem
resultados_recursivo = {}
resultados_memoizacao = {}
resultados_iterativo = {}

# Testando a função recursiva
for n in range(1, 11):
    global chamadas_recursivas
    chamadas_recursivas = 0  # Reseta a contagem de chamadas
    fibonacci_recursivo(n)   # Chama a função
    resultados_recursivo[n] = chamadas_recursivas  # Armazena o número de chamadas

# Testando a função recursiva com memoização
for n in range(1, 11):
    global chamadas_recursivas_memoizacao
    chamadas_recursivas_memoizacao = 0  # Reseta a contagem de chamadas
    fibonacci_memoizacao(n)   # Chama a função
    resultados_memoizacao[n] = chamadas_recursivas_memoizacao  # Armazena o número de chamadas

# Testando a função iterativa
for n in range(1, 11):
    valor, iteracoes = fibonacci_iterativo(n)  # Chama a função
    resultados_iterativo[n] = iteracoes  # Armazena o número de iterações

# Exibir os resultados
print("Recursivo:", resultados_recursivo)
print("Memoização:", resultados_memoizacao)
print("Iterativo:", resultados_iterativo)

# --- Plotando os gráficos ---

# Style
style.use('ggplot')
''' Estilos disponíveis
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']'''

plt.figure(figsize=(10, 6))




n_values = list(resultados_recursivo.keys())


# Plotando o gráfico para as abordagens recursiva e iterativa
plt.plot(n_values, list(resultados_recursivo.values()), label='Recursivo', marker='o')
plt.plot(n_values, list(resultados_memoizacao.values()), label='Recursivo (com Memoização)', marker='x')
plt.plot(n_values, list(resultados_iterativo.values()), label='Iterativo', marker='s')

# -----> outro estilo <-----
# plt.plot(n_values, list(resultados_recursivo.values()), label='Recursivo', color=colors[0], marker='o', linewidth=2, markersize=8)
# plt.plot(n_values, list(resultados_memoizacao.values()), label='Recursivo (com Memoização)', color=colors[1], marker='x', linewidth=2, markersize=8)
# plt.plot(n_values, list(resultados_iterativo.values()), label='Iterativo', color=colors[2], marker='s', linewidth=2, markersize=8)

# Configurando o gráfico
plt.xlabel('n')
plt.ylabel('Número de Chamadas/Iterações')
plt.title('Comparação entre Recursivo, Memoização e Iterativo - Fibonacci')
plt.legend()
plt.grid(True)

colors = ['#FF4500', '#4169E1', '#FFA500'] 

# plt.plot(n_values, list(resultados_recursivo.values()), label='Recursivo', color=colors[0], marker='o', linewidth=2, markersize=8)
# plt.plot(n_values, list(resultados_memoizacao.values()), label='Recursivo (com Memoização)', color=colors[1], marker='x', linewidth=2, markersize=8)
# plt.plot(n_values, list(resultados_iterativo.values()), label='Iterativo', color=colors[2], marker='s', linewidth=2, markersize=8)

plt.title('Comparação de Complexidade entre Abordagens de Fibonacci', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('n', fontsize=14, labelpad=15)
plt.ylabel('Número de Chamadas/Iterações', fontsize=14, labelpad=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=12, loc='upper left', frameon=True, shadow=True, borderpad=1)

plt.grid(True, which='both', linestyle='--', linewidth=0.6)

plt.savefig('fibonacci_comparacao.png', dpi=300, bbox_inches='tight')


# Exibindo o gráfico
plt.show()