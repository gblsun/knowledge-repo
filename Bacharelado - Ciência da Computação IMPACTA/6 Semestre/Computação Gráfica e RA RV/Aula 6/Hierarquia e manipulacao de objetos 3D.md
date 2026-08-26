### Anotações 25/08

#### Modelagem 3D
- Mesmo formato das Aulas 4 e 5: um único modelo de **cubo unitário** (8 vértices, 12 arestas), desenhado em **wireframe** (`pygame.draw.line`).
- Dois cubos independentes na cena — `objeto` (o "pai") e `filho` — cada um com seu próprio dicionário de estado: `pos`, `rot` e `escala`. Não há parentesco real na transformação (o filho não herda a pose do pai); "pai"/"filho" aqui é só o nome dos dois objetos manipuláveis, e `TAB` alterna qual deles recebe os comandos de teclado.

#### Transformação e projeção
- `transformar()`: escala local → rotação (`rotacionar`) → translação, na mesma ordem das aulas anteriores.
- `rotacionar()`: rotação por eixo com trigonometria direta (X → Y → Z), sem matrizes.
- `projetar()`: câmera como ponto `[x, y, z]` móvel, projeção em perspectiva com `foco / z` (`foco = 520`) e recorte simplificado (`z` mínimo de `0.1`).

#### Controles
| Tecla | Ação |
|---|---|
| `TAB` | Alterna o objeto selecionado (pai ⇄ filho) |
| Setas | Move o objeto selecionado no plano XZ |
| `W` / `S` | Rotaciona o objeto selecionado no eixo X |
| `A` / `D` | Rotaciona o objeto selecionado no eixo Y |
| `Q` / `E` | Reduz / aumenta a escala do objeto selecionado |
| `I` / `K` | Move a câmera para cima / para baixo |
| `J` / `L` | Move a câmera lateralmente (esquerda / direita) |
| `R` | Reseta posição, rotação, escala e câmera |
| `ESC` | Sai do programa |

O objeto atualmente selecionado aparece destacado em cor viva (azul para o pai, laranja para o filho); o outro fica em tom apagado.

#### Correções feitas
- O arquivo original (`aula6.py`) não tinha nenhuma indentação nos blocos (`def`, `while`, `if`), o que impedia a execução.
- Duas atribuições (reset com a tecla `R`) estavam quebradas em várias linhas de forma inválida (vírgula solta fora de parênteses/colchetes) — reescritas como atribuições simples, uma por campo.
- O laço principal terminava no meio de um comentário: faltava o tratamento das teclas de câmera (`I/K/J/L`), o desenho dos dois cubos na tela, o texto de instruções e o `pygame.display.flip()` / encerramento (`pygame.quit()` + `sys.exit()`) — tudo isso foi completado.

#### Implementação
- `aula6-hierarquia-objetos.py` — cena interativa em **Pygame** com dois cubos selecionáveis (pai/filho), cada um com translação, rotação e escala independentes, mais câmera móvel.
