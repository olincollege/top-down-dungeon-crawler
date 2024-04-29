"""e"""

import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from Model.player import Player
from Model.room import Room


class View:
    """e"""

    def __init__(self):
        """ """

        self._screen = pygame.display.set_mode(
            (SCREEN_WIDTH * TILE_SIZE, SCREEN_HEIGHT * TILE_SIZE)
        )

    def draw(self, player=Player, current_room=Room):
        """e"""
        # fill with black
        self._screen.fill((0, 0, 0))
        # draw the current room's lower tiles
        current_room.get_tile_groups()["Lower"].draw(self._screen)
        # draw the player
        player_image = player.sprite_list[player.current_sprite]
        self._screen.blit(player_image, player.coordinates)
        # draw the current room's upper tiles
        current_room.get_tile_groups()["Upper"].draw(self._screen)
        # draw textbox
        # DRAW TEXTBOX CODE
        # upload the finalized frame image
        pygame.display.flip()
