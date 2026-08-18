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

# Passo 1: gera 100 números aleatórios entre 1 e 100
numeros = np.random.randint(1, 101, size=100)
print('Números aleatórios:', numeros)

# Passo 2: média e mediana do conjunto original
# Média: soma de todos os valores dividida pela quantidade de valores
media = np.mean(numeros)
print(f"A média dos números é: {media}")

# Mediana: valor central da lista ordenada (ou média dos dois centrais, se n for par)
mediana = np.median(numeros)
print(f"A mediana dos números é: {mediana}")

# Passo 3: adiciona um outlier (5000) ao conjunto, sem alterar o array original
numeros_outlier = np.append(numeros, 5000)

# Passo 4: média e mediana do conjunto já com o outlier
media_outlier = np.mean(numeros_outlier)
print(f"A média dos números com o outlier é: {media_outlier}")

mediana_outlier = np.median(numeros_outlier)
print(f"A mediana dos números com o outlier é: {mediana_outlier}")

# Passo 5: compara o quanto cada medida se deslocou com a entrada do outlier
variacao_media = media_outlier - media
print(f"A diferença da média com e sem outlier é: {variacao_media}")

variacao_mediana = mediana_outlier - mediana
print(f"A diferença da mediana com e sem outlier é: {variacao_mediana}")

# abs() descarta o sinal da variação, sobrando só o "tamanho" do deslocamento.
# Sem isso, uma variação de -49 pareceria menor que uma de 0.5 numa comparação direta.
if abs(variacao_media) > abs(variacao_mediana):
    print("Conclusão: a média foi mais alterada pelo outlier.")
else:
    print("Conclusão: a mediana foi mais alterada pelo outlier.")