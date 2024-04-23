"""controller.py contains the class that controls the player
and it's interactions"""

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

    def check_item_coords(self, player, room):
        """
        Checks to see if the player has the same coordinates as any item in
        a room.

        Assumes that the parameters are a Player instance and Item instance,
        but will work with an instance of any class that inherits from
        DataSprite.

        Args:
            player: a Player instance representing the player's information
            room: an Room instance representing the room's information

        Returns an Item instance corresponding to the item that
        the player shares coordinates with, or None if no such item exists
        """
        player_coords = DataSprite.get_coordinates(player)

        room_items = room.get_item_list()

        for item in room_items:
            temp_item_coords = item.get_coords()
            if player_coords == temp_item_coords:
                return item

        return None

    def check_npc_coords(self, player, room, player_dir):
        """
        Checks to see if the player is interacting with an NPC.

        Args:
            player: a Player instance representing the player's information
            room: an Room instance representing the room's information
            player_dir: an int representing which direction the player is
            facing.

        Returns a NPC instance corresponding to the NPC that
        the player is interacting with, or None if no such NPC exists
        """

        npc_list = room.get_npc_list()
        player_coords = DataSprite.get_coordinates(player)

        for npc in npc_list:

            npc_coords = DataSprite.get_coordinates(npc)

            match player_dir:
                case 0:
                    player_up = (
                        player_coords[0],
                        player_coords[1] + 1,
                    )
                    if player_up == npc_coords:
                        return npc

                case 1:
                    player_right = (
                        player_coords[0] + 1,
                        player_coords[1],
                    )
                    if player_right == npc_coords:
                        return npc

                case 2:
                    player_down = (
                        player_coords[0],
                        player_coords[1] - 1,
                    )
                    if player_down == npc_coords:
                        return npc

                case 3:
                    player_left = (
                        player_coords[0] - 1,
                        player_coords[1],
                    )
                    if player_left == npc_coords:
                        return npc

        return None

    def move_left(self, player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = DataSprite.get_coordinates(player)

        DataSprite.set_coordinates(
            player, player_coords[0] - 32, player_coords[1]
        )

        Character.set_current_sprite(player, 3)

    def move_right(self, player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = DataSprite.get_coordinates(player)

        DataSprite.set_coordinates(
            player, player_coords[0] + 32, player_coords[1]
        )

        Character.set_current_sprite(player, 1)

    def move_down(self, player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = DataSprite.get_coordinates(player)

        DataSprite.set_coordinates(
            player, player_coords[0], player_coords[1] + 32
        )

        Character.set_current_sprite(player, 2)

    def move_up(self, player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        player_coords = DataSprite.get_coordinates(player)

        DataSprite.set_coordinates(
            player, player_coords[0], player_coords[1] - 32
        )

        Character.set_current_sprite(player, 0)

    def change_room(self, player):
        """
        Changes the current room a player is in based on the portal
        they entered

        Args:
            player: a Player instance representing the player's information
        """
        # next_room = portal.get_destination() - will work when
        # portal is implemented

        # player.set_room(next_room)
