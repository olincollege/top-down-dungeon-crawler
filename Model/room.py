""" """

from pytmx.util_pygame import load_pygame
from data_sprite import DataSprite
from tile import Tile
import pygame


class Room(DataSprite):
    """
    Creates a room for the player to traverse
    Inherits from DataSprite
    """

    def __init__(self, name, coordinates, filepath):
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
        super().__init__(name, coordinates, room=None, image=None)
        self.tile_group = pygame.sprite.Group()
        self.map_tmx = load_pygame(filepath)
        self.tile_id = 0
        for layer in self.map_tmx.layers:
            for x, y, surf in layer.tiles():
                self.temp_tile = Tile(
                    self.tile_id,
                    (
                        x,
                        y,
                    ),
                    name,
                    surf,
                    self.tile_group,
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
