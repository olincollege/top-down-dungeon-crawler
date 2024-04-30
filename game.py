"""Runs the game"""

# external packages
import pygame

# internal packages
from Model.player import Player
from controller import TopDownController
from view import View
from constants import TILE_SIZE

# initialize pygame
pygame.init()

# create management objects
view = View()
controller = TopDownController()

# create player
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

# create welcome screen
controller.create_textbox(
    "Welcome to Sandman's Adventure! Press X to start, and Q for instructions"
)

# create game run variable
RUN = True

# run game
while RUN:
    # get events in the game
    for event in pygame.event.get():
        # kill program on exit
        if event.type == pygame.QUIT:
            RUN = False

        # check for pressed keys
        if event.type == pygame.KEYDOWN:
            match (event.key):
                # exit game
                case pygame.K_ESCAPE:
                    RUN = False
                # move left
                case pygame.K_LEFT:
                    controller.move_left(user)
                # move right
                case pygame.K_RIGHT:
                    controller.move_right(user)
                # move up
                case pygame.K_UP:
                    controller.move_up(user)
                # move down
                case pygame.K_DOWN:
                    controller.move_down(user)
                # interact with npcs
                case pygame.K_SPACE:
                    IS_NPC = user.check_npc_coords(
                        user.room, user.current_sprite
                    )
                    if IS_NPC is not None:
                        controller.create_textbox(IS_NPC.det_voice(user))
                # open inventory
                case pygame.K_i:
                    controller.create_textbox(user.list_inventory())
                # remove text boxes
                case pygame.K_x:
                    controller.clear_text_box()
                # show instructions
                case pygame.K_q:
                    controller.instruct()
        # draw updated worldstate to screen
        view.draw(controller.text_box, user, controller.current_room)
