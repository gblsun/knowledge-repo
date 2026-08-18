### Anotações 18/08

#### Modelagem 3D
- Objetos são representados por uma lista de **vértices** (pontos no espaço) e uma lista de **faces** (índices dos vértices que formam cada polígono).
- Exemplos implementados: **cubo** (8 vértices, 6 faces) e **pirâmide** (5 vértices, 5 faces).

#### Coordenadas homogêneas
- Pontos 3D $(x, y, z)$ são representados como vetores $(x, y, z, 1)$ para permitir que translação, rotação e escala sejam combinadas em uma única matriz $4\times4$.
- A divisão final pela componente $w$ normaliza o ponto de volta ao espaço 3D.

#### Matrizes de transformação
- **Translação**: desloca a origem, preenchendo a última coluna da matriz identidade com $(t_x, t_y, t_z)$.
- **Escala**: multiplica cada eixo por um fator $(s_x, s_y, s_z)$ na diagonal principal.
- **Rotação**: uma matriz por eixo ($R_x$, $R_y$, $R_z$), construída com $\cos\theta$ e $\sin\theta$ nas posições correspondentes ao plano de rotação.
- **Composição**: transformações são combinadas por multiplicação de matrizes. A ordem importa — no código: escala → rotação → translação, aplicada da direita para a esquerda ($M = T \cdot R \cdot S$).

#### Câmera e projeção
- A câmera fica fixa em $z = \text{camera\_z}$, olhando para $+Z$; pontos com `z_view <= 0.1` são descartados (atrás ou muito próximos da câmera).
- **Projeção perspectiva**: divide $x$ e $y$ pela distância à câmera (`z_view`), escalados por uma distância focal — objetos mais distantes aparecem menores.
- **Projeção ortográfica**: aplica um fator de escala fixo, sem levar em conta a profundidade — não há efeito de perspectiva.
- Alternância entre os dois modos de projeção é feita em tempo real (tecla `P`).

#### Implementação
- `aula4-cubo-triangulo.py` — cena interativa em **Pygame** com um cubo e uma pirâmide, controlados por teclado (rotação nos três eixos e zoom da câmera).
- `cubo e triangulo.png` — captura da cena renderizada.
