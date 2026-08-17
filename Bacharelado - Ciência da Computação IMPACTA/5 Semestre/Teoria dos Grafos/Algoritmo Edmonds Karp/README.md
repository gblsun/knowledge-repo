# Algoritmo de Edmonds-Karp para Fluxo Maximo

## Sobre o Projeto

Implementacao do algoritmo de Edmonds-Karp para resolver o problema de fluxo
maximo em redes. O projeto inclui visualizacao grafica do grafo e animacao
passo a passo da execucao do algoritmo, desenvolvido em Python com Jupyter
Notebook.

O algoritmo de Edmonds-Karp e uma variacao do metodo de Ford-Fulkerson que
utiliza busca em largura (BFS) para encontrar caminhos aumentantes, garantindo
complexidade O(V * E^2).

---

## Grafo Utilizado

O grafo possui 6 vertices e 8 arestas dirigidas:

Vertices: S (origem), 1, 2, 3, 4, T (destino)     
     
Arestas:     
S -> 1  : capacidade 10     
S -> 2  : capacidade 10     
1 -> 2  : capacidade  2     
1 -> 3  : capacidade  4     
1 -> 4  : capacidade  8     
2 -> 4  : capacidade  9     
4 -> 3  : capacidade  6     
3 -> T  : capacidade 10     
4 -> T  : capacidade 10     

Matriz de capacidades:    

     S   1   2   3   4   T     
S [  0, 10, 10,  0,  0,  0 ]     
1 [  0,  0,  2,  4,  8,  0 ]     
2 [  0,  0,  0,  0,  9,  0 ]     
3 [  0,  0,  0,  0,  0, 10 ]     
4 [  0,  0,  0,  6,  0, 10 ]     
T [  0,  0,  0,  0,  0,  0 ]     

---

## Resultados

Fluxo maximo encontrado: **19**

Caminhos aumentantes identificados:

| Iteracao | Caminho               | Gargalo | Fluxo Acumulado |
|----------|-----------------------|---------|-----------------|
| 1        | S -> 1 -> 3 -> T      | 4       | 4               |
| 2        | S -> 1 -> 4 -> T      | 6       | 10              |
| 3        | S -> 2 -> 4 -> T      | 4       | 14              |
| 4        | S -> 2 -> 4 -> 3 -> T | 5       | 19              |

Fluxo final nas arestas:

| Aresta | Fluxo | Capacidade |
|--------|-------|------------|
| S -> 1 | 10    | 10         |
| S -> 2 | 9     | 10         |
| 1 -> 2 | 0     | 2          |
| 1 -> 3 | 4     | 4          |
| 1 -> 4 | 6     | 8          |
| 2 -> 4 | 9     | 9          |
| 4 -> 3 | 5     | 6          |
| 3 -> T | 9     | 10         |
| 4 -> T | 10    | 10         |

---

## Estrutura do Notebook

| Celula | Conteudo                                            |      
|--------|-----------------------------------------------------|      
| 1      | Importacoes                                         |      
| 2      | Busca em largura (BFS)                              |      
| 3      | Algoritmo de Edmonds-Karp                           |      
| 4      | Definicao do grafo e posicoes                       |      
| 5      | Funcao de plotagem                                  |      
| 6      | Visualizacao do grafo original                      |      
| 7      | Execucao do algoritmo                               |      
| 8      | Animacao passo a passo                              |      
| 9      | Resultado final                                     |      
      
---

## Requisitos

Python >= 3.7     
networkx     
matplotlib     
ipython     

#### Instalação:

```bash
pip install networkx matplotlib ipython
```

### Como Executar
Abrir o notebook em Jupyter ou Google Colab.      
Executar as celulas em ordem.      
A celula 6 exibe o grafo original.      
A celula 8 apresenta a animacao do algoritmo.      
A celula 9 exibe o resultado final.      
