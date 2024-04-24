"""Runs the game"""

# external packages
from pytmx.util_pygame import load_pygame
import pygame

# internal packages
from Model.player import Player
from Model.room import Room
from controller import TopDownController


pygame.init()

TILE_SIZE = 32
WIDTH = 10
HEIGHT = 10


screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))

player = Player([], [], 0, None, "M", (0, 0), "testroom", [])
controller = TopDownController()
test_room = Room(
    name="testroom",
    filepath="Resources/Maps/test_map_green_forest.tmx",
    npcs=None,
    items=None,
)

RUN = True

while RUN:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:

            match (event.key):
                case pygame.K_LEFT:
                    controller.move_left(player)
                case pygame.K_RIGHT:
                    controller.move_right(player)
                case pygame.K_UP:
                    controller.move_up(player)
                case pygame.K_DOWN:
                    controller.move_down(player)
                case pygame.K_SPACE:
                    controller.check_npc_coords(
                        player, player.get_room(), player.get_current_sprite()
                    )
                    controller.check_item_coords(player, player.get_room())

        screen.fill("black")
        test_room.tile_group.draw(screen)
        pygame.display.update()
