"""
view.py contains the class that sets the screen and
draws the player, map, and text to the screen
"""

import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from Model.player import Player
from Model.room import Room


class View:  # pylint: disable=too-few-public-methods
    """
    Sets the screen and draws the map, player, and text onto the screen

    Attributes:
        _screen: a Surface representing the screen that will be drawn on.
    """

    def __init__(self):
        """
        Initializes an instance of View and sets the screen to a size
        based on constants defined in constants.py
        """

        self._screen = pygame.display.set_mode(
            (SCREEN_WIDTH * TILE_SIZE, SCREEN_HEIGHT * TILE_SIZE)
        )

    def draw(self, text_box, player=Player, current_room=Room):
        """
        Draws the map and player or text to the screen.

        Args:
            text_box: a Surface representing the text that will
            be drawn, or None if there is no text
            player: a Player instance that contains all of the player's
            information
            current_room: a Room instance that contains all of the
            current room's information
        """
        # fill with black
        self._screen.fill((0, 0, 0))
        # if no textbox
        if text_box is None:
            # draw the current room's lower tiles
            current_room.get_tile_groups()["Lower"].draw(self._screen)
            # draw the player
            player_image = player.sprite_list[player.current_sprite]
            self._screen.blit(player_image, player.coordinates)
            # draw the current room's NPCs
            current_room.get_tile_groups()["NPC"].draw(self._screen)
            # draw the current room's upper tiles
            current_room.get_tile_groups()["Upper"].draw(self._screen)
        # if there is a textbox
        else:
            # Find value to center the textbox
            x = text_box.get_width()
            # Draw the textbox
            self._screen.blit(
                text_box,
                (
                    (SCREEN_WIDTH * TILE_SIZE - x) // 2,
                    SCREEN_HEIGHT * TILE_SIZE // 2,
                ),
            )
        # Update the display
        pygame.display.flip()
