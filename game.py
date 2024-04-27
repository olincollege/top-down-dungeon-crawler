"""Runs the game"""

# external packages
import pygame

# internal packages
from Model.player import Player
from controller import TopDownController


pygame.init()

TILE_SIZE = 32
SCREEN_WIDTH = 30
SCREEN_HEIGHT = 30

screen = pygame.display.set_mode(
    (SCREEN_WIDTH * TILE_SIZE, SCREEN_HEIGHT * TILE_SIZE)
)


controller = TopDownController()
current_room = controller.current_room
user = Player(
    sprite_list=[
        "sprite_up32.png",
        "sprite_right32.png",
        "sprite_down32.png",
        "sprite_left32.png",
    ],
    current_sprite=3,
    name="coco",
    coordinates=(3 * TILE_SIZE, 3 * TILE_SIZE),
    room=current_room,
)

imp = user.get_sprite_list()[3]
screen.blit(imp, user.coordinates)
pygame.display.flip()


RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        current_room = controller.current_room
        current_room.tile_group.draw(screen)

        if event.type == pygame.KEYDOWN:
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
                    user.check_npc_coords(user.room, user.dir)
                    user.check_item_coords()
        pygame.display.update()
