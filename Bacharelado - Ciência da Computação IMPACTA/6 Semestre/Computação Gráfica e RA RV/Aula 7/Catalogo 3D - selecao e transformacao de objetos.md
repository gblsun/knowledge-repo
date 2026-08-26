### Anotações 25/08

#### Modelagem 3D
- Duas malhas reutilizáveis: **cubo unitário** (8 vértices, 6 faces) e **pirâmide** de base quadrada (5 vértices, 5 faces), cada uma como uma lista de vértices e uma lista de faces (índices dos vértices, em ordem).
- Quatro **instâncias** no catálogo (`objetos`), reaproveitando as duas malhas com posição, rotação, escala e cor próprias — diferente das Aulas 4-6, aqui as faces são **preenchidas** (`pygame.draw.polygon`) em vez de desenhadas só em wireframe.
- `TAB` alterna qual objeto está selecionado; o selecionado ganha um retângulo amarelo de destaque ao redor (bounding box 2D dos vértices projetados).

#### Transformação e projeção
- `transformar()`: escala local → rotação (`rotacionar`) → translação, mesma ordem das aulas anteriores.
- `rotacionar()`: rotação por eixo com trigonometria direta (X → Y → Z), sem matrizes.
- `projetar()`: câmera como ponto `[x, y, z]` móvel, projeção em perspectiva com `foco / z` (`foco = 560`) e recorte simplificado (`z` mínimo de `0.2`).
- `desenhar_grade()`: chão em grade, só para dar noção de profundidade/escala.

#### Controles
| Tecla | Ação |
|---|---|
| `TAB` | Alterna o objeto selecionado |
| `SPACE` | Alterna modo "arame" (preenchimento escuro, silhueta) |
| Setas | Move o objeto selecionado no plano XZ |
| `W` / `S` | Rotaciona o objeto selecionado no eixo X |
| `A` / `D` | Rotaciona o objeto selecionado no eixo Y |
| `Q` / `E` | Reduz / aumenta a escala do objeto selecionado |
| `I` / `K` | Move a câmera para cima / para baixo |
| `J` / `L` | Move a câmera lateralmente (esquerda / direita) |
| `R` | Restaura a câmera e volta a seleção para o primeiro objeto |

#### Correções feitas
- O arquivo original (`aula7.py`) não tinha nenhuma indentação em nenhum bloco (`def`, `while`, `for`, `if`), o que impedia a execução — reescrito com a indentação correta em todas as funções e no laço principal.
- `projetar()` usava um traço "–" (travessão/en dash) no lugar do operador de subtração `-` (`ALTURA/2 – foco*y/z`), o que é um erro de sintaxe em Python — corrigido para `ALTURA / 2 - foco * y / z`.
- As strings de instrução (`info`/`info2`) estavam quebradas no meio por uma quebra de linha literal dentro de uma string comum (sem aspas triplas), outro erro de sintaxe — reescritas como uma única linha (com parênteses para continuação, quando necessário).
- Adicionado `sys.exit()` após `pygame.quit()` para encerrar o processo de forma limpa.

#### Implementação
- `aula7-catalogo-3d.py` — mini catálogo 3D em **Pygame** com quatro objetos (cubos e pirâmides) de faces preenchidas, seleção por `TAB`, transformação independente (posição/rotação/escala) do objeto selecionado, alternância de modo de preenchimento e câmera móvel.
