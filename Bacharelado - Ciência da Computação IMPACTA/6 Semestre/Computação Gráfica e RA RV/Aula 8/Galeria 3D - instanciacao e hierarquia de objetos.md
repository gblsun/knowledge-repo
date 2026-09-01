### Anotações 01/09

#### Modelagem 3D
- Uma única malha reutilizável: **cubo unitário** (8 vértices, 6 faces, 12 arestas), com uma cor própria por face (`CORES_FACES`) para deixar visível a variação de cor por face pedida no enunciado.
- Quatro **instâncias** na galeria (`objetos`), lado a lado no eixo X, todas a partir da mesma malha, só variando posição/escala/rotação: cubo unitário, cubo ampliado (gira continuamente), uma "coluna" com escala só em Y e uma peça com **escala não uniforme** `(0.7, 1.8, 0.7)` (tarefa 6 do enunciado).
- `1`–`4` seleciona a peça da galeria (contorno amarelo ao redor da peça selecionada, calculado pela caixa 2D dos vértices projetados).

#### Objeto composto (hierarquia pai-filho)
- `corpo` é o pedestal (pai) e `placa` é a filha, ambos reaproveitando a mesma malha de cubo — a placa é só uma escala bem achatada `(1.35, 0.16, 1.35)` por cima do pedestal.
- `filho_de()` calcula a instância da filha a cada quadro: roda o deslocamento local (`FILHO_OFFSET`) pela rotação **atual** do pai e soma à posição dele, e soma a rotação local extra à rotação do pai — por isso a placa acompanha a posição/inclinação do pedestal e ainda gira em torno do próprio eixo Y sem se soltar dele (resposta direta à questão de reflexão 12).
- O pedestal balança devagar em X/Z (`sin(tempo)`), só para deixar visível que a filha realmente herda a rotação do pai (se o pai só girasse em Y com a filha centralizada acima dele, o deslocamento não mudaria e a herança passaria despercebida).
- Objeto composto fica no vão central da galeria (x = 0) e mais perto da câmera (z = -3), então não compete visualmente com as quatro peças numeradas.

#### Transformação e projeção
- `transformar()`: escala local → rotação (`rotacionar`) → translação, mesma ordem das Aulas 4-7.
- `rotacionar()`: rotação por eixo com trigonometria direta (X → Y → Z), sem matrizes — reaproveitada tanto para as instâncias quanto para a câmera.
- `projetar()`: câmera **orbital** (não translada como nas Aulas 6-7): gira o ponto do mundo pelos ângulos opostos de yaw/pitch e depois aplica a perspectiva `foco / z` (com `DISTANCIA_CAMERA = 9` e recorte em `z <= 0.2`).
- Modo arame (tarefa 3) implementado de fato: quando `modo_arame` é verdadeiro, `desenhar_objeto()` desenha só as 12 arestas (`pygame.draw.line`) e pula o preenchimento/ordenação de faces — diferente da Aula 7, que só trocava a cor de preenchimento por uma silhueta escura.

#### Controles
| Tecla | Ação |
|---|---|
| `1` – `4` | Seleciona a peça da galeria |
| Setas `←` / `→` | Gira a câmera (yaw) |
| Setas `↑` / `↓` | Inclina a câmera (pitch, limitado a ±1.3 rad) |
| `ESPAÇO` | Alterna entre modo sólido e modo arame |
| `ESC` / fechar janela | Encerra o programa |

#### Painel e textos
- Painel no canto superior esquerdo (tarefa 5) mostra o nome da peça selecionada e sua posição, escala e rotação atuais, atualizado a cada quadro.
- Barra de instruções na parte inferior, sobre uma "prateleira" retangular que dá noção de chão/vitrine para a galeria.

#### Questões para reflexão
1. **Reutilizar uma malha é mais eficiente** porque os dados geométricos (vértices/faces) ficam armazenados uma única vez; cada instância só guarda alguns números (posição, escala, rotação), o que economiza memória e permite mudar a peça toda (ex.: trocar o cubo por outra malha) em um único lugar.
2. **A profundidade `z`** define o quanto o ponto é "empurrado" para o fundo da cena antes da divisão perspectiva (`foco / z`); quanto maior o `z`, menor o ponto projetado. Quando `z` se aproxima de zero (ou fica negativo), o ponto está atrás/em cima da câmera e a divisão explode ou inverte a projeção — por isso `projetar()` descarta pontos com `z <= 0.2`.
3. Uma **escala não uniforme** (eixos com fatores diferentes) deforma o objeto quando ele também é rotacionado fora dos eixos principais: a escala é aplicada no espaço local antes da rotação, então girar um objeto "esticado" faz a deformação aparecer em uma direção que não é mais alinhada aos eixos originais, distorcendo a silhueta de forma pouco previsível.
4. Para a peça filha **girar em torno do próprio eixo sem abandonar o pai**: soma-se uma rotação extra só à rotação herdada do pai (`rot_local_extra`), mantendo o deslocamento (`offset_local`) fixo em relação ao pai — é exatamente o que `filho_de()` faz, girando `placa` em Y por conta própria enquanto ainda segue a posição/inclinação de `corpo`.
5. **Modelo da cena**: `VERTICES`, `FACES`, `ARESTAS`, os dicionários de instância (`objetos`, `corpo`, `placa`) e as funções `transformar`/`rotacionar`/`projetar`. **Interface/interação**: o laço de eventos (`KEYDOWN`), a leitura de `pygame.key.get_pressed()`, o painel de texto e a barra de instruções.
6. A seleção por **mouse** poderia comparar a posição do clique com a caixa 2D (bounding box) já calculada para o contorno de cada peça — a mesma lógica usada no destaque da peça selecionada, só que testando `pygame.mouse.get_pos()` contra cada `pygame.Rect` em vez de usar as teclas `1`–`4`.

#### Implementação
- `aula8-galeria-3d.py` — Galeria 3D em **Pygame**: quatro instâncias de cubo (uma girando continuamente), seleção por teclado com painel de transformações, câmera orbital, modo sólido/arame de verdade e um objeto composto (pedestal + placa) com hierarquia pai-filho.
