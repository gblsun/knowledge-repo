import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# 1. Preparação dos Dados
indices = ['Brute Force', 'SQL Injection', 'DDoS']
colunas = ['Linux', 'Windows']
dados = [[70, 30],
         [20, 80],
         [50, 50]]

df = pd.DataFrame(dados, index=indices, columns=colunas)

# 2. Execução do Teste Qui-Quadrado
chi2, p, dof, esperados = chi2_contingency(df)

# 3. Visualização Gráfica
plt.figure(figsize=(12, 5))

# Gráfico 1: Distribuição Observada (Barras Agrupadas)
plt.subplot(1, 2, 1)
df.plot(kind='bar', ax=plt.gca(), color=['blue', 'orange'])
plt.title(f'Frequências Observadas\n(P-valor: {p:.4f})')
plt.ylabel('Quantidade de Ataques')
plt.xticks(rotation=0)

# Gráfico 2: Heatmap da Diferença (Resíduos)
# Mostra onde a diferença entre o Real e o Esperado é maior
plt.subplot(1, 2, 2)
df_esperados = pd.DataFrame(esperados, index=indices, columns=colunas)
diferenca = df - df_esperados
sns.heatmap(diferenca, annot=True, cmap='RdBu_r', center=0) #RdBu : red - blue r: reverse
plt.title('Diferença (Observado - Esperado)\nValores positivos = Mais ataques que o previsto')

plt.tight_layout()
plt.show()

# Print dos resultados
print(f"Estatística Qui-Quadrado: {chi2:.2f}")
print(f"P-valor: {p:.4f}")
# teste Qui quadrado
if p < 0.05:
    print("Resultado: O tipo de ataque DEPENDE do Sistema Operativo. Precisamos de patches específicos!")
else:
    print("Resultado: Os ataques são independentes do OS.")