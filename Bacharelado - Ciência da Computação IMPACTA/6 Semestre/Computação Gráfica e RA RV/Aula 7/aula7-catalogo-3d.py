#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 07 — EXERCÍCIO PRÁTICO — AULA 7         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  25 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝

Mini catálogo 3D: quatro objetos (cubos e pirâmides) com faces
preenchidas, selecionáveis por teclado, cada um com sua própria
translação, rotação e escala, mais uma câmera móvel.
"""

import math
import sys
import pygame

pygame.init()

LARGURA, ALTURA = 1100, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini catálogo 3D - Aula 7")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 18)

# Cada malha é uma lista de vértices e uma lista de faces (índices de
# vértices, em ordem, formando cada polígono). A mesma malha pode ser
# reutilizada por várias instâncias (objetos), cada uma com seu próprio
# pos/rot/escala.
CUBO = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
]
FACES_CUBO = [
    (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
    (3, 2, 6, 7), (1, 5, 6, 2), (0, 3, 7, 4),
]

PIRAMIDE = [
    (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (0, 1, 0),
]
FACES_PIRAMIDE = [
    (0, 1, 2, 3), (0, 4, 1), (1, 4, 2), (2, 4, 3), (3, 4, 0),
]

malhas = {
    "cubo": {"vertices": CUBO, "faces": FACES_CUBO},
    "piramide": {"vertices": PIRAMIDE, "faces": FACES_PIRAMIDE},
}


def rotacionar(p, rot):
    """Aplica rotações sucessivas nos eixos X, Y e Z (sem matrizes)."""
    x, y, z = p
    rx, ry, rz = rot
    c, s = math.cos(rx), math.sin(rx)
    y, z = y * c - z * s, y * s + z * c
    c, s = math.cos(ry), math.sin(ry)
    x, z = x * c + z * s, -x * s + z * c
    c, s = math.cos(rz), math.sin(rz)
    x, y = x * c - y * s, x * s + y * c
    return x, y, z


def transformar(p, instancia):
    """Escala local, rotação e translação de um vértice para o mundo."""
    escala = instancia["escala"]
    pos = instancia["pos"]
    p = (p[0] * escala[0], p[1] * escala[1], p[2] * escala[2])
    p = rotacionar(p, instancia["rot"])
    return (p[0] + pos[0], p[1] + pos[1], p[2] + pos[2])


def projetar(p, camera, foco=560):
    """Projeta um ponto do mundo na tela (perspectiva simples, foco/z)."""
    x, y, z = p
    x -= camera[0]
    y -= camera[1]
    z -= camera[2]
    if z <= 0.2:
        return None  # ponto atrás (ou muito perto) da câmera: não desenha
    return (int(LARGURA / 2 + foco * x / z), int(ALTURA / 2 - foco * y / z))


def desenhar_grade(superficie, camera):
    """Desenha um chão em grade, para dar noção de profundidade e escala."""
    for i in range(-8, 9):
        a = projetar((i, -2, 2), camera)
        b = projetar((i, -2, 16), camera)
        c = projetar((-8, -2, i + 10), camera)
        d = projetar((8, -2, i + 10), camera)
        if a and b:
            pygame.draw.line(superficie, (55, 65, 80), a, b, 1)
        if c and d:
            pygame.draw.line(superficie, (55, 65, 80), c, d, 1)


def desenhar_malha(superficie, malha, instancia, camera, cor, selecionado=False):
    """Transforma, projeta e desenha (preenchida) cada face de uma malha.

    Se `selecionado` for True, também desenha um retângulo de destaque
    (bounding box em 2D dos vértices projetados) ao redor do objeto.
    """
    pontos3d = [transformar(v, instancia) for v in malha["vertices"]]
    pontos2d = [projetar(v, camera) for v in pontos3d]
    for face in malha["faces"]:
        pontos = [pontos2d[i] for i in face]
        if all(pontos):
            pygame.draw.polygon(superficie, cor, pontos)
            pygame.draw.polygon(superficie, (230, 235, 242), pontos, 1)
    if selecionado:
        validos = [p for p in pontos2d if p]
        if validos:
            xs = [p[0] for p in validos]
            ys = [p[1] for p in validos]
            ret = pygame.Rect(min(xs) - 6, min(ys) - 6,
                               max(xs) - min(xs) + 12, max(ys) - min(ys) + 12)
            pygame.draw.rect(superficie, (255, 235, 80), ret, 2)


def nova_instancia(tipo, pos, escala, rot=(0, 0, 0), cor=(80, 170, 245)):
    """Cria um objeto (instância) de uma das malhas do catálogo."""
    return {"tipo": tipo, "pos": list(pos), "escala": list(escala),
            "rot": list(rot), "cor": cor}


# Catálogo: quatro instâncias reaproveitando só duas malhas (cubo/pirâmide).
objetos = [
    nova_instancia("cubo", (-3, 0, 8), (1.4, 1.4, 1.4), cor=(65, 155, 235)),
    nova_instancia("piramide", (0, 0, 9), (1.5, 1.5, 1.5), cor=(245, 165, 65)),
    nova_instancia("cubo", (3, 0, 11), (1.0, 2.0, 1.0), rot=(0.2, 0.4, 0), cor=(110, 215, 150)),
    nova_instancia("piramide", (0, 2.7, 10), (0.7, 0.7, 0.7), cor=(220, 105, 205)),
]

camera = [0, 1, 0]
selecionado = 0
modo_arame = False
rodando = True

while rodando:
    dt = relogio.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                selecionado = (selecionado + 1) % len(objetos)
            if evento.key == pygame.K_SPACE:
                modo_arame = not modo_arame
            if evento.key == pygame.K_r:
                camera = [0, 1, 0]
                selecionado = 0

    teclas = pygame.key.get_pressed()
    alvo = objetos[selecionado]
    v = 3 * dt

    # Setas: translação do objeto selecionado no plano XZ.
    if teclas[pygame.K_LEFT]:
        alvo["pos"][0] -= v
    if teclas[pygame.K_RIGHT]:
        alvo["pos"][0] += v
    if teclas[pygame.K_UP]:
        alvo["pos"][2] -= v
    if teclas[pygame.K_DOWN]:
        alvo["pos"][2] += v

    # A/D: rotação em Y; W/S: rotação em X.
    if teclas[pygame.K_a]:
        alvo["rot"][1] -= 1.8 * dt
    if teclas[pygame.K_d]:
        alvo["rot"][1] += 1.8 * dt
    if teclas[pygame.K_w]:
        alvo["rot"][0] -= 1.8 * dt
    if teclas[pygame.K_s]:
        alvo["rot"][0] += 1.8 * dt

    # Q/E: escala uniforme (mínimo de 0.2 para não colapsar/inverter o objeto).
    if teclas[pygame.K_q]:
        alvo["escala"] = [max(0.2, x - 1.2 * dt) for x in alvo["escala"]]
    if teclas[pygame.K_e]:
        alvo["escala"] = [x + 1.2 * dt for x in alvo["escala"]]

    # J/L e I/K: movimento da câmera nos eixos X e Y.
    if teclas[pygame.K_j]:
        camera[0] -= v
    if teclas[pygame.K_l]:
        camera[0] += v
    if teclas[pygame.K_i]:
        camera[1] += v
    if teclas[pygame.K_k]:
        camera[1] -= v

    tela.fill((15, 20, 30))
    desenhar_grade(tela, camera)

    for i, objeto in enumerate(objetos):
        malha = malhas[objeto["tipo"]]
        if not modo_arame:
            desenhar_malha(tela, malha, objeto, camera, objeto["cor"], i == selecionado)
        else:
            # Modo "arame": para simplificar, usa a mesma função de desenho
            # preenchido, mas com uma cor escura no lugar da cor do objeto
            # (silhueta), destacando o contorno claro das arestas.
            desenhar_malha(tela, malha, objeto, camera, (25, 35, 50), i == selecionado)

    info1 = (f"Objeto {selecionado + 1}/{len(objetos)}: {alvo['tipo']} | "
             f"TAB seleciona | SPACE arame")
    info2 = "Setas move | A/D e W/S gira | Q/E escala | J/L e I/K câmera | R restaura"
    tela.blit(fonte.render(info1, True, (240, 240, 245)), (20, 20))
    tela.blit(fonte.render(info2, True, (190, 205, 220)), (20, 48))

    pygame.display.flip()

pygame.quit()
sys.exit()
