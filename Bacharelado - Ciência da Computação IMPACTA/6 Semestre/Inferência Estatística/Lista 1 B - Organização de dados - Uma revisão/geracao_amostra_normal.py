"""
╔═══════════════════════════════════════════════════════════════╗
║  Lista_1B_Organizacao_de_Dados                  IMPACTA       ║
║  Parte 4: Exercícios Computacionais (Simulação)               ║
║  Inferência Estatística                                       ║
║  18 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝

Parte 4: Exercícios Computacionais (Simulação)

    18. Utilizando Python (biblioteca numpy), gere uma amostra de 100 números seguindo uma distribuição normal com média 50 e desvio padrão 10.
"""
import numpy as np

# np.random.normal(loc, scale, size) sorteia números seguindo uma distribuição normal
# (curva do sino) — diferente de np.random.randint, que sorteia inteiros com distribuição
# UNIFORME (todos os valores igualmente prováveis). Como o exercício pede média e desvio
# padrão específicos, precisa ser normal, não uniforme.
#   loc   = média em torno da qual os números vão se concentrar
#   scale = desvio padrão, controla o quão espalhados os números ficam da média
#   size  = quantos números gerar
numeros = np.random.normal(loc=50, scale=10, size=100)
print("Amostra gerada:", numeros)

# Verificação: média e desvio padrão da amostra devem ficar próximos dos parâmetros
# pedidos (50 e 10), mas não idênticos — é uma amostra aleatória, não a população inteira.
print(f"Média da amostra: {np.mean(numeros):.2f}")
print(f"Desvio padrão da amostra: {np.std(numeros):.2f}")
