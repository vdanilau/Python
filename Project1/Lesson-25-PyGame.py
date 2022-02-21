import pygame     # установка из cmd: python -m pip install --user pygame
# import pygame.examples.stars # Примеры игр
# pygame.examples.stars.main()

pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    pygame.display.flip()
