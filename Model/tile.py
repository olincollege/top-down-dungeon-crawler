"""
This file contains class Tile and its subclasses. Any class that is tile-like,
including NPCs, Items, and Portals, can be found here.
"""

import pygame
from constants import TILE_SIZE


class Tile(pygame.sprite.Sprite):
    """
    A standard tile representing one square of information on the map.

    Attributes:
        _group: An instance of the pygame Group class. This attribute
        designates the Tile instance as part of one of its parent Room's
        groups, which is useful for drawing the map.
        _coordinates: An tuple of ints in which the first item is the x
        position and the second item is the y position. Units are pixels.
        _image: A Surface which is the image the tile should display.
        _rect: A Rect object which derives from the tile image and allows it
        to be drawn in a group.
    """

    def __init__(
        self,
        coordinates,
        group,
        surf,
    ):
        """
        Initializes an instance of the Tile class.

        Args:
            coordinates: Sets the coordinates.
            group: Sets the group.
            surf: Sets the image.
        """
        # super the group
        super().__init__(group)
        # define coordinates in pixel size
        self._coordinates = (
            coordinates[0] * TILE_SIZE,
            coordinates[1] * TILE_SIZE,
        )
        # create image variables
        self._image = surf
        self._rect = self.image.get_rect(topleft=self.coordinates)

    # getters
    @property
    def coordinates(self):
        """
        Gets the coordinates of this tile.
        """
        return self._coordinates

    @property
    def image(self):
        """
        Gets the image of this tile.
        """
        return self._image

    @property
    def rect(self):
        """
        Gets the rect of this tile.
        """
        return self._rect


class Portal(Tile):
    """
    A special tile that, when stepped on, transports the Player to a new room.

    Attributes:
        _dest_room: The string name of the Room the player should appear in
        after stepping on this tile.
        _dest_coords: The coordinates the player should appear in after
        stepping on this tile.
        _dest_dir: The int value representing the direction the player should
        face after stepping on this tile.
    """

    def __init__(
        self,
        dest_room,
        dest_coords,
        dest_dir,
        coordinates,
        surf,
        group,
    ):  # pylint: disable=too-many-arguments
        """
        Initializes an instance of the Portal class.

        Args:
            dest_room: Sets the destination room.
            dest_coords: Sets the destination coordinates.
            dest_dir: Sets the destination direction.
            coordinates: Sets the coordinates.
            surf: Sets the image.
            group: Sets the group.
        """
        super().__init__(coordinates, group, surf)
        self._dest_room = dest_room
        self._dest_dir = dest_dir
        self._dest_coords = (
            dest_coords[0] * TILE_SIZE,
            dest_coords[1] * TILE_SIZE,
        )

    # getters
    @property
    def dest_room(self):
        """
        Returns the destination room of the portal.
        """
        return self._dest_room

    @property
    def dest_coords(self):
        """
        Returns the destination coords of the portal.
        """
        return self._dest_coords

    @property
    def dest_dir(self):
        """
        Returns the destination direction of the portal.
        """
        return self._dest_dir


class Item(Tile):
    """
    A special tile that can be picked up by the player.

    Attributes:
        _name: A string representing the name of the item. Once the item is
        taken off the map, it is only referred to by name rather than any
        other unique attributes.
    """

    def __init__(self, name, coordinates, group, surf):
        """
        Initializes an instance of the Item class.

        Attributes:
            name: Sets the name.
            coordinates: Sets the coordinates.
            group: Sets the group.
            Surf: Sets the image.
        """
        # super
        super().__init__(coordinates, group, surf)
        self._name = name

    @property
    def name(self):
        """
        Returns the string name of the item.
        """
        return self._name


class NPC(Tile):
    """
    A special tile that can be collided with and spoken to.

    Attributes:
    _name:  A string representing the name of the NPC.
    _voice_line_init: A string representing what the NPC will say if it has
    not received the item it wants yet.
    _voice_line_received: A string representing what the NPC will say if it has
    just received the item it wants.
    _voice_line_after: A string representing what the NPC will say once it
    possesses the item it wants.
    _item_wants: A string representing the name of the item that the NPC wants.
    _is_satisfied: A boolean representing whether the NPC has received the item
    that it wants in order to be completed.
    _player_visits: A boolean representing whether or not the player has spoken
    to this NPC yet.
    """

    def __init__(
        self,
        voice_lines,
        item_wants,
        surf,
        group,
        name,
        coordinates,
    ):  # pylint: disable=too-many-arguments
        """
        Initializes an instance of the NPC class.

        Args:
            name: Sets the name.
            voice_lines: List of strings that sets what the NPC says when
            a player interacts, gives an item, or after satisfied.
            item_wants: Sets the item that the NPC wants.
            surf: Sets the image.
            group: Sets the group.
            coordinates: Sets the coordinates.
        """
        # super
        super().__init__(coordinates, group, surf)
        # set from parameters
        self._name = name
        self._item_wants = item_wants
        # set voice lines
        self._voice_line_init = voice_lines[0]
        self._voice_line_received = voice_lines[1]
        self._voice_line_after = voice_lines[2]
        # set default attributes
        self._is_satisfied = False
        self._player_visits = False

    # getters
    @property
    def is_satisfied(self):
        """
        Returns whether or not the NPC is satisfied.
        """
        return self._is_satisfied

    @property
    def item_wants(self):
        """
        Returns the string name of the desired item of the NPC.
        """
        return self._item_wants

    @property
    def name(self):
        """
        Returns the string name of the NPC.
        """
        return self._name

    # determine current voiceline
    def det_voice(self, player):
        """
        Determines which voiceline the NPC will give to the player, based on
        whether or not the player has the item they want and whether the player
        has spoken to this NPC yet.

        Args:
            player: the current player, who is of the Player class.

        Returns the correct voiceline for the situation.
        """
        # if possessing the item
        if self._is_satisfied:
            return self._voice_line_after
        # if just receiving the item now
        if self._item_wants in player.inventory and self._player_visits:
            player.give(self._item_wants)
            self._is_satisfied = True
            return self._voice_line_received
        # if never visited yet
        self._player_visits = True
        return self._voice_line_init
