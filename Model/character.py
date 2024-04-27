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
    ):  # pylint: disable=too-many-arguments
        """
        Initializes a new character

        Attributes:
            sprite_list: list of Surfaces representing the
                4 states the character sprite can be in
            current_sprite: int representing which sprite from the list
                is currently used
            current_item: item that the character currently has
            name: String of the name of the sprite
            coordinates: tuple of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            pos: a tuple representing the pixel location of the character
            image: a Surface representing the image of the character
            rect: a Rect representing the rectangle around the character
            for collision detection
        """
        self._sprite_list = []
        for sprite in sprite_list:
            temp = pygame.image.load(sprite)
            self._sprite_list.append(temp)

        self._current_item = current_item
        self._current_sprite = current_sprite
        super().__init__(name, coordinates, room)
        self._pos = (coordinates[0] * 32, coordinates[1] * 32)
        self._image = self._sprite_list[self._current_sprite]
        self._rect = self._image.get_rect(topleft=self._pos)

    def get_sprite_list(self):
        """
        Returns the sprite list of a character as a list of Surfaces
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

    @property
    def rect(self):
        """
        Returns the character's rect
        """
        return self._rect

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
            item: string representing item that the character is set to have
        """
        self._current_item = item

    def set_rect(self, new_pos):
        """
        sets the rect of the sprite

        Args:
            new_coords: tuple representing character's new coords
        """
        self._rect = self._image.get_rect(topleft=new_pos)
