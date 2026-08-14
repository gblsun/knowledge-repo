"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 03 — EXERCÍCIO PRÁTICO — AULA 3         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  11 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝
"""

import math
import pygame

# -----------------------------
# Configuracao da janela
# -----------------------------
WIDTH, HEIGHT = 800, 600
BACKGROUND = (18, 24, 38)
CUBE_COLOR = (80, 190, 255)
TEXT_COLOR = (235, 240, 248)

# Vertices do cubo no espaco 3D
VERTICES = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
]

# Cada tupla conecta dois vertices e forma uma aresta
EDGES = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
]


def rotate_x(point, angle):
    x, y, z = point
    c, s = math.cos(angle), math.sin(angle)
    return (x, y * c - z * s, y * s + z * c)


def rotate_y(point, angle):
    x, y, z = point
    c, s = math.cos(angle), math.sin(angle)
    return (x * c + z * s, y, -x * s + z * c)


def rotate_z(point, angle):
    x, y, z = point
    c, s = math.cos(angle), math.sin(angle)
    return (x * c - y * s, x * s + y * c, z)


def transform(point, angles):
    """Aplica rotacoes no modelo, na ordem X -> Y -> Z."""
    point = rotate_x(point, angles[0])
    point = rotate_y(point, angles[1])
    point = rotate_z(point, angles[2])
    return point


def project_perspective(point, focal_length, camera_z):
    """Projeta 3D em 2D; retorna None se o ponto estiver atras da camera."""
    x, y, z = point
    z_camera = z + camera_z
    if z_camera <= 0.1:
        return None
    scale = focal_length / z_camera
    screen_x = WIDTH / 2 + x * scale
    screen_y = HEIGHT / 2 - y * scale
    return (round(screen_x), round(screen_y))


def project_orthographic(point, scale):
    """Na ortografica, a profundidade nao altera o tamanho aparente."""
    x, y, _ = point
    screen_x = WIDTH / 2 + x * scale
    screen_y = HEIGHT / 2 - y * scale
    return (round(screen_x), round(screen_y))


def draw_cube(surface, projected, color):
    for start, end in EDGES:
        p1, p2 = projected[start], projected[end]
        if p1 is not None and p2 is not None:
            pygame.draw.line(surface, color, p1, p2, width=3)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pipeline grafico 3D - Aula 3")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    angles = [0.0, 0.0, 0.0]
    camera_z = 6.0
    projection = "perspectiva"

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p:
                    projection = (
                        "ortografica" if projection == "perspectiva" else "perspectiva"
                    )

        keys = pygame.key.get_pressed()
        speed = 2.0 * dt
        if keys[pygame.K_a]:
            angles[1] -= speed
        if keys[pygame.K_d]:
            angles[1] += speed
        if keys[pygame.K_w]:
            angles[0] -= speed
        if keys[pygame.K_s]:
            angles[0] += speed
        if keys[pygame.K_q]:
            angles[2] -= speed
        if keys[pygame.K_e]:
            angles[2] += speed
        if keys[pygame.K_EQUALS] or keys[pygame.K_KP_PLUS]:
            camera_z = max(2.0, camera_z - 3.0 * dt)
        if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
            camera_z = min(12.0, camera_z + 3.0 * dt)

        transformed = [transform(v, angles) for v in VERTICES]
        if projection == "perspectiva":
            projected = [project_perspective(v, 360, camera_z) for v in transformed]
        else:
            projected = [project_orthographic(v, 130) for v in transformed]

        screen.fill(BACKGROUND)
        draw_cube(screen, projected, CUBE_COLOR)

        info = f"Projeção: {projection} | Camera Z: {camera_z:.1f}"
        screen.blit(font.render(info, True, TEXT_COLOR), (20, 18))
        screen.blit(
            font.render(
                "A/D: Y | W/S: X | Q/E: Z | +/-: camera | P: troca | ESC: sai",
                True,
                TEXT_COLOR,
            ),
            (20, 48),
        )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
