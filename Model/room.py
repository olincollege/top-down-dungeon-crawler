""" """

import pygame
from pytmx.util_pygame import load_pygame
from Model.data_sprite import DataSprite
from Model.tile import Tile


class Room(DataSprite):
    """
    Creates a room for the player to traverse
    Inherits from DataSprite
    """

    def __init__(self, name, filepath):
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
        self._was_visited = False
        super().__init__(
            name, coordinates=None, room=None, image=pygame.Surface((32, 32))
        )
        self.tile_group = pygame.sprite.Group()
        self.map_tmx = load_pygame(filepath)
        self.tile_id = 0
        # cycle through all layers
        for layer in self.map_tmx.visible_layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    Tile(
                        coordinates=(x, y),
                        room=self,
                        surf=surf,
                        group=self.tile_group,
                    )

        for obj in self.map_tmx.objects:
            if obj.type in ("Building", "Vegetation"):
                Tile(
                    coordinates=(x, y),
                    room=self,
                    surf=obj.image,
                    group=self.tile_group,
                )

    def get_was_visited(self):
        """
        returns whether the player has been to the room or not
        """
        return self._was_visited

    def get_map(self):
        """
        Returns the map as a 2d array of sprites
        """
        # return self._map #Fill this in when json is set up
