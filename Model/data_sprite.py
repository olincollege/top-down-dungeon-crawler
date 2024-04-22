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

    def __init__(self, name, coordinates, room, image=pygame.Surface([32, 32])):
        """
        Initializes the DataSprite object

        Attributes:
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        self._name = name
        self._coordinates = coordinates
        self._image = image
        self._room = room
        self._rect = self.image.get_rect()

    @property
    def get_name(self):
        """
        returns name of the object
        """
        return self._name

    @property
    def get_coordinates(self):
        """
        returns coordinates of the object
        """
        return self._coordinates

    @property
    def get_image(self):
        """
        returns image of the object
        """
        return self._image

    @property
    def get_room(self):
        """
        returns room of the object
        """
        return self._room

    def set_coordinates(self, new_x, new_y):
        """
        Setter method for coordinates

        Args:
            new_x: an int representing the new x-coordinate
            new_y: an int representing the new y-coordinate

        """
        self._coordinates = (new_x, new_y)

    def set_room(self, room_name):
        """
        setter method for room, does nothing
        -- to be overriden
        """
