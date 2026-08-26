"""
==============================================================================
 REGULARIZAÇÃO EM MODELOS DE REGRESSÃO: OVERFITTING, RIDGE (L2), LASSO (L1)
 E ELASTIC NET
==============================================================================

Este script demonstra, de forma prática e visual, os seguintes conceitos:

1. OVERFITTING (sobreajuste)
   Quando um modelo é complexo demais para os dados disponíveis, ele "decora"
   o ruído do conjunto de treino em vez de aprender o padrão real. O modelo
   fica ótimo no treino, mas performa mal em dados novos (teste).

2. REGULARIZAÇÃO
   Técnica que adiciona uma penalidade ao tamanho dos coeficientes do modelo
   na função de custo, forçando-o a ser "mais simples" e generalizar melhor.

   Função de custo original (mínimos quadrados):
       J(w) = soma( (y_real - y_previsto)^2 )

   Ridge (L2): penaliza a soma dos QUADRADOS dos coeficientes.
       J(w) = soma( (y_real - y_previsto)^2 ) + alpha * soma(w_i^2)
       -> Encolhe os coeficientes em direção a zero, mas raramente os zera.
       -> Bom quando há muitas variáveis correlacionadas (multicolinearidade).

   Lasso (L1) - Least Absolute Shrinkage and Selection Operator: penaliza a
   soma dos VALORES ABSOLUTOS dos coeficientes.
       J(w) = soma( (y_real - y_previsto)^2 ) + alpha * soma(|w_i|)
       -> Consegue zerar coeficientes por completo, funcionando também como
          um SELETOR DE VARIÁVEIS (sparsity / esparsidade).

   Elastic Net: combina as duas penalidades acima com um peso "l1_ratio"
   que controla a mistura entre L1 e L2.
       J(w) = soma((y_real - y_previsto)^2)
              + alpha * [ l1_ratio * soma(|w_i|) + (1-l1_ratio) * soma(w_i^2) ]
       -> Tenta juntar o melhor dos dois mundos: seleciona variáveis (como o
          Lasso) mas lida melhor com variáveis correlacionadas (como o Ridge).

O parâmetro "alpha" controla a FORÇA da regularização:
   - alpha = 0   -> nenhuma penalidade (regressão comum, tende a overfitting)
   - alpha alto  -> penalidade forte (modelo mais simples, risco de underfitting)

==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)

# ------------------------------------------------------------------------
# 1) GERANDO DADOS SINTÉTICOS
# ------------------------------------------------------------------------
# Vamos criar uma relação real simples (uma senoide) e adicionar ruído.
# O objetivo é ajustar um polinômio de grau ALTO a esses poucos pontos,
# o que é uma receita clássica para overfitting.
n_amostras = 30
X = np.sort(np.random.uniform(0, 1, n_amostras))
y_real = np.sin(2 * np.pi * X)
ruido = np.random.normal(0, 0.25, n_amostras)
y = y_real + ruido

X = X.reshape(-1, 1)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Grade fina de pontos só para desenhar as curvas ajustadas
X_plot = np.linspace(0, 1, 300).reshape(-1, 1)
y_plot_real = np.sin(2 * np.pi * X_plot).ravel()

GRAU_POLINOMIO = 15  # grau bem alto -> favorece overfitting


def treinar_modelo(modelo, grau=GRAU_POLINOMIO):
    """Cria um pipeline: features polinomiais -> padronização -> modelo."""
    pipeline = make_pipeline(
        PolynomialFeatures(degree=grau, include_bias=False),
        StandardScaler(),
        modelo,
    )
    pipeline.fit(X_treino, y_treino)
    return pipeline


def avaliar_modelo(pipeline, nome):
    pred_treino = pipeline.predict(X_treino)
    pred_teste = pipeline.predict(X_teste)
    rmse_treino = np.sqrt(mean_squared_error(y_treino, pred_treino))
    rmse_teste = np.sqrt(mean_squared_error(y_teste, pred_teste))
    r2_teste = r2_score(y_teste, pred_teste)
    print(f"{nome:22s} | RMSE treino: {rmse_treino:6.3f} | "
          f"RMSE teste: {rmse_teste:6.3f} | R2 teste: {r2_teste:6.3f}")
    return rmse_treino, rmse_teste


# ------------------------------------------------------------------------
# 2) OVERFITTING: regressão linear "pura" sobre polinômio de grau alto
# ------------------------------------------------------------------------
print("=" * 78)
print("COMPARAÇÃO DE MODELOS (polinômio de grau", GRAU_POLINOMIO, ")")
print("=" * 78)

modelo_sem_reg = treinar_modelo(LinearRegression())
modelo_ridge = treinar_modelo(Ridge(alpha=0.01))
modelo_lasso = treinar_modelo(Lasso(alpha=0.001, max_iter=20000))
modelo_elastic = treinar_modelo(ElasticNet(alpha=0.002, l1_ratio=0.5, max_iter=20000))

avaliar_modelo(modelo_sem_reg, "Sem regularização")
avaliar_modelo(modelo_ridge, "Ridge (L2)")
avaliar_modelo(modelo_lasso, "Lasso (L1)")
avaliar_modelo(modelo_elastic, "Elastic Net")
print("=" * 78)

# ------------------------------------------------------------------------
# 3) GRÁFICO 1: overfitting vs. modelos regularizados
# ------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))
modelos_plot = [
    (modelo_sem_reg, "Sem regularização (overfitting)", "tab:red"),
    (modelo_ridge, "Ridge (L2)", "tab:blue"),
    (modelo_lasso, "Lasso (L1)", "tab:green"),
    (modelo_elastic, "Elastic Net (L1 + L2)", "tab:purple"),
]

for ax, (modelo, titulo, cor) in zip(axes.ravel(), modelos_plot):
    y_pred_plot = modelo.predict(X_plot)
    ax.plot(X_plot, y_plot_real, "k--", linewidth=1.5, label="Função real")
    ax.scatter(X_treino, y_treino, color="gray", s=35, label="Dados de treino", zorder=3)
    ax.scatter(X_teste, y_teste, color="orange", marker="x", s=50, label="Dados de teste", zorder=3)
    ax.plot(X_plot, y_pred_plot, color=cor, linewidth=2.5, label="Modelo ajustado")
    ax.set_title(titulo, fontsize=12, fontweight="bold")
    ax.set_ylim(-2, 2)
    ax.legend(fontsize=8, loc="upper right")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

fig.suptitle(
    f"Overfitting vs. Regularização (polinômio de grau {GRAU_POLINOMIO})",
    fontsize=15, fontweight="bold"
)
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig("/home/claude/1_overfitting_vs_regularizacao.png", dpi=130)
plt.close(fig)

# ------------------------------------------------------------------------
# 4) GRÁFICO 2: comparação dos coeficientes aprendidos
# ------------------------------------------------------------------------
# Aqui mostramos, lado a lado, o valor de cada coeficiente do polinômio
# para cada tipo de modelo. É a melhor forma de "ver" a diferença entre
# L1 (zera coeficientes) e L2 (só encolhe os coeficientes).
def pega_coeficientes(pipeline):
    return pipeline.named_steps[list(pipeline.named_steps.keys())[-1]].coef_

coefs_sem_reg = pega_coeficientes(modelo_sem_reg)
coefs_ridge = pega_coeficientes(modelo_ridge)
coefs_lasso = pega_coeficientes(modelo_lasso)
coefs_elastic = pega_coeficientes(modelo_elastic)

n_coefs = len(coefs_sem_reg)
indices = np.arange(1, n_coefs + 1)
largura = 0.2

fig2, ax2 = plt.subplots(figsize=(13, 6))
ax2.bar(indices - 1.5 * largura, coefs_sem_reg, largura, label="Sem regularização", color="tab:red")
ax2.bar(indices - 0.5 * largura, coefs_ridge, largura, label="Ridge (L2)", color="tab:blue")
ax2.bar(indices + 0.5 * largura, coefs_lasso, largura, label="Lasso (L1)", color="tab:green")
ax2.bar(indices + 1.5 * largura, coefs_elastic, largura, label="Elastic Net", color="tab:purple")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_xlabel("Coeficiente do termo polinomial (x^1, x^2, ..., x^n)")
ax2.set_ylabel("Valor do coeficiente")
ax2.set_title(
    "Comparação dos coeficientes aprendidos por cada modelo\n"
    "(repare como Lasso e Elastic Net zeram vários coeficientes)",
    fontsize=13, fontweight="bold"
)
ax2.set_xticks(indices)
ax2.legend()
fig2.tight_layout()
fig2.savefig("/home/claude/2_comparacao_coeficientes.png", dpi=130)
plt.close(fig2)

n_zeros_lasso = np.sum(np.isclose(coefs_lasso, 0, atol=1e-3))
n_zeros_elastic = np.sum(np.isclose(coefs_elastic, 0, atol=1e-3))
n_zeros_ridge = np.sum(np.isclose(coefs_ridge, 0, atol=1e-3))
print(f"Coeficientes zerados -> Ridge: {n_zeros_ridge}/{n_coefs} | "
      f"Lasso: {n_zeros_lasso}/{n_coefs} | Elastic Net: {n_zeros_elastic}/{n_coefs}")

# ------------------------------------------------------------------------
# 5) GRÁFICO 3: caminho de regularização (coeficientes x alpha)
# ------------------------------------------------------------------------
# Mostra o que acontece com CADA coeficiente à medida que alpha aumenta:
# no Ridge eles encolhem suavemente; no Lasso, vão "morrendo" (viram zero)
# um a um -- por isso o Lasso funciona como seleção de variáveis.
alphas = np.logspace(-4, 1, 60)

def caminho_coeficientes(ClasseModelo, alphas, **kwargs):
    caminho = []
    for a in alphas:
        modelo = ClasseModelo(alpha=a, **kwargs)
        pipe = make_pipeline(
            PolynomialFeatures(degree=GRAU_POLINOMIO, include_bias=False),
            StandardScaler(),
            modelo,
        )
        pipe.fit(X_treino, y_treino)
        coef = pipe.named_steps[list(pipe.named_steps.keys())[-1]].coef_
        caminho.append(coef)
    return np.array(caminho)

caminho_ridge = caminho_coeficientes(Ridge, alphas)
caminho_lasso = caminho_coeficientes(Lasso, alphas, max_iter=100000)

fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(13, 5.5))
for i in range(n_coefs):
    ax3a.plot(alphas, caminho_ridge[:, i])
    ax3b.plot(alphas, caminho_lasso[:, i])

for ax, titulo in [(ax3a, "Ridge (L2): coeficientes encolhem suavemente"),
                    (ax3b, "Lasso (L1): coeficientes vão a zero um a um")]:
    ax.set_xscale("log")
    ax.set_xlabel("alpha (força da regularização, escala log)")
    ax.set_ylabel("Valor do coeficiente")
    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.axhline(0, color="black", linewidth=0.7)

fig3.suptitle("Caminho de regularização: como os coeficientes mudam com alpha",
              fontsize=14, fontweight="bold")
fig3.tight_layout(rect=[0, 0, 1, 0.94])
fig3.savefig("/home/claude/3_caminho_regularizacao.png", dpi=130)
plt.close(fig3)

# ------------------------------------------------------------------------
# 6) GRÁFICO 4: erro de treino x erro de teste em função de alpha (Ridge)
# ------------------------------------------------------------------------
# Clássico gráfico de "underfitting <-> sweet spot <-> overfitting":
# com alpha muito baixo, o modelo decora o treino (overfitting);
# com alpha muito alto, o modelo fica simples demais (underfitting).
rmse_treino_lista, rmse_teste_lista = [], []
for a in alphas:
    pipe = make_pipeline(
        PolynomialFeatures(degree=GRAU_POLINOMIO, include_bias=False),
        StandardScaler(),
        Ridge(alpha=a),
    )
    pipe.fit(X_treino, y_treino)
    rmse_treino_lista.append(np.sqrt(mean_squared_error(y_treino, pipe.predict(X_treino))))
    rmse_teste_lista.append(np.sqrt(mean_squared_error(y_teste, pipe.predict(X_teste))))

melhor_idx = int(np.argmin(rmse_teste_lista))
melhor_alpha = alphas[melhor_idx]

fig4, ax4 = plt.subplots(figsize=(9, 5.5))
ax4.plot(alphas, rmse_treino_lista, label="Erro (RMSE) no treino", color="tab:blue")
ax4.plot(alphas, rmse_teste_lista, label="Erro (RMSE) no teste", color="tab:orange")
ax4.axvline(melhor_alpha, color="green", linestyle="--",
            label=f"Melhor alpha ≈ {melhor_alpha:.4f}")
ax4.set_xscale("log")
ax4.set_xlabel("alpha (força da regularização, escala log)")
ax4.set_ylabel("RMSE")
ax4.set_title(
    "Ridge: underfitting <-> ponto ótimo <-> overfitting\n"
    "conforme alpha aumenta", fontsize=12, fontweight="bold"
)
ax4.legend()
fig4.tight_layout()
fig4.savefig("/home/claude/4_underfitting_overfitting_alpha.png", dpi=130)
plt.close(fig4)

print("\nGráficos salvos em /home/claude/:")
print(" 1_overfitting_vs_regularizacao.png")
print(" 2_comparacao_coeficientes.png")
print(" 3_caminho_regularizacao.png")
print(" 4_underfitting_overfitting_alpha.png")
