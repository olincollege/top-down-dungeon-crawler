import pygame
from pytmx.util_pygame import load_pygame
from tile_manager import TileManager

tile_manager = TileManager()

tile_manager.load("Resources/32x32.png", (32, 32), 0, 0)
test_surface = tile_manager.get_tile(3)

from pytmx.util_pygame import load_pygame


pygame.init()

WIDTH = 100
HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
tmx = load_pygame("Resources/test_map.tmx")

print(dir(tmx.get_layer_by_name("Dirt")))

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.blit(test_surface, [100, 100])
    pygame.display.update()
