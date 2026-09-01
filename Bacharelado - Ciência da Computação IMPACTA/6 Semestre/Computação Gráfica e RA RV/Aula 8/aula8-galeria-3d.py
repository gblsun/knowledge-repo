"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 08 — EXERCÍCIO PRÁTICO — AULA 8         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  01 de Setembro de 2026                                       ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝

Galeria 3D: quatro instâncias de um cubo unitário — mesma malha,
posição/escala/rotação próprias, uma delas girando continuamente —
mais um objeto composto (pedestal + placa filha) que demonstra
hierarquia pai-filho: a placa herda posição e rotação do pedestal e
ainda gira em torno do próprio eixo. Seleção por teclas 1-4, câmera
orbital pelas setas e alternância sólido/arame pelo ESPAÇO.
"""

import math
import sys
import pygame

pygame.init()

LARGURA, ALTURA = 1000, 650
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Galeria 3D - Aula 8")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 18)
fonte_painel = pygame.font.SysFont("arial", 16)

# Malha reutilizável: cubo unitário (8 vértices, 6 faces, 12 arestas).
# A mesma malha é instanciada para as quatro peças da galeria e também
# para o corpo e a placa do objeto composto — só posição, escala e
# rotação mudam entre elas.
VERTICES = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
]
FACES = [
    (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
    (3, 2, 6, 7), (1, 5, 6, 2), (0, 3, 7, 4),
]
ARESTAS = [
    (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]
CORES_FACES = [
    (225, 90, 90), (90, 165, 235), (95, 195, 130),
    (235, 185, 75), (175, 105, 215), (90, 205, 205),
]
COR_ARESTA = (225, 230, 240)

DISTANCIA_CAMERA = 9
FOCO = 520


def rotacionar(ponto, rot):
    """Aplica rotações sucessivas nos eixos X, Y e Z (sem matrizes)."""
    x, y, z = ponto
    rx, ry, rz = rot
    c, s = math.cos(rx), math.sin(rx)
    y, z = y * c - z * s, y * s + z * c
    c, s = math.cos(ry), math.sin(ry)
    x, z = x * c + z * s, -x * s + z * c
    c, s = math.cos(rz), math.sin(rz)
    x, y = x * c - y * s, x * s + y * c
    return x, y, z


def transformar(ponto, instancia):
    """Escala local, rotação e translação de um vértice para o mundo."""
    escala = instancia["escala"]
    pos = instancia["pos"]
    p = (ponto[0] * escala[0], ponto[1] * escala[1], ponto[2] * escala[2])
    p = rotacionar(p, instancia["rot"])
    return (p[0] + pos[0], p[1] + pos[1], p[2] + pos[2])


def projetar(ponto, camera_yaw, camera_pitch):
    """Câmera orbital: gira a cena pelos ângulos opostos de yaw/pitch e
    projeta em perspectiva (foco / z). Reaproveita `rotacionar` para a
    rotação da câmera, com o mesmo mecanismo usado nos objetos."""
    x, y, z = rotacionar(ponto, (-camera_pitch, -camera_yaw, 0))
    z += DISTANCIA_CAMERA
    if z <= 0.2:
        return None
    return (int(LARGURA / 2 + FOCO * x / z), int(ALTURA / 2 - FOCO * y / z), z)


def desenhar_objeto(instancia, camera_yaw, camera_pitch, cores_faces, arame, selecionado=False):
    """Transforma, projeta e desenha uma instância — sólida (faces
    preenchidas, ordenadas por profundidade) ou em arame (só arestas)."""
    pontos = [projetar(transformar(v, instancia), camera_yaw, camera_pitch) for v in VERTICES]
    if any(p is None for p in pontos):
        return
    if arame:
        for a, b in ARESTAS:
            pygame.draw.line(tela, COR_ARESTA, pontos[a][:2], pontos[b][:2], 2)
    else:
        ordem = sorted(range(len(FACES)), key=lambda f: sum(pontos[i][2] for i in FACES[f]), reverse=True)
        for f in ordem:
            poligono = [pontos[i][:2] for i in FACES[f]]
            pygame.draw.polygon(tela, cores_faces[f], poligono)
            pygame.draw.polygon(tela, (25, 30, 42), poligono, 1)
    if selecionado:
        xs = [p[0] for p in pontos]
        ys = [p[1] for p in pontos]
        contorno = pygame.Rect(min(xs) - 8, min(ys) - 8, max(xs) - min(xs) + 16, max(ys) - min(ys) + 16)
        pygame.draw.rect(tela, (255, 225, 70), contorno, 2)


def cor_solida(cor):
    """Repete uma única cor nas seis faces — usado nas peças do objeto
    composto, para diferenciá-las visualmente da galeria multicolorida."""
    return [cor] * 6


def filho_de(pai, offset_local, escala_local, rot_local_extra):
    """Calcula a instância mundial de uma peça filha a partir do pai.

    A filha herda a posição e a rotação do pai (o deslocamento local é
    rotacionado junto com o pai) e ainda soma sua própria rotação local
    — por isso ela gira em torno do próprio eixo sem se soltar dele.
    """
    deslocamento = rotacionar(offset_local, pai["rot"])
    pos = tuple(p + d for p, d in zip(pai["pos"], deslocamento))
    rot = tuple(r + e for r, e in zip(pai["rot"], rot_local_extra))
    return {"pos": pos, "escala": escala_local, "rot": rot}


# Galeria: quatro instâncias da mesma malha de cubo, lado a lado, com
# posição/escala próprias (task 6: a 4ª peça tem escala não uniforme).
objetos = [
    {"pos": [-4.5, 0, 0], "escala": [1, 1, 1], "rot": [0, 0, 0], "nome": "Cubo unitário"},
    {"pos": [-1.5, 0, 0], "escala": [1.4, 1.4, 1.4], "rot": [0, 0, 0], "nome": "Cubo ampliado (gira)"},
    {"pos": [1.5, 0, 0], "escala": [1, 2, 1], "rot": [0, 0, 0], "nome": "Coluna (escala em Y)"},
    {"pos": [4.5, 0.55, 0], "escala": [0.7, 1.8, 0.7], "rot": [0, 0, 0], "nome": "Escultura (escala não uniforme)"},
]

# Objeto composto: pedestal (corpo/pai) + placa (filha), no vão central
# da galeria e mais perto da câmera — demonstra hierarquia pai-filho
# reaproveitando a mesma malha de cubo.
corpo = {"pos": [0, -1.7, -3], "escala": [0.55, 1.1, 0.55], "rot": [0, 0, 0]}
FILHO_OFFSET = (0, 1.5, 0)
FILHO_ESCALA = (1.35, 0.16, 1.35)
rot_local_filho = 0.0

camera_yaw = 0.0
camera_pitch = 0.0
tempo = 0.0
selecionado = 1
modo_arame = False
rodando = True

while rodando:
    dt = relogio.tick(60) / 1000
    tempo += dt

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
            elif evento.key == pygame.K_SPACE:
                modo_arame = not modo_arame
            elif evento.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4):
                selecionado = evento.key - pygame.K_1

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        camera_yaw -= 1.2 * dt
    if teclas[pygame.K_RIGHT]:
        camera_yaw += 1.2 * dt
    if teclas[pygame.K_UP]:
        camera_pitch = min(1.3, camera_pitch + 1.0 * dt)
    if teclas[pygame.K_DOWN]:
        camera_pitch = max(-1.3, camera_pitch - 1.0 * dt)

    # A segunda peça da galeria gira continuamente em torno de Y.
    objetos[1]["rot"][1] += 0.9 * dt

    # O pedestal balança suavemente em X/Z (o pai); a placa herda essa
    # inclinação e ainda gira mais rápido em torno do próprio eixo Y
    # (rotação local somada à do pai, sem se soltar dele).
    corpo["rot"][0] = 0.16 * math.sin(tempo * 0.7)
    corpo["rot"][2] = 0.10 * math.sin(tempo * 0.5 + 1.0)
    rot_local_filho += 1.6 * dt
    placa = filho_de(corpo, FILHO_OFFSET, FILHO_ESCALA, (0, rot_local_filho, 0))

    tela.fill((16, 21, 32))
    pygame.draw.rect(tela, (36, 45, 62), (60, 470, 880, 70))

    for i, obj in enumerate(objetos):
        desenhar_objeto(obj, camera_yaw, camera_pitch, CORES_FACES, modo_arame, i == selecionado)
    desenhar_objeto(corpo, camera_yaw, camera_pitch, cor_solida((120, 140, 168)), modo_arame)
    desenhar_objeto(placa, camera_yaw, camera_pitch, cor_solida((230, 190, 90)), modo_arame)

    alvo = objetos[selecionado]
    painel = [
        f"Peça selecionada: {alvo['nome']} (tecla {selecionado + 1})",
        f"Posição: ({alvo['pos'][0]:.1f}, {alvo['pos'][1]:.1f}, {alvo['pos'][2]:.1f})",
        f"Escala: ({alvo['escala'][0]:.2f}, {alvo['escala'][1]:.2f}, {alvo['escala'][2]:.2f})",
        f"Rotação (rad): ({alvo['rot'][0]:.2f}, {alvo['rot'][1]:.2f}, {alvo['rot'][2]:.2f})",
    ]
    for i, linha in enumerate(painel):
        tela.blit(fonte_painel.render(linha, True, (225, 230, 238)), (20, 20 + i * 22))

    info = "Galeria 3D | 1-4 seleciona peça | Setas: câmera | ESPAÇO: sólido/arame | ESC: sair"
    tela.blit(fonte.render(info, True, (235, 235, 235)), (60, 615))

    pygame.display.flip()

pygame.quit()
sys.exit()
