""" """

import pygame


class Tile(pygame.sprite.Sprite):
    """
    tile object
    """

    def __init__(self, coordinates, room, group, surf=pygame.Surface((32, 32))):
        super().__init__(group)
        self.room = room
        self.image = surf
        self.coordinates = coordinates
        self.pos = (coordinates[0] * 32, coordinates[1] * 32)
        self.rect = self.image.get_rect(topleft=self.pos)
