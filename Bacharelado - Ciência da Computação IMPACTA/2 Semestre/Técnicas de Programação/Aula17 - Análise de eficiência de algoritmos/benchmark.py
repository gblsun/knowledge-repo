# ═════════════════════════════════════════════════
# Autor     : Lucio Nunes de Lira
# ═════════════════════════════════════════════════
# Programa  : Benchmark
# Linguagem : Python 3
# Compilador: CPython (3.9.7)
# Versão    : A (Rev. 2)
# ═════════════════════════════════════════════════

from copy import deepcopy
from time import perf_counter, process_time

def tempo(F, *A, TR=False):
    """Retorna o tempo em segundos consumido pela função
    F dados A argumentos. Se TR=True, a medição será pelo
    tempo de relógio, senão será pelo tempo do processo."""
    medicao = perf_counter if TR else process_time
    inicio = medicao()
    F(*A)
    return medicao() - inicio

def tempo_medio(F, *A, R=3, TR=False):
    """Retorna o tempo médio em segundos da função F
    executada com A argumentos em R rodadas. Se TR=True,
    a medição será pelo tempo de relógio, senão será pelo
    tempo do processo."""
    tempos = []
    for _ in range(R):
        copia = deepcopy(A)
        tempos.append(tempo(F, *copia, TR=TR))
    return sum(tempos) / len(tempos)

def compara(F, A, R=3, TR=False):
    """Retorna os tempos médios em segundos das funções F
    executadas com A argumentos em R rodadas. Se TR=True,
    a medição será pelo tempo de relógio, senão será pelo
    tempo do processo."""
    tempos = {}
    for funcao in F:
        tempos[funcao.__name__] = [] 
        for argumentos in A:
            tempos[funcao.__name__].append(tempo_medio(funcao, *argumentos, R=R, TR=TR))
    return tempos