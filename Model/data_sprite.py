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

    def __init__(self, name, coordinates, room, image=pygame.Surface([32,32])):
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
    
    #Add Getters 
    #setCoords do nothing, gets overriden
    #setRoom do nothing, gets overriden
    