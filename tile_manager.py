"""
This class possesses all of the tiles.
"""

import pygame


class TileManager:
    """ """

    def __init__(self):
        self._tile_list = []

    def load(self, filepath, size, margin, spacing):
        """
        This function loads individual tile images from the tileset image and
        stores them in an array.

        Args:
            file: A file object representing the tileset image.
            size: A tuple of ints representing the pixel height and width of a
            resultant tile.
            margin: An int representing the pixel width of the edge of the
            tileset image.
            spacing: An int representing the pixel with of the spacing between
            tiles in the tile image.

        Returns: A list of tiles as image objects.
        """
        tiles = []
        image = pygame.image.load(open(filepath))
        rect = image.get_rect()
        x0 = y0 = margin
        w, h = rect.size
        dx = size[0] + spacing
        dy = size[1] + spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(size)
                tile.blit(image, (0, 0), (x, y, *size))
                tiles.append(tile)
        self._tile_list += tiles

    def get_tile(self, tile_code):
        """
        Get a tile image using its unique int code.

        Args:
            tile_code: An int representing a unique tile image.
        """
        print(
            f"Getting tile {tile_code} as {self._tile_list[tile_code]} out of {len(self._tile_list)} total tiles."
        )
        return self._tile_list[tile_code]
