"""controller.py contains the class that controls the player
and it's interactions"""

from Model.room import Room
from Model.tile import Tile
from Model.tile import Portal
from Model.data_sprite import DataSprite
from Model.character import Character

TILE_HEIGHT = 8
TILE_WIDTH = 8


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items
    """

    def __init__(self):
        pass

    def change_room(self, player, portal):
        """
        Changes the current room a player is in based on the portal
        they entered

        Args:
            player: a Player instance representing the player's information
            portal: a Portal instance that represents the portal's information
        """
        next_room = portal.get_dest_room
        player.set_room(next_room)

    def move_left(self, player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = player.coordinates

        player.set_coordinates(player_coords[0] - 32, player_coords[1])

        Character.set_current_sprite(player, 3)

    def move_right(self, player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = player.coordinates

        player.set_coordinates(player_coords[0] + 32, player_coords[1])

        Character.set_current_sprite(player, 1)

    def move_down(self, player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = player.coordinates
        player.set_coordinates(player_coords[0], player_coords[1] + 32)

        Character.set_current_sprite(player, 2)

    def move_up(self, player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = player.coordinates

        player.set_coordinates(player_coords[0], player_coords[1] - 32)

        Character.set_current_sprite(player, 0)
