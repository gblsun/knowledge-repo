# ==============================================================================
#  PROJETO    : Regularização em Modelos de Regressão
#  ARQUIVO    : regularizacao_demo.py
#  AUTOR(A)   : << coloque seu nome aqui >>
#  CURSO      : Ciência da Computação
#  DATA       : 26/08/2026
# ------------------------------------------------------------------------------
#  DESCRIÇÃO  : Demonstração prática e visual de overfitting (sobreajuste) e
#               das três técnicas clássicas de regularização usadas para
#               combatê-lo: L2 (Ridge), L1 (Lasso) e a mistura das duas,
#               Elastic Net. Ajusta-se um polinômio de grau alto a um
#               conjunto de dados ruidosos e compara-se o comportamento do
#               modelo sem regularização com o de cada técnica regularizada.
#
#  REFERÊNCIA PRINCIPAL (teoria, fórmulas e propriedades citadas ao longo
#  deste arquivo):
#      MORETTIN, P. A.; SINGER, J. M. Estatística e Ciência de Dados.
#      1. ed. Rio de Janeiro: LTC, 2022. Capítulo 8 — "Regularização e
#      Modelos Aditivos Generalizados", Seção 8.2 "Regularização"
#      (Subseções 8.2.1 Ridge, 8.2.2 Lasso, 8.2.3 Elastic Net).
# ==============================================================================

"""
TEORIA — visão geral
==============================================================================

1) OVERFITTING (sobreajuste)
------------------------------------------------------------------------------
Um modelo sofre overfitting quando é complexo demais para a quantidade e a
qualidade dos dados disponíveis: em vez de aprender o padrão real, ele
"decora" o ruído do conjunto de treino. O sintoma é sempre o mesmo — erro
baixíssimo no treino, mas erro alto em dados novos (teste); o modelo não
generaliza.

Este script reproduz, em espírito, o experimento clássico apresentado por
Bishop (2006) e retomado no livro-texto (MORETTIN; SINGER, 2022, Cap. 8,
Seção 8.2, Figura 8.1): ajustam-se polinômios de graus crescentes a pontos
gerados por
                      yᵢ = sen(2πxᵢ) + eᵢ ,   eᵢ ~ N(0, σ²)
Um polinômio de grau baixo não consegue capturar a curva (underfitting); um
polinômio de grau muito alto passa quase exatamente pelos pontos de treino,
mas oscila descontroladamente entre eles — esse é o sobreajuste. Abaixo,
usamos exatamente essa ideia (grau 15 sobre uma senoide ruidosa) para deixar
o fenômeno bem visível.

2) REGULARIZAÇÃO (definição geral)
------------------------------------------------------------------------------
Regularização é o conjunto de técnicas usadas para ajustar modelos que se
adaptem aos dados evitando o sobreajuste, adicionando à função de perda
(soma de quadrados dos erros) um TERMO DE PENALIZAÇÃO que reduz a influência
de coeficientes responsáveis por flutuações excessivas do modelo
(MORETTIN; SINGER, 2022, Cap. 8, Seção 8.2).

Partindo do modelo de regressão linear (equivalente à Eq. 8.1 do livro-texto)

              yₜ = β₀ + β₁x₁ₜ + ... + βₚxₚₜ + eₜ ,   t = 1, ..., n

o ajuste "comum" por mínimos quadrados minimiza apenas Σₜ(yₜ − βᵀxₜ)². As
três técnicas abaixo (Seção 8.2) diferem exatamente no termo de penalização
somado a essa soma de quadrados.

3) REGULARIZAÇÃO L2 — RIDGE  (Seção 8.2.1)
------------------------------------------------------------------------------
Introduzida por Hoerl e Kennard (1970) originalmente para tratar o problema
da multicolinearidade, também é eficaz contra o sobreajuste. Penaliza a SOMA
DOS QUADRADOS dos coeficientes (equivalente à Eq. 8.2):

    β̂_Ridge(λ) = argmin_β [ Σₜ(yₜ − βᵀxₜ)²  +  λ·Σⱼβⱼ² ]

em que λ ≥ 0 é o coeficiente de regularização: λ = 0 reproduz os mínimos
quadrados comuns e λ → ∞ encolhe todos os coeficientes em direção a zero
(sem, em geral, zerá-los). Possui forma fechada (equivalente à Eq. 8.4):

    β̂_Ridge(λ) = (XᵀX + λI)⁻¹Xᵀy

Propriedades citadas no livro-texto (Seção 8.2.1):
  i)   o estimador Ridge não é consistente, mas é assintoticamente
       consistente sob condições sobre λ, p e n;
  ii)  é enviesado (biased) para os parâmetros não nulos;
  iii) NÃO serve para seleção de variáveis (em geral não zera coeficientes);
  iv)  λ é escolhido via validação cruzada ou algum critério de informação.

4) REGULARIZAÇÃO L1 — LASSO, "least absolute shrinkage and selection
   operator"  (Seção 8.2.2)
------------------------------------------------------------------------------
Proposta por Tibshirani (1996). Penaliza a SOMA DOS VALORES ABSOLUTOS dos
coeficientes (equivalente à Eq. 8.5):

    β̂_Lasso(λ) = argmin_β [ Σₜ(yₜ − βᵀxₜ)²  +  λ·Σⱼ|βⱼ| ]

Diferentemente do Ridge, essa penalidade consegue ZERAR coeficientes por
completo: o Lasso funciona também como um SELETOR DE VARIÁVEIS, produzindo
soluções esparsas. Quando p = n (nº de preditores = nº de observações), a
técnica equivale à aplicação de um limiar brando / soft threshold
(equivalente à Eq. 8.7):

    β̂ⱼ(λ) = sinal(Zⱼ)·(|Zⱼ| − λ/2)₊ ,     (x)₊ = max{x, 0}

Propriedades citadas no livro-texto (Seção 8.2.2):
  i)   coeficientes de preditores redundantes são encolhidos a zero;
  ii)  é enviesado para os parâmetros não nulos;
  iii) sob certas condições, descarta variáveis irrelevantes do modelo,
       atribuindo peso nulo aos respectivos coeficientes.

5) ELASTIC NET (Seção 8.2.3)
------------------------------------------------------------------------------
Mistura as duas penalidades anteriores (equivalente à Eq. 8.8):

    β̂_EN(λ₁,λ₂) = argmin_β [ Σₜ(yₜ−βᵀxₜ)² + λ₁·Σⱼβⱼ² + λ₂·Σⱼ|βⱼ| ]

Uma parametrização equivalente usa α = λ₂/(λ₁+λ₂) ∈ [0, 1] para controlar a
MISTURA entre L1 e L2 (α = 1 → Lasso puro; α = 0 → Ridge puro) — é
exatamente o papel do parâmetro `l1_ratio` do scikit-learn (ver item 7).
Sob certas condições, o estimador Elastic Net é consistente
(MORETTIN; SINGER, 2022, Cap. 8, Seção 8.2.3).

6) POR QUE O LASSO ZERA COEFICIENTES E O RIDGE NÃO (intuição geométrica —
   Figura 8.2 do livro-texto)
------------------------------------------------------------------------------
Minimizar a soma de quadrados sujeita a uma restrição sobre o tamanho de β é
equivalente a encontrar o ponto em que as curvas de nível da soma de
quadrados dos resíduos (elipses/círculos concêntricos ao redor do estimador
de mínimos quadrados) TANGENCIAM a região delimitada pela restrição. No
Ridge, essa região (Σβⱼ² ≤ m) é um CÍRCULO — uma superfície lisa, sem
"quinas" — de modo que o ponto de tangência raramente cai exatamente sobre
um eixo (ou seja, raramente algum βⱼ = 0). No Lasso, a região (Σ|βⱼ| ≤ m) é
um LOSANGO, com QUINAS exatamente sobre os eixos, e é justamente nessas
quinas que a tangência costuma ocorrer — zerando um ou mais coeficientes.
Esse é o motivo geométrico pelo qual o Lasso gera soluções esparsas e o
Ridge não (MORETTIN; SINGER, 2022, Cap. 8, Fig. 8.2). O Gráfico 2 e o
Gráfico 3 gerados por este script tornam esse efeito visível nos dados.

7) DO LIVRO PARA O CÓDIGO: A NOTAÇÃO DO SCIKIT-LEARN
------------------------------------------------------------------------------
  • O parâmetro `alpha` do scikit-learn corresponde ao λ (lambda) do livro.
  • `Ridge` minimiza exatamente a Eq. 8.2: ||y − Xw||² + alpha·||w||².
  • `Lasso` minimiza (1/(2n))·||y − Xw||² + alpha·||w||₁ — repare que,
    diferentemente do Ridge, o termo de erro é dividido por 2n. Por isso os
    valores de alpha do Ridge e do Lasso NÃO são diretamente comparáveis
    entre si; é por isso que este script usa ordens de grandeza diferentes
    de alpha para cada modelo (ver Seção 2 do código, mais abaixo).
  • `ElasticNet` tem um segundo parâmetro, `l1_ratio`, que corresponde
    exatamente ao α = λ₂/(λ₁+λ₂) da Eq. 8.9 (l1_ratio=1 → Lasso puro;
    l1_ratio=0 → Ridge puro). O próprio livro usa essa mesma convenção no
    pacote R `glmnet`, no Exemplo 8.1 (alpha=0 → Ridge, alpha=1 → Lasso,
    alpha=0,5 → Elastic Net) — a ideia é idêntica à do `l1_ratio` aqui.

------------------------------------------------------------------------------
REFERÊNCIA PRINCIPAL
    MORETTIN, P. A.; SINGER, J. M. Estatística e Ciência de Dados. 1. ed.
    Rio de Janeiro: LTC, 2022. Cap. 8, Seção 8.2.
FONTES CITADAS PELO PRÓPRIO LIVRO-TEXTO NESSA SEÇÃO
    BISHOP, C. M. Pattern Recognition and Machine Learning. New York:
      Springer, 2006. [origem do experimento de overfitting reproduzido aqui]
    HOERL, A. E.; KENNARD, R. W. Ridge regression: biased estimation for
      nonorthogonal problems. Technometrics, 12, 55-67, 1970.
    TIBSHIRANI, R. Regression shrinkage and selection via the lasso.
      Journal of the Royal Statistical Society B, 58, 267-288, 1996.
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Semente fixa: garante que os dados "aleatórios" gerados abaixo sejam
# sempre os mesmos a cada execução (reprodutibilidade dos resultados).
np.random.seed(42)

# ==============================================================================
# 1) GERANDO DADOS SINTÉTICOS (réplica do experimento da Seção 8.2 / Fig. 8.1)
# ==============================================================================
# Criamos uma relação real simples -- uma senoide, yᵢ = sen(2πxᵢ) + eᵢ, com
# eᵢ ~ N(0, σ²) -- e vamos ajustar um polinômio de grau ALTO a esses poucos
# pontos ruidosos. Ajustar um modelo muito flexível a poucos dados é a
# receita clássica para o overfitting descrito na Seção 1 da introdução acima.
n_amostras = 30
X = np.sort(np.random.uniform(0, 1, n_amostras))      # pontos xᵢ em [0, 1]
y_real = np.sin(2 * np.pi * X)                         # função geradora real
ruido = np.random.normal(0, 0.25, n_amostras)          # eᵢ ~ N(0, 0.25²)
y = y_real + ruido                                     # yᵢ observado (com ruído)

X = X.reshape(-1, 1)  # sklearn espera X em formato de matriz (n_amostras, 1)

# Separamos 30% dos pontos como conjunto de TESTE: são os dados "novos" que
# o modelo nunca vê durante o treino. É comparando o erro no treino com o
# erro no teste que detectamos o overfitting (Seção 1 acima).
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Grade fina de pontos (não usada no treino) só para desenhar as curvas
# ajustadas de forma suave nos gráficos.
X_plot = np.linspace(0, 1, 300).reshape(-1, 1)
y_plot_real = np.sin(2 * np.pi * X_plot).ravel()

# Grau do polinômio ajustado. Um valor tão alto quanto 15 para apenas ~20
# pontos de treino é proposital: é o que torna o overfitting evidente sem
# regularização (o polinômio tem graus de liberdade de sobra para passar
# quase exatamente pelos pontos de treino e ainda oscilar entre eles).
GRAU_POLINOMIO = 15


def treinar_modelo(modelo, grau=GRAU_POLINOMIO):
    """Treina um modelo de regressão sobre features polinomiais padronizadas.

    Monta um Pipeline com três etapas, na ordem em que são aplicadas:
        1. PolynomialFeatures : expande x em [x, x², x³, ..., x^grau],
           transformando a regressão simples em uma regressão polinomial
           (é o que permite ao modelo "curvar" o suficiente para se ajustar
           -- ou sobreajustar -- aos dados).
        2. StandardScaler     : padroniza cada coluna (média 0, desvio 1).
           Este passo é ESSENCIAL antes de qualquer regularização: como o
           termo de penalização (λ·Σβⱼ² no Ridge, λ·Σ|βⱼ| no Lasso) atua
           diretamente sobre o valor numérico dos coeficientes, variáveis em
           escalas diferentes (aqui, x, x² , ..., x¹⁵ têm magnitudes muito
           diferentes) seriam penalizadas de forma desigual e injusta se não
           fossem levadas à mesma escala primeiro.
        3. modelo              : o regressor propriamente dito (recebido
           como argumento -- LinearRegression, Ridge, Lasso ou ElasticNet).

    Args:
        modelo: instância de um regressor scikit-learn já configurado
            (por exemplo, Ridge(alpha=0.01)).
        grau: grau do polinômio usado em PolynomialFeatures.

    Returns:
        O Pipeline já treinado (fit) sobre (X_treino, y_treino).
    """
    pipeline = make_pipeline(
        PolynomialFeatures(degree=grau, include_bias=False),
        StandardScaler(),
        modelo,
    )
    pipeline.fit(X_treino, y_treino)
    return pipeline


def avaliar_modelo(pipeline, nome):
    """Calcula e imprime métricas de treino e teste para um modelo treinado.

    Comparar o erro no treino com o erro no teste é exatamente como se
    diagnostica overfitting na prática: um RMSE de treino baixo acompanhado
    de um RMSE de teste muito maior é a assinatura de um modelo que decorou
    o ruído do treino em vez de aprender o padrão (ver Seção 1 da
    introdução teórica, no topo do arquivo).

    Args:
        pipeline: Pipeline já treinado (retornado por treinar_modelo).
        nome: rótulo do modelo, usado apenas na impressão do resultado.

    Returns:
        Tupla (rmse_treino, rmse_teste) com a raiz do erro quadrático médio
        em cada conjunto.
    """
    pred_treino = pipeline.predict(X_treino)
    pred_teste = pipeline.predict(X_teste)
    rmse_treino = np.sqrt(mean_squared_error(y_treino, pred_treino))
    rmse_teste = np.sqrt(mean_squared_error(y_teste, pred_teste))
    r2_teste = r2_score(y_teste, pred_teste)
    print(f"{nome:22s} | RMSE treino: {rmse_treino:6.3f} | "
          f"RMSE teste: {rmse_teste:6.3f} | R2 teste: {r2_teste:6.3f}")
    return rmse_treino, rmse_teste


# ==============================================================================
# 2) TREINANDO OS QUATRO MODELOS: sem regularização, Ridge, Lasso, Elastic Net
# ==============================================================================
print("=" * 78)
print("COMPARAÇÃO DE MODELOS (polinômio de grau", GRAU_POLINOMIO, ")")
print("=" * 78)

# Os valores de alpha (λ) foram escolhidos em ordens de grandeza DIFERENTES
# de propósito: como visto no item 7 da introdução teórica, a implementação
# do Lasso/ElasticNet no scikit-learn normaliza o termo de erro por 1/(2n),
# enquanto a do Ridge não -- então um mesmo alpha numérico não representa a
# mesma "força" de penalização nos três modelos.
modelo_sem_reg = treinar_modelo(LinearRegression())               # λ = 0 (sem penalidade)
modelo_ridge = treinar_modelo(Ridge(alpha=0.01))                  # penalidade L2
modelo_lasso = treinar_modelo(Lasso(alpha=0.001, max_iter=20000))  # penalidade L1
modelo_elastic = treinar_modelo(                                   # mistura L1+L2
    ElasticNet(alpha=0.002, l1_ratio=0.5, max_iter=20000)          # l1_ratio=0.5 -> α=0,5, como no Exemplo 8.1 do livro
)

avaliar_modelo(modelo_sem_reg, "Sem regularização")
avaliar_modelo(modelo_ridge, "Ridge (L2)")
avaliar_modelo(modelo_lasso, "Lasso (L1)")
avaliar_modelo(modelo_elastic, "Elastic Net")
print("=" * 78)

# ==============================================================================
# 3) GRÁFICO 1 — overfitting vs. modelos regularizados
# ==============================================================================
# Um painel por modelo: a curva real (tracejada), os pontos de treino/teste
# e a curva efetivamente aprendida pelo modelo. O painel "Sem regularização"
# deve mostrar uma curva que passa quase exatamente pelos pontos cinza
# (treino) mas oscila de forma extrema entre eles -- a marca registrada do
# overfitting (Seção 1 da introdução). Os outros três painéis mostram como
# cada penalidade "acalma" essas oscilações.
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

# ==============================================================================
# 4) GRÁFICO 2 — comparação dos coeficientes aprendidos por cada modelo
# ==============================================================================
# Aqui mostramos, lado a lado, o valor de cada um dos 15 coeficientes do
# polinômio (um por grau: x¹, x², ..., x¹⁵) para os quatro modelos. É a
# melhor forma de "ver" a diferença de comportamento entre L1 e L2 descrita
# no item 6 da introdução teórica (intuição geométrica da Figura 8.2 do
# livro-texto): espera-se que várias barras do Lasso e do Elastic Net sejam
# exatamente zero, enquanto as do Ridge apenas encolhem, sem se anular.
def pega_coeficientes(pipeline):
    """Extrai o vetor de coeficientes (β̂) do último passo de um Pipeline.

    `pipeline.named_steps` é um dicionário ordenado com as etapas do
    Pipeline (ex.: 'polynomialfeatures', 'standardscaler', 'ridge'); o
    último passo é sempre o regressor propriamente dito, cujo atributo
    `.coef_` guarda os coeficientes β̂₁, ..., β̂ₚ estimados (o intercepto β̂₀
    fica em `.intercept_` e não entra nessa comparação, assim como não
    entra no termo de penalização -- ver item 3 da introdução teórica).

    Args:
        pipeline: Pipeline já treinado (retornado por treinar_modelo).

    Returns:
        Array numpy com os coeficientes do modelo final do pipeline.
    """
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

# Contagem de coeficientes "praticamente zero" (tolerância numérica, já que
# soluções de otimização raramente são EXATAMENTE 0.000000...).  Esperamos
# Ridge ≈ 0 zeros (propriedade iii, Seção 8.2.1) e Lasso/Elastic Net > 0
# zeros (propriedade i, Seção 8.2.2) -- a "seleção de variáveis" na prática.
n_zeros_lasso = np.sum(np.isclose(coefs_lasso, 0, atol=1e-3))
n_zeros_elastic = np.sum(np.isclose(coefs_elastic, 0, atol=1e-3))
n_zeros_ridge = np.sum(np.isclose(coefs_ridge, 0, atol=1e-3))
print(f"Coeficientes zerados -> Ridge: {n_zeros_ridge}/{n_coefs} | "
      f"Lasso: {n_zeros_lasso}/{n_coefs} | Elastic Net: {n_zeros_elastic}/{n_coefs}")

# ==============================================================================
# 5) GRÁFICO 3 — caminho de regularização (coeficientes em função de alpha)
# ==============================================================================
# "Caminho de regularização" (regularization path) é o nome dado à trajetória
# de cada coeficiente à medida que alpha (λ) varia -- é justamente o título
# do artigo de Friedman, Hastie e Tibshirani (2010) citado pelo livro-texto
# como a referência do pacote glmnet usado no Exemplo 8.1. Aqui reproduzimos
# a mesma ideia com o scikit-learn: no Ridge, espera-se que os coeficientes
# encolham SUAVEMENTE e continuamente até perto de zero; no Lasso, espera-se
# que cada coeficiente "morra" (vire exatamente zero) em um alpha diferente,
# um a um -- é essa diferença de comportamento que torna o Lasso um seletor
# de variáveis, como discutido no item 6 da introdução teórica.
alphas = np.logspace(-4, 1, 60)  # escala log: a "força" da penalização atua
                                  # de forma multiplicativa, não aditiva, então
                                  # varrer alpha em escala log cobre melhor as
                                  # ordens de grandeza relevantes do que uma
                                  # escala linear cobriria.

def caminho_coeficientes(ClasseModelo, alphas, **kwargs):
    """Treina o mesmo modelo repetidas vezes, variando alpha, e devolve
    o histórico de coeficientes obtidos em cada valor de alpha.

    Args:
        ClasseModelo: a classe do regressor a ser instanciada a cada
            iteração (Ridge ou Lasso).
        alphas: sequência de valores de alpha (λ) a percorrer.
        **kwargs: argumentos extras repassados ao construtor do modelo
            (por exemplo, max_iter para o Lasso).

    Returns:
        Array numpy de forma (len(alphas), n_coefs) com os coeficientes
        aprendidos em cada valor de alpha -- uma linha por alpha.
    """
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

# ==============================================================================
# 6) GRÁFICO 4 — erro de treino x erro de teste em função de alpha (Ridge)
# ==============================================================================
# O clássico gráfico "underfitting <-> ponto ótimo <-> overfitting": com
# alpha muito baixo (penalização fraca), o modelo ainda decora o ruído do
# treino (overfitting); com alpha muito alto (penalização forte demais), o
# modelo fica simples demais para capturar até o padrão real (underfitting).
# O alpha ótimo -- aquele que minimiza o erro no conjunto de TESTE, nunca no
# de treino -- fica em algum ponto entre esses dois extremos. No livro-texto
# (Exemplo 8.1), essa busca é feita por validação cruzada via
# cv.glmnet(..., alpha=0) no R; aqui fazemos o equivalente de forma manual,
# varrendo o mesmo vetor `alphas` do Gráfico 3 e comparando RMSE de treino
# e de teste (propriedade iv da Seção 8.2.1: a escolha de λ é um dos
# componentes da estratégia de regularização).
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