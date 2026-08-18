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
    
    Simulação de Curtose: Gere um conjunto de dados que siga uma distribuição normal e outro que tenha muitos outliers propositais. Calcule a curtose de ambos e verifique se o resultado condiz com a teoria (Mesocúrtica vs Leptocúrtica).
"""
import numpy as np


def curtose(dados):
    """Curtose de Fisher (curtose em excesso): distribuição normal = 0."""
    # desvios: distância de cada valor até a média do conjunto (pode ser positiva ou negativa)
    desvios = dados - np.mean(dados)
    # desvios ** 4: eleva à 4ª potência, então valores próximos da média quase não pesam,
    # mas valores muito distantes (outliers) explodem em magnitude — é isso que faz a
    # curtose ser sensível ao "peso das caudas" da distribuição, e não à dispersão em si
    # np.mean(desvios ** 4): 4º momento central, a média desses desvios elevados à 4ª potência
    # np.std(dados) ** 4: desvio padrão elevado à 4ª potência (variância ao quadrado), usado para
    # normalizar o resultado, tornando a curtose independente da escala/unidade dos dados
    # "- 3": convenção de Fisher, desloca a escala para que a distribuição normal fique em 0
    # (sem o "- 3" teríamos a curtose de Pearson, onde a normal vale 3)
    return np.mean(desvios ** 4) / np.std(dados) ** 4 - 3


# Passo 1: gera um conjunto com distribuição normal "pura" (sem outliers propositais)
# np.random.normal(loc, scale, size) sorteia números seguindo uma distribuição normal (curva do sino):
#   loc   = média em torno da qual os números vão se concentrar
#   scale = desvio padrão, controla o quão espalhados os números ficam da média
#   size  = quantos números gerar
normal = np.random.normal(loc=50, scale=10, size=100)
print('Conjunto Normal:', normal)

# Passo 2: gera um conjunto com muitos outliers propositais
# núcleo central normal (90 valores, mesmos parâmetros do Conjunto Normal) + cauda de valores
# extremos (10 valores com desvio padrão 10x maior, ou seja, muito mais distantes da média)
nucleo = np.random.normal(loc=50, scale=10, size=90)
outliers = np.random.normal(loc=50, scale=100, size=10)
# np.concatenate: junta os dois arrays (núcleo + outliers) em um único conjunto de dados
com_outliers = np.concatenate([nucleo, outliers])
print('Conjunto com Outliers:', com_outliers)

# Passo 3: calcula a curtose de cada conjunto
curtose_normal = curtose(normal)
curtose_outliers = curtose(com_outliers)
print(f"Curtose do Conjunto Normal: {curtose_normal:.2f}")
print(f"Curtose do Conjunto com Outliers: {curtose_outliers:.2f}")

# Passo 4: compara com a teoria (classificação pela curtose de Fisher, normal = 0)
# curtose ≈ 0 -> Mesocúrtica: mesmo "achatamento"/peso de cauda de uma distribuição normal
# curtose > 0 -> Leptocúrtica: pico mais alto/estreito no centro e caudas pesadas
#                (mais propensa a valores extremos/outliers), quanto maior, mais outliers "puxam" a curtose
# curtose < 0 -> Platicúrtica: pico mais achatado e caudas leves (menos propensa a outliers)
if curtose_normal < curtose_outliers:
    print("Conclusão: o Conjunto Normal é Mesocúrtico (curtose próxima de 0) e o Conjunto com Outliers é Leptocúrtico (curtose bem maior), como previsto pela teoria.")
else:
    print("Conclusão: o resultado não condiz com o esperado pela teoria; revise a geração dos outliers.")

