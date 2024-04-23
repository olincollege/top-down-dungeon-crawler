"""
character.py lays out information for characters:
npc or players
"""

import pygame
from Model.data_sprite import DataSprite


class Character(DataSprite):
    """
    Class Character defines a new character, inherits from
    DataSprite Class in data_sprite.py
    """

    def __init__(
        self,
        sprite_list,
        current_sprite,
        current_item,
        name,
        coordinates,
        room,
        image,
    ):  # pylint: disable=too-many-arguments
        """
        Initializes a new character

        Attributes:
            sprite_list: list of images reprisenting the
                4 states the character sprite can be in
            current_sprite: int reprisenting which sprite from the list
                is currently used
            current_item: item that the character currently has
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        self._sprite_list = []
        for sprite in sprite_list:
            temp = pygame.image.load(sprite)
            self._sprite_list.append(temp)

        self._current_item = current_item
        self._current_sprite = current_sprite
        super().__init__(name, coordinates, room, image)

    def get_sprite_list(self):
        """
        Returns the sprite list of a character as a list of strings
        """
        return self._sprite_list

    def get_current_sprite(self):
        """
        Returns the current sprite orientation as an int
        0:up, 1:right, 2:down, 3:left
        """
        return self._current_sprite

    def get_current_item(self):
        """
        Returns the current item that the Character has
        """
        return self._current_item

    def set_current_sprite(self, orientation):
        """
        sets the current orientation of the sprite

        Args:
            orientation: int reprisenting which orientation the
                sprite is set to
                0:up, 1:right, 2:down, 3:left
        """
        self._current_sprite = orientation

    def set_current_item(self, item):
        """
        sets the current item that the chracter has

        Args:
            item: item that the character is set to have
        """
        self._current_item = item
