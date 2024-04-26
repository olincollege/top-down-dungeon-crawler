""" """

import pygame


class Tile(pygame.sprite.Sprite):
    """
    tile object
    """

    def __init__(self, coordinates, room, group, surf=pygame.Surface((32, 32))):
        super().__init__(group)
        self.room = room
        self.image = surf
        self.coordinates = coordinates
        self.pos = (coordinates[0] * 32, coordinates[1] * 32)
        self.rect = self.image.get_rect(topleft=self.pos)


class Portal(Tile):
    """
    Creates a portal tile
    """

    def __init__(
        self,
        dest_room,
        dest_coords,
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
            dest_room: room object that the portal leads to
            dest_coords: coordinates of the portal destination
            key: item object reprisenting the key to the portal
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        super().__init__(coordinates, room, group, surf)
        self._dest_room = dest_room
        self._dest_coords = dest_coords
        self._is_locked = is_locked
        self._key = key

    @property
    def get_is_locked(self):
        """
        Returns whether the portal is locked
        """
        return self._is_locked

    @property
    def get_dest_room(self):
        """
        Returns the destination room
        """
        return self._dest_room

    @property
    def get_dest_coords(self):
        """
        Returns the destination coords of the portal
        """
        return self._dest_coords

    @property
    def get_key(self):
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
