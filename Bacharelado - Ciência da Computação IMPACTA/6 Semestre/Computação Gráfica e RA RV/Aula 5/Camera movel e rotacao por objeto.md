### Anotações 18/08

#### Modelagem 3D
- Reaproveita o mesmo formato da Aula 4: cada objeto é uma lista de **vértices** (pontos no espaço) mais uma lista de **arestas** (pares de índices), desenhado em **wireframe** (`pygame.draw.line`), sem preenchimento de faces.
- Exemplos: **cubo** (8 vértices, 12 arestas) e **pirâmide** (5 vértices, 8 arestas).

#### Rotação por eixo (sem matrizes)
- Diferente da Aula 4 (que usa matrizes 4×4 homogêneas), aqui a rotação é aplicada diretamente com trigonometria, um eixo por vez, em `rotacionar()`:
  1. Rotação em X — combina `y` e `z` usando $\cos(\theta_x)$/$\sin(\theta_x)$.
  2. Rotação em Y — combina `x` e `z` (já rotacionados) usando $\cos(\theta_y)$/$\sin(\theta_y)$.
  3. Rotação em Z — combina `x` e `y` (já rotacionados) usando $\cos(\theta_z)$/$\sin(\theta_z)$.
- Como cada rotação usa o resultado da anterior, o efeito final equivale à multiplicação das três matrizes de rotação na ordem X → Y → Z.

#### Transformação de modelo
- `transformar()` aplica, na ordem: **escala** (multiplica cada coordenada local) → **rotação** (`rotacionar`) → **translação** (soma a posição do objeto no mundo).

#### Câmera e projeção
- A câmera é um ponto `[x, y, z]` móvel (só translação, sem rotação/mira).
- `projetar()` subtrai a posição da câmera do ponto do mundo e limita `z` a no mínimo `0.15` como plano de recorte simplificado (evita divisão por zero/negativo ao projetar pontos atrás ou muito perto da câmera).
- **Perspectiva**: fator de projeção `420 / z` — quanto mais longe (maior `z`), menor o objeto na tela.
- **Ortográfica**: fator fixo `170`, sem efeito de profundidade.
- O eixo Y é invertido na conversão para tela (`ALTURA/2 - y*fator`), pois em Pygame a coordenada de tela cresce para baixo enquanto o mundo usa Y crescendo para cima.

#### Controles
| Tecla | Ação |
|---|---|
| Setas | Move a câmera nos eixos X/Y |
| `W` / `S` | Move a câmera no eixo Z (aproxima/afasta) |
| `A` | Rotaciona o cubo em Y |
| `D` | Rotaciona a pirâmide em Y (sentido oposto) |
| `P` | Alterna projeção perspectiva ⇄ ortográfica |
| `R` | Reseta câmera e rotações dos objetos |
| `ESC` | Sai do programa |

#### Correções feitas
- O arquivo original tinha texto de cabeçalho/rodapé de PDF (`Exercício prático • Página 3/4`, `Computação Gráfica • Aula 5`) colado no meio do código, quebrando a sintaxe.
- Toda a indentação dos blocos (`def`, `while`, `for`, `if`) havia sido perdida na cópia, o que também impedia a execução.
- Duas linhas com quebras de linha inválidas dentro de expressões (`objetos[0]["rotacao"]\n[1]+velocidade`) foram reescritas de forma legível.

#### Implementação
- `aula5.py` — cena interativa em **Pygame** com cubo e pirâmide, câmera móvel e rotação independente por objeto via teclado.
