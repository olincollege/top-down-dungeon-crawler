"""
e
"""

import pygame
from pytmx.util_pygame import load_pygame
from Model.room import Room


pygame.init()

WIDTH = 100
HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
tmx = load_pygame("Resources/test_map.tmx")

test_room = Room(
    name="testroom",
    coordinates=(0, 0),
    filepath="/root/top-down-dungeon-crawler/Resources/test_map.tmx",
)

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    screen.blit(test_room.tile_group)
    pygame.display.update()
