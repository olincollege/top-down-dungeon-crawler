"""
character.py lays out information for characters:
npc or players
"""

import pygame


class Character(pygame.sprite.Sprite):
    """
    Class Character defines a new character, inherits from
    DataSprite Class in data_sprite.py
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
            image: a Surface representing the image of the character
            rect: a Rect representing the rectangle around the character
            for collision detection
        """
        # init
        self._name = name
        self._room = room
        self._coordinates = coordinates
        # create sprites
        self._sprite_list = []
        for sprite in sprite_list:
            temp = pygame.image.load(sprite)
            self._sprite_list.append(temp)
        # create current sprite info
        self._current_sprite = current_sprite
        self._image = self._sprite_list[self._current_sprite]
        self._rect = self._image.get_rect(topleft=self.coordinates)

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
