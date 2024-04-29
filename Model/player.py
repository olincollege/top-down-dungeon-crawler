"""
player.py lays out all the information for a player
"""

from Model.character import Character

TILE_WIDTH = 32
TILE_HEIGHT = 32


class Player(Character):
    """
    Creates a player object, inherits from Character
    """

    def __init__(
        self,
        sprite_list,
        current_sprite,
        name,
        coordinates,
        room,
    ):  # pylint: disable=too-many-arguments
        """
        Initializes a new npc

        Attributes:
            inventory: list of items that the player has
            sprite_list: list of images reprisenting the
                4 states the character sprite can be in
            current_sprite: int reprisenting which sprite from the list
                is currently used
            current_item: item that the character currently has
            name: String of the name of the sprite
            coordinates: tuple of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
        """
        # give inventory
        self._inventory = []
        # init
        super().__init__(
            sprite_list,
            current_sprite,
            name,
            coordinates,
            room,
        )

    def check_npc_coords(self, room, player_dir):
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

        npc_list = room.npc_list
        player_coords = self.coordinates

        for npc in npc_list:

            npc_coords = npc.coordinates

            match player_dir:
                case 0:
                    player_up = (
                        player_coords[0],
                        player_coords[1] - TILE_HEIGHT,
                    )
                    if player_up == npc_coords:
                        return npc.voice_line

                case 1:
                    player_right = (
                        player_coords[0] + TILE_WIDTH,
                        player_coords[1],
                    )
                    if player_right == npc_coords:
                        return npc.voice_line

                case 2:
                    player_down = (
                        player_coords[0],
                        player_coords[1] + TILE_HEIGHT,
                    )
                    if player_down == npc_coords:
                        return npc.voice_line

                case 3:
                    player_left = (
                        player_coords[0] - TILE_WIDTH,
                        player_coords[1],
                    )
                    if player_left == npc_coords:
                        return npc.voice_line

        return None

    def check_collision(self, player_dir, collidables):
        """
        Checks to see if the player will collide with a tile

        Args:
            player: a Player instance representing the player's information
            room: an Room instance representing the room's information
            player_dir: an int representing which direction the player is
            facing.
            collidables: a list of tiles representing the collidable objects
            in the current room.

        Returns True if the character will collide, and False if it won't
        """
        player_coords = self.coordinates

        for tile in collidables:
            tile_coords = tile.coordinates

            match player_dir:
                case 0:
                    if (
                        tile_coords[0] == player_coords[0]
                        and tile_coords[1] == player_coords[1] - TILE_HEIGHT
                    ):
                        return True
                case 1:
                    if (
                        tile_coords[0] == player_coords[0] + TILE_WIDTH
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True
                case 2:
                    if (
                        tile_coords[0] == player_coords[0]
                        and tile_coords[1] == player_coords[1] + TILE_HEIGHT
                    ):
                        return True
                case 3:
                    if (
                        tile_coords[0] == player_coords[0] - TILE_WIDTH
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True

        return False

    def pick_up(self, item):
        """
        takes item to be picked up and places it in the inventory

        Args:
            item: item to be picked up
        """
        self._inventory.append(item)

    def list_inventory(self):
        """
        Returns a string of the current items in the inventory

        Returns:
            inv_string: string reprisentation of the names of the items
                in the player inventory
        """
        inv_string = "Current Inventory: "

        for item in self._inventory:
            inv_string += f"{item.name}, "

        return inv_string[: len(inv_string) - 2]

    def set_coordinates(self, coords):
        """
        Setter method for coordinates

        Args:
            coords: A tuple of ints representing the datasprite's new
            coordinates.

        """
        self._coordinates = coords

    def set_room(self, room):
        """
        Setter method for room

        Args:
            room_name: a room object representing the new room
        """
        self._room = room

    def update_movement(self, new_dir, x_mod, y_mod):
        """
        Groups all of the standard movement functions.

        Args:
            new_dir: An int representing the new direction to face.
            x_mod: An int by which to change the x coordinate.
            y_mod: An int by which to change the y coordinate.
        """
        self.set_coordinates(
            (self.coordinates[0] + x_mod, self.coordinates[1] + y_mod)
        )
        self.set_current_sprite(new_dir)
        self.set_rect(self.coordinates)
