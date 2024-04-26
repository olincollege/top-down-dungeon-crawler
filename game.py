"""Runs the game"""

# external packages
from pytmx.util_pygame import load_pygame
import pygame

# internal packages
import Model
from Model.room import Room
import Model.character
from controller import TopDownController


pygame.init()

TILE_SIZE = 32
WIDTH = 30
HEIGHT = 30


user = Model.character.Character(
    [
        "sprite_up32.png",
        "sprite_right32.png",
        "sprite_down32.png",
        "sprite_left32.png",
    ],
    3,
    None,
    "coco",
    (0, 0),
    "basement",
)
controller = TopDownController()

screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
imp = user.get_sprite_list()[3]
screen.blit(imp, (0, 0))
pygame.display.flip()

test_room = Room(
    name="testroom",
    filepath="test_map_green_forest.tmx",
    portals=None,
    npcs=None,
    items=None,
)

test_dungeon = Room(
    name="testdungeon",
    filepath="test_map_green_dungeon.tmx",
    portals=None,
    npcs=None,
    items=None,
)

RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:

            test_dungeon.tile_group.draw(screen)

            match (event.key):
                case pygame.K_LEFT:
                    controller.move_left(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("LEFT")
                case pygame.K_RIGHT:
                    controller.move_right(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("RIGHT")
                case pygame.K_UP:
                    controller.move_up(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("UP")
                case pygame.K_DOWN:
                    controller.move_down(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("DOWN")
                case pygame.K_SPACE:
                    controller.check_npc_coords(
                        user, user.room, user.get_current_sprite()
                    )
                    controller.check_item_coords(user, user.room)
        pygame.display.update()
