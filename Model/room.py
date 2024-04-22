""" """

from pytmx.util_pygame import load_pygame
import data_sprite
import pygame


class Room(data_sprite.DataSprite):
    """
    e
    """

    def __init__(self, name, coordinates, room, filepath, image=None):
        """ """
        super().__init__(name, coordinates, room, image)
        tile_group = pygame.sprite.Group()
        map_tmx = load_pygame(filepath)
