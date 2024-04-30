"""
player.py lays out all the information for a player
"""

import pygame
from constants import TILE_SIZE


class Player(pygame.sprite.Sprite):
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
            coordinates: tuple of 2 ints, reprisenting the location of sprite
            room: String of name of the room the sprite is in
        """
        # parameter init
        self._name = name
        self._room = room
        self._coordinates = coordinates
        # create sprites as images from filepaths
        self._sprite_list = []
        for sprite in sprite_list:
            temp = pygame.image.load(sprite)
            self._sprite_list.append(temp)
        # create current sprite info
        self._current_sprite = current_sprite
        self._image = self._sprite_list[self._current_sprite]
        self._rect = self._image.get_rect(topleft=self.coordinates)
        # give inventory
        self._inventory = []

    # getters/properties
    @property
    def name(self):
        """
        returns name of the object
        """
        return self._name

    @property
    def room(self):
        """
        returns room of the object
        """
        return self._room

    @property
    def coordinates(self):
        """
        returns coordinates of the object
        """
        return self._coordinates

    @property
    def sprite_list(self):
        """
        Returns the sprite list of a character as a list of Surfaces
        """
        return self._sprite_list

    @property
    def current_sprite(self):
        """
        Returns the current sprite orientation as an int
        0:up, 1:right, 2:down, 3:left
        """
        return self._current_sprite

    @property
    def rect(self):
        """
        Returns the character's rect
        """
        return self._rect

    @property
    def inventory(self):
        """
        Returns the inventory as a list of item names
        """
        item_names = []
        for item in self._inventory:
            item_names.append(item)
        return item_names

    # setters
    def set_room(self, room):
        """
        Setter method for room

        Args:
            room_name: a room object representing the new room
        """
        self._room = room

    def set_coordinates(self, coords):
        """
        Setter method for coordinates

        Args:
            coords: A tuple of ints representing the datasprite's new
            coordinates.

        """
        self._coordinates = coords

    def set_current_sprite(self, orientation):
        """
        sets the current orientation of the sprite

        Args:
            orientation: int reprisenting which orientation the
                sprite is set to
                0:up, 1:right, 2:down, 3:left
        """
        self._current_sprite = orientation

    def set_rect(self, new_coords):
        """
        sets the rect of the sprite

        Args:
            new_coords: tuple representing character's new coords
        """
        self._coordinates = new_coords
        self._rect = self._image.get_rect(topleft=self._coordinates)

    # function to call three common movement functions together
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

    # functions to manage the inventory
    def pick_up(self, item):
        """
        takes item to be picked up and places it in the inventory

        Args:
            item: item to be picked up
        """
        self._inventory.append(item.name)

    def give(self, item):
        """
        Takes item from inventory and deletes it

        Args:
            item: a string representing an item to be removed
        """
        self._inventory.remove(item)

    def list_inventory(self):
        """
        Returns a string of the current items in the inventory

        Returns:
            inv_string: string representation of the names of the items
                in the player inventory
        """
        inv_string = "Current Inventory: "

        for item in self._inventory:
            inv_string += f"{item}, "

        return inv_string[: len(inv_string) - 2]

    # function to see if an NPC is in front of the player
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
                        player_coords[1] - TILE_SIZE,
                    )
                    if player_up == npc_coords:
                        return npc

                case 1:
                    player_right = (
                        player_coords[0] + TILE_SIZE,
                        player_coords[1],
                    )
                    if player_right == npc_coords:
                        return npc

                case 2:
                    player_down = (
                        player_coords[0],
                        player_coords[1] + TILE_SIZE,
                    )
                    if player_down == npc_coords:
                        return npc

                case 3:
                    player_left = (
                        player_coords[0] - TILE_SIZE,
                        player_coords[1],
                    )
                    if player_left == npc_coords:
                        return npc

        return None

    # function to see if the player is colliding with something
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
                        and tile_coords[1] == player_coords[1] - TILE_SIZE
                    ):
                        return True
                case 1:
                    if (
                        tile_coords[0] == player_coords[0] + TILE_SIZE
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True
                case 2:
                    if (
                        tile_coords[0] == player_coords[0]
                        and tile_coords[1] == player_coords[1] + TILE_SIZE
                    ):
                        return True
                case 3:
                    if (
                        tile_coords[0] == player_coords[0] - TILE_SIZE
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True

        return False
