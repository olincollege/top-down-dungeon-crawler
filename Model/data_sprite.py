"""
data_sprite.py is the file that most of our classes
inherit from. it will contain base attributes that
apply to all the classes in the other files
"""

import pygame


class DataSprite(pygame.sprite.Sprite):
    """
    DataSprite contains the base info that all of
    the other classes inherit from.
    """

    def __init__(self, name, coordinates, room):
        """
        Initializes the DataSprite object

        Attributes:
            name: String of the name of the sprite
            coordinates: tuple of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        self._name = name
        self._room = room
        self._coordinates = coordinates

    @property
    def name(self):
        """
        returns name of the object
        """
        return self._name

    @property
    def coordinates(self):
        """
        returns coordinates of the object
        """
        return self._coordinates

    @property
    def room(self):
        """
        returns room of the object
        """
        return self._room

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
