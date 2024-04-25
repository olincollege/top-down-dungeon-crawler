""" """

import pygame
from pytmx.util_pygame import load_pygame
from Model.data_sprite import DataSprite
from Model.tile import Tile


class Room(pygame.sprite.Sprite):
    """
    Creates a room for the player to traverse
    Inherits from DataSprite
    """

    def __init__(self, name, filepath, npcs, items):
        """
        initializes the Room

        Attributes:
            _was_visited: boolean of whether the room has been visited
            _map: 2d array of sprites reprisenting the room
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        # super init
        super().__init__()
        # set from parameters
        self._name = name
        self._npc_list = npcs
        self._item_list = items
        # defining map and tilegroups
        self._tile_group = pygame.sprite.Group()
        self._map_tmx = load_pygame(filepath)
        self._tile_id = 0
        # cycle through all layers
        for layer in self._map_tmx.visible_layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():

                    Tile(
                        coordinates=(x, y),
                        room=self,
                        surf=surf,
                        group=self._tile_group,
                    )

        # other attributes
        self._was_visited = False

    @property
    def npc_list(self):
        """
        e
        """
        return self._npc_list

    @property
    def item_list(self):
        """
        e
        """
        return self._item_list

    @property
    def tile_group(self):
        return self._tile_group

    @property
    def was_visited(self):
        """
        returns whether the player has been to the room or not
        """
        return self._was_visited
