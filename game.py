"""Runs the game"""

# external packages
import pygame

# internal packages
from Model.player import Player
from controller import TopDownController
from view import View
from constants import TILE_SIZE


pygame.init()

# create management objects
view = View()
controller = TopDownController()


user = Player(
    sprite_list=[
        "Resources/Player Images/red_up_32.png",
        "Resources/Player Images/red_right_32.png",
        "Resources/Player Images/red_down_32.png",
        "Resources/Player Images/red_left_32.png",
    ],
    current_sprite=3,
    name="coco",
    coordinates=(3 * TILE_SIZE, 3 * TILE_SIZE),
    room=controller.current_room,
)


RUN = True

while RUN:
    for event in pygame.event.get():
        # kill program on exit
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_ESCAPE:
                    RUN = False
                case pygame.K_LEFT:
                    controller.move_left(user)
                case pygame.K_RIGHT:
                    controller.move_right(user)
                    print("RIGHT")
                case pygame.K_UP:
                    controller.move_up(user)
                    print("UP")
                case pygame.K_DOWN:
                    controller.move_down(user)
                    print("DOWN")
                case pygame.K_SPACE:
                    user.check_npc_coords(user.room, user.current_sprite)
                case pygame.K_i:
                    # user.open_inventory
                    controller.create_textbox(user.list_inventory())
                case pygame.K_x:
                    # user.close_textbox
                    controller.clear_text_box()

        view.draw(controller.text_box, user, controller.current_room)
