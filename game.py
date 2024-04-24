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
WIDTH = 10
HEIGHT = 10


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
    ["sprite_left32.png"],
)
controller = TopDownController()
test_room = Room(
    name="testroom",
    filepath="Resources/Maps/test_map_green_forest.tmx",
    npcs=None,
    items=None,
)

screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
tmx = load_pygame("Resources/test_map.tmx")
imp = user.get_sprite_list()[3]
screen.blit(imp, (0, 0))
pygame.display.flip()

RUN = True

while RUN:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:

            match (event.key):
                case pygame.K_LEFT:
                    controller.move_left(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("LEFT")
                case pygame.K_RIGHT:
                    controller.move_right(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("RIGHT")
                case pygame.K_UP:
                    controller.move_up(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("UP")
                case pygame.K_DOWN:
                    controller.move_down(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("DOWN")
                case pygame.K_SPACE:
                    controller.check_npc_coords(
                        user, user.get_room(), user.get_current_sprite()
                    )
                    controller.check_item_coords(user, user.get_room())

        screen.fill("black")
        test_room.tile_group.draw(screen)
        pygame.display.update()
