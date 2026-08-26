# Regularização em Modelos de Regressão — Overfitting, Ridge, Lasso e Elastic Net

Script em Python (`regularizacao_demo.py`) que demonstra, de forma prática e
visual, o fenômeno do **overfitting (sobreajuste)** e como três técnicas de
**regularização** — Ridge (L2), Lasso (L1) e Elastic Net — ajudam a evitá-lo.

> Fundamentação teórica baseada no Capítulo 8 ("Regularização e Modelos
> Aditivos Generalizados"), Seção 8.2, de:
> **MORETTIN, P. A.; SINGER, J. M. Estatística e Ciência de Dados.** 1. ed.
> Rio de Janeiro: LTC, 2022. ISBN 978-85-216-3816-2.

## Sumário

- [Como executar](#como-executar)
- [O que o script faz](#o-que-o-script-faz)
- [Fundamentação teórica](#fundamentação-teórica)
  - [1. Overfitting (sobreajuste)](#1-overfitting-sobreajuste)
  - [2. Regularização](#2-regularização)
  - [3. Regularização L2 — Ridge](#3-regularização-l2--ridge)
  - [4. Regularização L1 — Lasso](#4-regularização-l1--lasso)
  - [5. Elastic Net](#5-elastic-net)
  - [6. Por que o Lasso zera coeficientes e o Ridge não](#6-por-que-o-lasso-zera-coeficientes-e-o-ridge-não)
- [Do livro para o código: notação do scikit-learn](#do-livro-para-o-código-notação-do-scikit-learn)
- [Os gráficos gerados](#os-gráficos-gerados)
- [Resultados obtidos](#resultados-obtidos-última-execução)
- [Estrutura de arquivos](#estrutura-de-arquivos)
- [Referências](#referências)

## Como executar

```bash
pip install numpy matplotlib scikit-learn
python3 regularizacao_demo.py
```

O script imprime no terminal uma tabela comparativa (RMSE de treino/teste,
R² e nº de coeficientes zerados) e salva 4 imagens `.png` na mesma pasta.

## O que o script faz

1. Gera um conjunto sintético de 30 pontos a partir de `y = sen(2πx) + ruído`
   — a mesma construção usada no exemplo clássico de overfitting do
   livro-texto (Seção 8.2, Figura 8.1).
2. Ajusta um **polinômio de grau 15** a esses pontos usando quatro
   abordagens: sem regularização, Ridge, Lasso e Elastic Net.
3. Compara o erro (RMSE) e o R² de cada modelo no treino **e** no teste —
   é essa comparação que revela o overfitting.
4. Gera 4 gráficos (explicados [abaixo](#os-gráficos-gerados)) que tornam
   visíveis o overfitting, o efeito de cada penalidade sobre os
   coeficientes, e o trade-off entre viés e variância.

## Fundamentação teórica

### 1. Overfitting (sobreajuste)

Um modelo sofre overfitting quando é complexo demais para a quantidade e a
qualidade dos dados disponíveis: em vez de aprender o padrão real, ele
"decora" o ruído do conjunto de treino. O sintoma é sempre o mesmo: erro
baixíssimo no treino, mas erro alto em dados novos (teste) — o modelo não
generaliza.

O script reproduz, em espírito, o experimento proposto por **Bishop (2006)**
e retomado no livro-texto: ajustam-se polinômios a pontos gerados por

```
yᵢ = sen(2πxᵢ) + eᵢ ,   eᵢ ~ N(0, σ²)
```

Um polinômio de grau baixo não consegue capturar a curva (underfitting); um
de grau muito alto passa quase exatamente pelos pontos de treino, mas oscila
descontroladamente entre eles — esse é o sobreajuste (MORETTIN; SINGER,
2022, Cap. 8, Seção 8.2).

### 2. Regularização

> "O termo regularização refere-se a um conjunto de técnicas utilizadas para
> especificar modelos que se ajustem a um conjunto de dados evitando o
> sobreajuste" — em outras palavras, soma-se à função de perda um **termo de
> penalização** que reduz a influência de coeficientes responsáveis por
> flutuações excessivas do modelo (MORETTIN; SINGER, 2022, Cap. 8, Seção 8.2).

Partindo do modelo linear

```
yₜ = β₀ + β₁x₁ₜ + ... + βₚxₚₜ + eₜ ,   t = 1, ..., n            (Eq. 8.1)
```

o ajuste comum por mínimos quadrados minimiza apenas `Σ(yₜ − βᵀxₜ)²`. As três
técnicas a seguir diferem no termo de penalização somado a essa soma de
quadrados (MORETTIN; SINGER, 2022, Cap. 8, Seção 8.2).

### 3. Regularização L2 — Ridge

Introduzida por **Hoerl e Kennard (1970)** para tratar o problema da
multicolinearidade, também é eficaz contra o sobreajuste. Penaliza a **soma
dos quadrados** dos coeficientes:

```
β̂_Ridge(λ) = argmin_β [ Σ(yₜ − βᵀxₜ)²  +  λ·Σβⱼ² ]              (Eq. 8.2)
```

```latex
\hat{\boldsymbol\beta}_{Ridge}(\lambda) = \arg\min_{\boldsymbol\beta}
\left[ \sum_{t=1}^{n} (y_t - \boldsymbol\beta^\top \mathbf{x}_t)^2
+ \lambda \sum_{j=1}^{p} \beta_j^2 \right]
```

com solução em forma fechada `β̂_Ridge(λ) = (XᵀX + λI)⁻¹Xᵀy` (Eq. 8.4).
λ = 0 reproduz os mínimos quadrados comuns; λ → ∞ encolhe todos os
coeficientes em direção a zero, mas raramente os anula.

**Propriedades** (MORETTIN; SINGER, 2022, Seção 8.2.1):
| # | Propriedade |
|---|---|
| i | Não é consistente, mas é assintoticamente consistente sob condições sobre λ, p e n |
| ii | É enviesado (*biased*) para os parâmetros não nulos |
| iii | **Não** serve para seleção de variáveis (em geral não zera coeficientes) |
| iv | λ é escolhido via validação cruzada ou algum critério de informação |

### 4. Regularização L1 — Lasso

*Least Absolute Shrinkage and Selection Operator*, proposto por
**Tibshirani (1996)**. Penaliza a **soma dos valores absolutos** dos
coeficientes:

```
β̂_Lasso(λ) = argmin_β [ Σ(yₜ − βᵀxₜ)²  +  λ·Σ|βⱼ| ]              (Eq. 8.5)
```

```latex
\hat{\boldsymbol\beta}_{Lasso}(\lambda) = \arg\min_{\boldsymbol\beta}
\left[ \sum_{t=1}^{n} (y_t - \boldsymbol\beta^\top \mathbf{x}_t)^2
+ \lambda \sum_{j=1}^{p} |\beta_j| \right]
```

Diferentemente do Ridge, essa penalidade consegue **zerar coeficientes por
completo** — o Lasso funciona também como um **seletor de variáveis**,
produzindo soluções esparsas. Quando p = n, a técnica equivale a um limiar
brando (*soft threshold*): `β̂ⱼ(λ) = sinal(Zⱼ)·(|Zⱼ| − λ/2)₊` (Eq. 8.7).

**Propriedades** (MORETTIN; SINGER, 2022, Seção 8.2.2):
| # | Propriedade |
|---|---|
| i | Coeficientes de preditores redundantes são encolhidos a zero |
| ii | É enviesado para os parâmetros não nulos |
| iii | Sob certas condições, descarta variáveis irrelevantes (peso nulo) |

### 5. Elastic Net

Mistura as duas penalidades anteriores:

```
β̂_EN(λ1,λ2) = argmin_β [ Σ(yₜ−βᵀxₜ)² + λ1·Σβⱼ² + λ2·Σ|βⱼ| ]      (Eq. 8.8)
```

```latex
\hat{\boldsymbol\beta}_{EN}(\lambda_1,\lambda_2) = \arg\min_{\boldsymbol\beta}
\left[ \sum_{t=1}^{n} (y_t - \boldsymbol\beta^\top \mathbf{x}_t)^2
+ \lambda_1 \sum_{j=1}^{p} \beta_j^2 + \lambda_2 \sum_{j=1}^{p} |\beta_j| \right]
```

Uma parametrização equivalente usa `α = λ2/(λ1+λ2) ∈ [0,1]` para controlar a
mistura entre L1 e L2 (α=1 → Lasso puro; α=0 → Ridge puro) — é exatamente o
papel do parâmetro `l1_ratio` do scikit-learn. Sob certas condições, o
estimador Elastic Net é consistente (MORETTIN; SINGER, 2022, Seção 8.2.3).

### 6. Por que o Lasso zera coeficientes e o Ridge não

Intuição geométrica (Figura 8.2 do livro-texto): minimizar a soma de
quadrados sujeita a uma restrição sobre o tamanho de β equivale a encontrar
o ponto em que as curvas de nível da soma de quadrados dos resíduos
(elipses/círculos concêntricos) **tangenciam** a região delimitada pela
restrição.

- No **Ridge**, essa região (`Σβⱼ² ≤ m`) é um **círculo** — uma superfície
  lisa, sem "quinas" — então o ponto de tangência raramente cai exatamente
  sobre um eixo (ou seja, raramente algum βⱼ = 0).
- No **Lasso**, a região (`Σ|βⱼ| ≤ m`) é um **losango**, com quinas
  exatamente sobre os eixos, e é justamente nessas quinas que a tangência
  costuma ocorrer — zerando um ou mais coeficientes.

Esse é o motivo geométrico pelo qual o Lasso gera soluções esparsas e o
Ridge não (MORETTIN; SINGER, 2022, Cap. 8, Fig. 8.2). Os **Gráficos 2 e 3**
gerados pelo script tornam esse efeito visível nos dados do experimento.

## Do livro para o código: notação do scikit-learn

| Livro-texto (Cap. 8) | Significado | scikit-learn |
|---|---|---|
| λ (lambda) | coeficiente de regularização | `alpha` |
| Σβⱼ² (Eq. 8.2) | penalidade L2 | `Ridge(alpha=...)` |
| Σ\|βⱼ\| (Eq. 8.5) | penalidade L1 | `Lasso(alpha=...)` |
| α = λ2/(λ1+λ2) (Eq. 8.9) | mistura L1/L2 | `ElasticNet(l1_ratio=...)` |

**Nota técnica importante:** a implementação do scikit-learn normaliza o
termo de erro quadrático por `1/(2n)` no Lasso e no Elastic Net, mas **não**
no Ridge:

- `Ridge` minimiza `‖y − Xw‖² + alpha·‖w‖²` — igual à Eq. 8.2.
- `Lasso` minimiza `(1/(2n))·‖y − Xw‖² + alpha·‖w‖₁`.
- `ElasticNet` minimiza `(1/(2n))·‖y − Xw‖² + alpha·l1_ratio·‖w‖₁ + 0.5·alpha·(1−l1_ratio)·‖w‖²`.

Por isso, valores de `alpha` do Ridge e do Lasso **não são diretamente
comparáveis** entre si — o script usa ordens de grandeza diferentes de alpha
para cada modelo por esse motivo. O próprio livro-texto usa essa mesma
lógica de mistura no pacote R `glmnet`, no Exemplo 8.1 do Capítulo 8
(`alpha=0` → Ridge, `alpha=1` → Lasso, `alpha=0,5` → Elastic Net) — o
`alpha` do `glmnet` corresponde ao `l1_ratio` do scikit-learn, não ao `alpha`
dele.

## Os gráficos gerados

| Arquivo | O que mostra |
|---|---|
| `1_overfitting_vs_regularizacao.png` | Um painel por modelo: a curva real, os pontos de treino/teste e a curva aprendida. O painel "sem regularização" mostra o polinômio de grau 15 oscilando de forma extrema entre os pontos — o overfitting visível. |
| `2_comparacao_coeficientes.png` | Os 15 coeficientes de cada modelo lado a lado. Mostra a esparsidade do Lasso/Elastic Net (várias barras em zero) versus o Ridge, que só encolhe os coeficientes. |
| `3_caminho_regularizacao.png` | O "caminho de regularização": cada coeficiente em função de alpha. No Ridge as curvas encolhem suavemente; no Lasso, cada curva "morre" (chega a zero) em um alpha diferente. |
| `4_underfitting_overfitting_alpha.png` | RMSE de treino x teste em função de alpha, para o Ridge. Mostra o clássico formato em U do erro de teste: overfitting à esquerda (alpha baixo), underfitting à direita (alpha alto), com o ponto ótimo marcado. |

## Resultados obtidos (última execução)

| Modelo | RMSE treino | RMSE teste | R² teste | Coeficientes zerados |
|---|---|---|---|---|
| Sem regularização | 0,149 | 715,097 | −829575,061 | 0/15 |
| Ridge (L2) | 0,216 | 0,203 | 0,933 | 0/15 |
| Lasso (L1) | 0,211 | 0,216 | 0,925 | 11/15 |
| Elastic Net | 0,230 | 0,215 | 0,925 | 6/15 |

O salto absurdo no RMSE de teste "sem regularização" (0,149 no treino contra
715 no teste!) é o overfitting em estado puro: o polinômio de grau 15 se
ajustou perfeitamente ao ruído dos 21 pontos de treino e, por isso mesmo,
explode fora deles. As três técnicas de regularização trazem o erro de
teste de volta para perto do erro de treino — sinal de que o modelo voltou
a generalizar.

## Estrutura de arquivos

```
.
├── regularizacao_demo.py                     # script principal (documentado)
├── README.md                                  # este arquivo
├── 1_overfitting_vs_regularizacao.png
├── 2_comparacao_coeficientes.png
├── 3_caminho_regularizacao.png
└── 4_underfitting_overfitting_alpha.png
```

## Referências

**Fonte principal:**

MORETTIN, P. A.; SINGER, J. M. **Estatística e Ciência de Dados**. 1. ed.
Rio de Janeiro: LTC, 2022. Capítulo 8 — Regularização e Modelos Aditivos
Generalizados, Seção 8.2. ISBN 978-85-216-3816-2.

**Fontes citadas pelo próprio livro-texto nessa seção:**

- BISHOP, C. M. *Pattern Recognition and Machine Learning*. New York:
  Springer, 2006. — origem do experimento de overfitting reproduzido aqui.
- HOERL, A. E.; KENNARD, R. W. Ridge regression: biased estimation for
  nonorthogonal problems. *Technometrics*, 12, p. 55-67, 1970.
- TIBSHIRANI, R. Regression shrinkage and selection via the lasso.
  *Journal of the Royal Statistical Society*, Series B, 58, p. 267-288, 1996.
- FRIEDMAN, J. H.; HASTIE, T.; TIBSHIRANI, R. Regularization paths for
  generalized linear models via coordinate descent. *Journal of Statistical
  Software*, 33, p. 1-22, 2010. — algoritmo de *coordinate descent* usado
  também pelo scikit-learn para ajustar Lasso e Elastic Net.
- HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. *The Elements of Statistical
  Learning*. 2. ed. New York: Springer, 2017.
- JAMES, G.; WITTEN, D.; HASTIE, T.; TIBSHIRANI, R. *Introduction to
  Statistical Learning*. New York: Springer, 2017.
- MEDEIROS, M. C. *Machine Learning Theory and Econometrics*. Lecture
  Notes, 2019.
