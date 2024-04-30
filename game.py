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
    current_sprite=2,
    name="Sandman",
    coordinates=(3 * TILE_SIZE, 15 * TILE_SIZE),
    room=controller.current_room,
)

controller.create_textbox(
    "Welcome to Sandman's Adventure! Press X to start, and Q to display instructions"
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
                case pygame.K_UP:
                    controller.move_up(user)
                case pygame.K_DOWN:
                    controller.move_down(user)
                case pygame.K_SPACE:
                    is_npc = user.check_npc_coords(
                        user.room, user.current_sprite
                    )
                    if is_npc is not None:
                        controller.create_textbox(is_npc.det_voice(user))
                case pygame.K_i:
                    # user.open_inventory
                    controller.create_textbox(user.list_inventory())
                case pygame.K_x:
                    # user.close_textbox
                    controller.clear_text_box()
                case pygame.K_q:
                    controller.instruct()

        view.draw(controller.text_box, user, controller.current_room)
