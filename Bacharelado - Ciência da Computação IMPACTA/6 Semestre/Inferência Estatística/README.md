# Inferência Estatística

Revisão de estatística univariada e bivariada aplicada com **Python** (numpy, pandas, scipy, seaborn): medidas de tendência central, dispersão e forma, organização de dados e testes de associação entre variáveis categóricas.

**Curso:** Bacharelado em Ciência da Computação — IMPACTA
**Semestre:** 6º | **Carga horária:** 80h

## Estrutura

- `Lista 1 - Estatística Univariada - Uma revisão/` — exercícios computacionais de simulação:
  - `Simulação de Média e Mediana.py` — compara o quanto média e mediana se deslocam com a inserção de um outlier
  - `Simulação de Dispersão.py` — coeficiente de variação (CV) de dois conjuntos com mesma média e desvios-padrão diferentes
  - `Simulação de Curtose.py` — curtose de Fisher de uma distribuição normal vs. uma com outliers propositais (mesocúrtica x leptocúrtica)
- `Lista 1 B - Organização de dados - Uma revisão/` — exercícios de organização de dados:
  - `geracao_amostra_normal.py` — geração de amostra aleatória com distribuição normal
- `Aula 4 - Estatística bivariada - Revisão/` — associação entre variáveis categóricas:
  - `Exemplo 2 - ataque cibersegurança.py` — teste qui-quadrado de independência (`scipy.stats.chi2_contingency`) relacionando tipo de ataque cibernético (Brute Force, SQL Injection, DDoS) e sistema operacional (Linux, Windows); inclui gráfico de barras das frequências observadas e heatmap dos resíduos (observado - esperado)
- `Aula 5 - Estimadores e estimação/` — estimação por intervalo de confiança:
  - `aula5 - Intervalo de confiança.ipynb` — cálculo do IC de 95% para a média (distribuição *t* de Student, via `scipy.stats.t.interval`) aplicado a um conjunto de tempos de resposta de uma API (ms), incluindo alguns outliers; reporta estimador pontual (média), erro padrão, limites do IC e margem de erro, com scatter plot da amostra + faixa do IC e histograma com KDE marcando média e limites
