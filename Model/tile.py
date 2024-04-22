""" """

import data_sprite
import pygame


class Tile(data_sprite.DataSprite):
    """
    tile object
    """

    def __init__(self, name, coordinates, room, surf, group):
        super().__init__(name, coordinates, room, surf)
        self.rect = self.image.get_rect(topleft=coordinates)
        pos = coordinates
        self.group = group
