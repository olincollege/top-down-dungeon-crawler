"""Runs the game"""

# external packages
import pygame

# internal packages
from Model.world_manager import WorldManager
from Model.player import Player
from controller import TopDownController


pygame.init()

TILE_SIZE = 32
WIDTH = 30
HEIGHT = 30

screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))


world = WorldManager()
current_room = world.get_room("Tent_Interior")
user = Player(
    sprite_list=[
        "sprite_up32.png",
        "sprite_right32.png",
        "sprite_down32.png",
        "sprite_left32.png",
    ],
    inventory=[],
    current_sprite=3,
    current_item=None,
    name="coco",
    coordinates=(0, 0),
    room=current_room,
)
controller = TopDownController()

imp = user.get_sprite_list()[3]
screen.blit(imp, (0, 0))
pygame.display.flip()


RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            current_room.tile_group.draw(screen)

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
