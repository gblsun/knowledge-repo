'''
╔═══════════════════════════════════════════════════════════════╗
║  Lista_Estatistica_Univariada                     IMPACTA     ║
║  Parte 4: Exercícios Computacionais (Simulação)               ║
║  Inferência Estatística                                       ║
║  17 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝

Parte 4: Exercícios Computacionais (Simulação)
    Para estes exercícios, utilize uma ferramenta como Python (bibliotecas numpy/pandas) ou Excel.

    Simulação de Média e Mediana: Gere 100 números aleatórios entre 1 e 100. Calcule a média e a mediana. Em seguida, adicione um valor outlier (ex: 5000) ao conjunto. Verifique qual das duas medidas foi mais alterada.

'''
import numpy as np

numeros = np.random.randint(1, 101, size=100)
print('Números aleatórios:', numeros)