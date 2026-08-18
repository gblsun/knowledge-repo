"""
╔═══════════════════════════════════════════════════════════════╗
║  Lista_Estatistica_Univariada                     IMPACTA     ║
║  Parte 4: Exercícios Computacionais (Simulação)               ║
║  Inferência Estatística                                       ║
║  18 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝

Parte 4: Exercícios Computacionais (Simulação)
    Para estes exercícios, utilize uma ferramenta como Python (bibliotecas numpy/pandas) ou Excel.

Simulação de Dispersão: Gere dois conjuntos de dados: Conjunto A (50 números aleatórios, média 10, desvio padrão 1) e Conjunto B (50 números, média 10, desvio padrão 5). Calcule o Coeficiente de Variação (CV) e comente.
"""
import numpy as np


# Passo 1: gera dois conjuntos com distribuição normal, mesma média (10) e desvios diferentes (1 e 5)
conjuntoA = np.random.normal(loc=10, scale=1, size=50)
print('Conjunto A:', conjuntoA)

conjuntoB = np.random.normal(loc=10, scale=5, size=50)
print('Conjunto B:', conjuntoB)
'''
np.random.normal(loc, scale, size) sorteia números seguindo uma distribuição normal (curva do sino):
    loc   = média em torno da qual os números vão se concentrar
    scale = desvio padrão, controla o quão espalhados os números ficam da média
    size  = quantos números gerar
'''
# Passo 2: Coeficiente de Variação (CV) = desvio padrão / média, em %
cv_A = np.std(conjuntoA) / np.mean(conjuntoA) * 100
cv_B = np.std(conjuntoB) / np.mean(conjuntoB) * 100
print(f"Coeficiente de Variação do Conjunto A: {cv_A:.2f}%")
print(f"Coeficiente de Variação do Conjunto B: {cv_B:.2f}%")

# Comentário: as duas médias são iguais (10), então o CV isola a dispersão relativa de cada conjunto
if cv_A < cv_B:
    print("Conclusão: mesmo com a mesma média, o Conjunto B tem variação relativa muito maior (CV mais alto).")
else:
    print("Conclusão: mesmo com a mesma média, o Conjunto A tem variação relativa muito maior (CV mais alto).")
