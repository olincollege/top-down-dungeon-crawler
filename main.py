""" """

import pygame
from pytmx.util_pygame import load_pygame
from Model.room import Room


pygame.init()

TILE_SIZE = 32
WIDTH = 10
HEIGHT = 10


screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
tmx = load_pygame("Resources/test_map.tmx")

test_room = Room(
    name="testroom",
    filepath="/root/top-down-dungeon-crawler/Resources/test_map.tmx",
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")
    test_room.tile_group.draw(screen)

    pygame.display.update()
