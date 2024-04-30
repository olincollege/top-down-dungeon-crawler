""" """

import pygame
from constants import TILE_SIZE
from Model.player import Player


class Tile(pygame.sprite.Sprite):
    """
    tile object
    """

    def __init__(
        self,
        coordinates,
        room,
        group,
        surf=pygame.Surface((TILE_SIZE, TILE_SIZE)),
    ):
        super().__init__(group)
        self._room = room
        self._image = surf
        self._coordinates = (
            coordinates[0] * TILE_SIZE,
            coordinates[1] * TILE_SIZE,
        )
        self._rect = self.image.get_rect(topleft=self.coordinates)

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
        Gets the pos of this tile.
        """
        return self._rect


class Portal(Tile):
    """
    Creates a portal tile
    """

    def __init__(
        self,
        dest_room,
        dest_coords,
        dest_dir,
        coordinates,
        room,
        surf,
        group,
        is_locked=False,
        key=None,
    ):  # pylint: disable=too-many-arguments
        """
        initializes a new portal object.

        Attributes:
            is_locked: boolean of whether the portal is availble to use
            dest_room: string name of room that the portal leads to
            dest_coords: int tuple coordinates of the portal destination
            key: item object reprisenting the key to the portal
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        super().__init__(coordinates, room, group, surf)
        self._dest_room = dest_room
        self._dest_dir = dest_dir
        self._dest_coords = (
            dest_coords[0] * TILE_SIZE,
            dest_coords[1] * TILE_SIZE,
        )
        self._is_locked = is_locked
        self._key = key

    @property
    def is_locked(self):
        """
        Returns whether the portal is locked
        """
        return self._is_locked

    @property
    def dest_room(self):
        """
        Returns the destination room
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

    @property
    def key(self):
        """
        Returns the key item for the portal
        """
        return self._key

    def unlock(self, key_input):
        """
        unlocks the room based on the players input key item

        Attributes:
            key_input: item that the player inputs
        """
        if key_input == self._key:
            self._is_locked = False


class Item(Tile):
    """
    Sets up an Item object
    """

    def __init__(self, name, coordinates, room, group, surf):
        """
        Initializes an item object

        Attributes:
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        self._name = name
        super().__init__(coordinates, room, group, surf)

    @property
    def name(self):
        """
        eee"""
        return self._name


class NPC(Tile):
    """
    Class Npc defines a new npc,.
    """

    def __init__(
        self,
        voice_lines,
        item_wants,
        surf,
        group,
        name,
        coordinates,
        room,
    ):
        """
        Initializes a new npc

        Attributes:
            voice_line: List of strings representing what the npc says when
                a player interacts, gives an item, or after satisfied
            is_satisfied: boolean of whether the npc has gotten the item
                or not
            item_wants: item that the npc needs to be satisfied

        """
        super().__init__(coordinates, room, group, surf)
        self._name = name
        self._voice_line_init = voice_lines[0]
        self._voice_line_received = voice_lines[1]
        self._voice_line_after = voice_lines[2]
        self._is_satisfied = False
        self._item_wants = item_wants
        self._player_visits = False

    @property
    def voice_lines(self):
        """
        Returns the voice lines of the npc
        """
        return self._voice_lines

    @property
    def is_satisfied(self):
        """
        Returns whether the npc is satisfied
        """
        return self._is_satisfied

    @property
    def item_wants(self):
        """
        Returns the desired item of the npc
        """
        return self._item_wants

    @property
    def name(self):
        """
        eee"""
        return self._name

    def det_voice(self, player=Player):
        """
        Determines which voiceline the NPC will give to the player,
        based on whether or not the player has the item they want.

        Args:
            player: a Player instance that represents the information of the
            player

        Returns the correct string
        """
        if self._is_satisfied:
            return self._voice_line_after
        if self._item_wants in player.inventory and self._player_visits:
            player.give(self._item_wants)
            self._is_satisfied = True
            return self._voice_line_received
        self._player_visits = True
        return self._voice_line_init
