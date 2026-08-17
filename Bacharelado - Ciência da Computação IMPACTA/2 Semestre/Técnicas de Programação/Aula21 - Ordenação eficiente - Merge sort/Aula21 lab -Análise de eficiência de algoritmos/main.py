'''
Análise de eficiência de algoritmos de ordenação:

    Merge sort
        e
            Heap Sort

------> precisa terminar
'''

# %% imports
from line_profiler import LineProfiler
from memory_profiler import profile
import time
import heapsort
import mergesort
import random
import matplotlib.pyplot as plt

# Gera uma lista de 1000 números aleatórios
lista_randomica = random.sample(range(10000), 1000)
repeticoes = 10

# Listas para armazenar os dados
tempos_heapsort = []
tempos_mergesort = []
memorias_heapsort = []
memorias_mergesort = []
line_profile_heapsort = []
line_profile_mergesort = []

# Função para medir o tempo e a memória para heapsort
def test_heapsort():
    for _ in range(repeticoes):
        start_time = time.perf_counter()
        heapsort.heap_sort(lista_randomica.copy())
        end_time = time.perf_counter()
        tempo_medio = (end_time - start_time)
        tempos_heapsort.append(tempo_medio)

# Função para medir o uso de memória para heapsort
@profile
def memory_profile_heapsort():
    for _ in range(repeticoes):
        lista = lista_randomica.copy()
        heapsort.heap_sort(lista)

# Função para medir o tempo e a memória para mergesort
def test_mergesort():
    for _ in range(repeticoes):
        start_time = time.perf_counter()
        mergesort.merge_sort(lista_randomica.copy())
        end_time = time.perf_counter()
        tempo_medio = (end_time - start_time)
        tempos_mergesort.append(tempo_medio)

# Função para medir o uso de memória para mergesort
@profile
def memory_profile_mergesort():
    for _ in range(repeticoes):
        lista = lista_randomica.copy()
        mergesort.merge_sort(lista)

# Teste de tempo para heapsort
test_heapsort()

# Teste de memória para heapsort
memory_profile_heapsort()

# Teste de tempo para mergesort
test_mergesort()

# Teste de memória para mergesort
memory_profile_mergesort()

# Teste LineProfiler para heapsort
profiler_heapsort = LineProfiler()
profiler_heapsort.add_function(heapsort.heap_sort)

def profile_heapsort():
    for _ in range(repeticoes):
        lista = lista_randomica.copy()
        heapsort.heap_sort(lista)

profiler_heapsort.enable()
profile_heapsort()
profiler_heapsort.disable()

# Teste LineProfiler para mergesort
profiler_mergesort = LineProfiler()
profiler_mergesort.add_function(mergesort.merge_sort)

def profile_mergesort():
    for _ in range(repeticoes):
        lista = lista_randomica.copy()
        mergesort.merge_sort(lista)

profiler_mergesort.enable()
profile_mergesort()
profiler_mergesort.disable()

# Função para plotar gráficos
def plotar_graficos():
    # Gráfico de Tempo
    plt.figure(figsize=(10, 5))
    
    # Gráfico de Tempo
    plt.subplot(1, 3, 1)
    plt.bar(['Heap Sort', 'Merge Sort'], 
            [sum(tempos_heapsort) / len(tempos_heapsort), sum(tempos_mergesort) / len(tempos_mergesort)], 
            color=['blue', 'orange'])
    plt.ylabel('Tempo Médio de Execução (segundos)')
    plt.title('Comparação de Algoritmos de Ordenação - Tempo')

    # Gráfico de Memória  ----> precisa dos dados
    plt.subplot(1, 3, 2)
    plt.bar(['Heap Sort', 'Merge Sort'], 
            [0, 0],  # Substitua com os dados de memória apropriados
            color=['blue', 'orange'])
    plt.ylabel('Uso de Memória (MB)')
    plt.title('Comparação de Algoritmos de Ordenação - Memória')

    # Gráfico de Line Profiler ----> precisa dos dados
    plt.subplot(1, 3, 3)
    plt.bar(['Heap Sort', 'Merge Sort'], 
            [0, 0],  # Substitua com os dados apropriados do Line Profiler
            color=['blue', 'orange'])
    plt.ylabel('Contagem de Chamadas')
    plt.title('Comparação de Algoritmos de Ordenação - Line Profiler')

    plt.tight_layout()
    plt.show()

plotar_graficos()
