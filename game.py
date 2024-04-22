"""Runs the game"""

import pygame

import Model

import Model.data_sprite
import Model.player
import Model.room
from controller import TopDownController

import view


pygame.init()

# view initialization

player = Model.player.Player([], [], 0, None, "M", (0, 0), "basement", [])


controller = TopDownController()

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
