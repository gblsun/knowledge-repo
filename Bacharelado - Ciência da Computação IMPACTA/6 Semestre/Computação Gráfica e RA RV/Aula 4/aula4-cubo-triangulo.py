"""
╔═══════════════════════════════════════════════════════════════╗
║  Aula 04 — EXERCÍCIO PRÁTICO — AULA 4         IMPACTA         ║
║  Computação Gráfica e RA/RV                                   ║
║  18 de Agosto de 2026                                         ║
╟───────────────────────────────────────────────────────────────╢
║  Anotações e comentários por Gabriel Muchon Pavanelli         ║
║  github: gblsunn                                              ║
╚═══════════════════════════════════════════════════════════════╝
"""

import math
import pygame
from pygame.locals import K_a, K_d, K_w, K_s, K_q, K_e, K_EQUALS, K_MINUS

WIDTH, HEIGHT = 960, 640
FPS = 60


# ---------------- Matrizes e vetores ----------------
def mat_mul(A, B):
    """Multiplica duas matrizes 4x4."""
    return [[sum(A[i][k] * B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def transform_point(M, p):
    """Aplica uma matriz 4x4 ao ponto 3D p=(x,y,z)."""
    x, y, z = p
    v = [x, y, z, 1.0]
    r = [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]
    w = r[3] if abs(r[3]) > 1e-8 else 1.0
    return (r[0] / w, r[1] / w, r[2] / w)


def identity():
    return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def translation(tx, ty, tz):
    M = identity()
    M[0][3], M[1][3], M[2][3] = tx, ty, tz
    return M


def scale(sx, sy, sz):
    return [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]


def rotation_x(a):
    c, s = math.cos(a), math.sin(a)
    return [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]


def rotation_y(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]]


def rotation_z(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


# ---------------- Modelos geométricos ----------------
def cube(size=2.0):
    h = size / 2
    vertices = [(-h, -h, -h), (h, -h, -h), (h, h, -h), (-h, h, -h),
                (-h, -h, h), (h, -h, h), (h, h, h), (-h, h, h)]
    faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
             (3, 2, 6, 7), (1, 5, 6, 2), (0, 3, 7, 4)]
    return vertices, faces


def pyramid(size=2.0, height=2.2):
    h = size / 2
    vertices = [(-h, 0, -h), (h, 0, -h), (h, 0, h), (-h, 0, h), (0, height, 0)]
    faces = [(0, 1, 2, 3), (0, 4, 1), (1, 4, 2), (2, 4, 3), (3, 4, 0)]
    return vertices, faces


# ---------------- Câmera e projeção ----------------
def project(point, camera_z, perspective=True):
    x, y, z = point
    z_view = z - camera_z
    # A câmera olha para +Z; pontos atrás/próximos demais são descartados.
    if z_view <= 0.1:
        return None
    if perspective:
        focal = 520.0
        sx = focal * x / z_view
        sy = focal * y / z_view
    else:
        sx = 230.0 * x
        sy = 230.0 * y
    return (int(WIDTH / 2 + sx), int(HEIGHT / 2 - sy), z_view)


def draw_model(screen, vertices, faces, model_matrix, camera_z, perspective, color):
    world = [transform_point(model_matrix, v) for v in vertices]
    projected = [project(v, camera_z, perspective) for v in world]
    for face in faces:
        points = [projected[i] for i in face]
        if all(p is not None for p in points):
            # Tom mais escuro para diferenciar as faces sem iluminação real.
            fill = tuple(max(25, c - 55) for c in color)
            pygame.draw.polygon(screen, fill, [(p[0], p[1]) for p in points])
            pygame.draw.lines(screen, color, True,
                               [(p[0], p[1]) for p in points], 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Computação Gráfica — Modelagem e Câmera')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 18)

    cube_v, cube_f = cube()
    pyr_v, pyr_f = pyramid()

    angle_x = angle_y = angle_z = 0.0
    camera_z = -8.0
    perspective = True

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p:
                    perspective = not perspective

        keys = pygame.key.get_pressed()
        speed = 2.0 * dt
        if keys[K_a]: angle_y -= speed
        if keys[K_d]: angle_y += speed
        if keys[K_w]: angle_x -= speed
        if keys[K_s]: angle_x += speed
        if keys[K_q]: angle_z -= speed
        if keys[K_e]: angle_z += speed
        if keys[K_EQUALS] or keys[pygame.K_KP_PLUS]: camera_z += 3.0 * dt
        if keys[K_MINUS] or keys[pygame.K_KP_MINUS]: camera_z -= 3.0 * dt

        screen.fill((12, 20, 35))

        # Ordem: escala -> rotações -> translação (composição matricial).
        R = mat_mul(rotation_z(angle_z), mat_mul(rotation_y(angle_y), rotation_x(angle_x)))
        cube_model = mat_mul(translation(-2.0, 0.0, 7.0), mat_mul(R, scale(1.2, 1.2, 1.2)))
        pyramid_model = mat_mul(translation(2.0, -1.0, 9.0), mat_mul(R, scale(1.0, 1.0, 1.0)))

        draw_model(screen, cube_v, cube_f, cube_model, camera_z, perspective, (80, 190, 255))
        draw_model(screen, pyr_v, pyr_f, pyramid_model, camera_z, perspective, (255, 170, 80))

        mode = 'perspectiva' if perspective else 'ortográfica'
        info = font.render(f'Projeção: {mode} | Câmera Z: {camera_z:.1f} | P: alternar', True,
                            (235, 235, 235))
        help_text = font.render('W/S X  A/D Y  Q/E Z  +/- câmera  ESC sair', True, (180, 200, 220))
        screen.blit(info, (18, 16))
        screen.blit(help_text, (18, 42))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
