"""
player.py lays out all the information for a player
"""

import pygame
from constants import TILE_SIZE  # pylint: disable=import-error


class Player(
    pygame.sprite.Sprite
):  # pylint: disable=too-many-instance-attributes
    """
    Creates a player object

    Attributes:
        _name: a string representing the name of the player
        _room: a Room instance representing the room the
        player is in
        _coordinates: a tuple representing the x and y location
        of the player
        _sprite_list: a list of Surfaces representing the different
        sprites a player has
        _current_sprite: an integer from 0-3 representing which sprite
        the player needs to display - direction.
        _inventory: a list of strings that represent the item names that
        the player has in the inventory
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
        Initializes a new Player

        Args:
            sprite_list: a list of images that represent the different
            sprites a player has
            current_sprite: an integer representing what direction the
            player starts out facing - which sprite should be used
            name: a string representing the player's name
            coordinates: a tuple of integers representing the player's
            starting coordinates
            room: a Room instance representing what room the player
            starts in
        """
        # initialize name, room, coords
        self._name = name
        self._room = room
        self._coordinates = coordinates
        # create sprites as Surfaces from image filepaths
        self._sprite_list = []
        for sprite in sprite_list:
            temp = pygame.image.load(sprite)
            self._sprite_list.append(temp)
        # create current sprite info
        self._current_sprite = current_sprite
        # give inventory
        self._inventory = []

    # getters/properties
    @property
    def name(self):
        """
        Gets the name of the player.

        Returns the self._name attribute.
        """
        return self._name

    @property
    def room(self):
        """
        Gets the current room of the player

        Returns the self._room attribute.
        """
        return self._room

    @property
    def coordinates(self):
        """
        Gets the current coordinates of the player

        Returns the self._coordinates attribute.
        """
        return self._coordinates

    @property
    def sprite_list(self):
        """
        Gets the sprite list of the player.

        Returns the sprite list of the player as a list of Surfaces
        """
        return self._sprite_list

    @property
    def current_sprite(self):
        """
        Gets the current orientation of the player.

        Returns the current sprite orientation as an int -
        0:up, 1:right, 2:down, 3:left
        """
        return self._current_sprite

    @property
    def inventory(self):
        """
        Gets the inventory of the player

        Returns the inventory as a list of item names
        """
        item_names = []
        for item in self._inventory:
            item_names.append(item)
        return item_names

    # setters
    def set_room(self, room):
        """
        Sets the player's current room

        Args:
            room_name: a room object representing the new room
        """
        self._room = room

    def set_coordinates(self, coords):
        """
        Sets the player's current coordinates

        Args:
            coords: A tuple of ints representing the player's new
            coordinates.

        """
        self._coordinates = coords

    def set_current_sprite(self, orientation):
        """
        Sets the current orientation of the sprite

        Args:
            orientation: int representing which orientation the
                sprite is set to: 0:up, 1:right, 2:down, 3:left
        """
        self._current_sprite = orientation

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

    # functions to manage the inventory
    def pick_up(self, item):
        """
        Takes item to be picked up and places it's name in the inventory

        Args:
            item: item to be picked up
        """
        self._inventory.append(item.name)

    def give(self, item):
        """
        Takes item from inventory and deletes it

        Args:
            item: a string representing the item's name that will be removed
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

        inv_string = inv_string + ", ".join(self.inventory)

        return inv_string

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
        # Gets list of NPCs in the room
        npc_list = room.npc_list

        # Gets the player's current coordinates
        player_coords = self.coordinates

        # Cycles through the room's NPCs
        for npc in npc_list:
            # Gets the NPC's coordinates
            npc_coords = npc.coordinates

            match player_dir:
                # Checks if the coordinates above the player have a NPC
                case 0:
                    player_up = (
                        player_coords[0],
                        player_coords[1] - TILE_SIZE,
                    )
                    if player_up == npc_coords:
                        return npc
                # Checks if the coordinates right of the player have a NPC
                case 1:
                    player_right = (
                        player_coords[0] + TILE_SIZE,
                        player_coords[1],
                    )
                    if player_right == npc_coords:
                        return npc
                # Checks if the coordinates below the player have a NPC
                case 2:
                    player_down = (
                        player_coords[0],
                        player_coords[1] + TILE_SIZE,
                    )
                    if player_down == npc_coords:
                        return npc
                # Checks if the coordinates left of the player have a NPC
                case 3:
                    player_left = (
                        player_coords[0] - TILE_SIZE,
                        player_coords[1],
                    )
                    if player_left == npc_coords:
                        return npc

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
        # Gets the player's current coordinates
        player_coords = self.coordinates

        # Cycles through each collidable tile and gets its coordinates
        for tile in collidables:
            tile_coords = tile.coordinates

            match player_dir:
                # Checks if the coordinates above the player is collidable
                case 0:
                    if (
                        tile_coords[0] == player_coords[0]
                        and tile_coords[1] == player_coords[1] - TILE_SIZE
                    ):
                        return True
                # Checks if the coordinates right of the player is collidable
                case 1:
                    if (
                        tile_coords[0] == player_coords[0] + TILE_SIZE
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True
                # Checks if the coordinates below the player is collidable
                case 2:
                    if (
                        tile_coords[0] == player_coords[0]
                        and tile_coords[1] == player_coords[1] + TILE_SIZE
                    ):
                        return True
                # Checks if the coordinates left of the player is collidable
                case 3:
                    if (
                        tile_coords[0] == player_coords[0] - TILE_SIZE
                        and tile_coords[1] == player_coords[1]
                    ):
                        return True

        return False
