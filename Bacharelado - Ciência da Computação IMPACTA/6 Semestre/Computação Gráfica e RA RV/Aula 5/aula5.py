"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 05 — EXERCÍCIO PRÁTICO — AULA 5         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  18 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝
"""

import math
import sys
import pygame

pygame.init()

LARGURA, ALTURA = 1000, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini ambiente virtual - Aula 5")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 22)

# Cada objeto é uma lista de vértices e arestas em coordenadas locais.
CUBO = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
ARESTAS_CUBO = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
                (0, 4), (1, 5), (2, 6), (3, 7)]

PIRAMIDE = [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (0, 1, 0)]
ARESTAS_PIRAMIDE = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4)]


def rotacionar(ponto, angulo_x, angulo_y, angulo_z):
    """Aplica rotações lineares sucessivas nos eixos X, Y e Z."""
    x, y, z = ponto
    cx, sx = math.cos(angulo_x), math.sin(angulo_x)
    y, z = y * cx - z * sx, y * sx + z * cx
    cy, sy = math.cos(angulo_y), math.sin(angulo_y)
    x, z = x * cy + z * sy, -x * sy + z * cy
    cz, sz = math.cos(angulo_z), math.sin(angulo_z)
    x, y = x * cz - y * sz, x * sz + y * cz
    return (x, y, z)


def transformar(ponto, posicao, rotacao, escala):
    """Modelo: escala, rotação e translação no mundo."""
    escalado = tuple(c * escala for c in ponto)
    girado = rotacionar(escalado, *rotacao)
    return tuple(g + t for g, t in zip(girado, posicao))


def projetar(ponto, camera, perspectiva=True):
    """Converte coordenadas do mundo em coordenadas da janela."""
    x, y, z = (ponto[i] - camera[i] for i in range(3))
    z = max(z, 0.15)  # plano de recorte simplificado, evita divisão por zero/negativo
    fator = 420 / z if perspectiva else 170
    return (int(LARGURA / 2 + x * fator), int(ALTURA / 2 - y * fator))


def desenhar_objeto(objeto, arestas, configuracao, camera, perspectiva):
    """Transforma, projeta e desenha (em wireframe) um objeto na tela."""
    pontos_2d = []
    for vertice in objeto:
        mundo = transformar(vertice, configuracao["posicao"],
                             configuracao["rotacao"], configuracao["escala"])
        pontos_2d.append(projetar(mundo, camera, perspectiva))
    for a, b in arestas:
        pygame.draw.line(tela, configuracao["cor"], pontos_2d[a], pontos_2d[b], 3)


objetos = [
    {"modelo": CUBO, "arestas": ARESTAS_CUBO, "posicao": (-2, 0, 7),
     "rotacao": (0, 0, 0), "escala": 1.2, "cor": (70, 190, 255)},
    {"modelo": PIRAMIDE, "arestas": ARESTAS_PIRAMIDE, "posicao": (2, 0, 8),
     "rotacao": (0, 0, 0), "escala": 1.5, "cor": (255, 170, 70)},
]

camera = [0, 0, 0]
perspectiva = True
executando = True

while executando:
    dt = relogio.tick(60) / 1000

    # Eventos "de disparo único" (um clique de tecla, não segurar).
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
            elif evento.key == pygame.K_p:
                perspectiva = not perspectiva
            elif evento.key == pygame.K_r:
                camera[:] = [0, 0, 0]
                for obj in objetos:
                    obj["rotacao"] = (0, 0, 0)

    # Teclas contínuas: verificadas a cada quadro enquanto estiverem pressionadas.
    teclas = pygame.key.get_pressed()
    velocidade = 3 * dt
    if teclas[pygame.K_LEFT]:
        camera[0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        camera[0] += velocidade
    if teclas[pygame.K_UP]:
        camera[1] += velocidade
    if teclas[pygame.K_DOWN]:
        camera[1] -= velocidade
    if teclas[pygame.K_w]:
        camera[2] += velocidade
    if teclas[pygame.K_s]:
        camera[2] -= velocidade
    if teclas[pygame.K_a]:
        rx, ry, rz = objetos[0]["rotacao"]
        objetos[0]["rotacao"] = (rx, ry + velocidade, rz)
    if teclas[pygame.K_d]:
        rx, ry, rz = objetos[1]["rotacao"]
        objetos[1]["rotacao"] = (rx, ry - velocidade, rz)

    tela.fill((18, 24, 38))

    for obj in objetos:
        desenhar_objeto(obj["modelo"], obj["arestas"], obj, camera, perspectiva)

    modo = "perspectiva" if perspectiva else "ortografica"
    texto = fonte.render(f"Projecao: {modo} | P: alternar | R: reiniciar", True,
                          (235, 235, 235))
    instrucoes = fonte.render("Setas/W/S: camera | A/D: rotacionar objetos | ESC: sair",
                               True, (190, 205, 220))
    tela.blit(texto, (24, 22))
    tela.blit(instrucoes, (24, 52))

    pygame.display.flip()

pygame.quit()
sys.exit()
