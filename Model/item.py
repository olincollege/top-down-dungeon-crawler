"""
Lays out the information for each item
"""

from Model.tile import Tile


class Item(Tile):
    """
    Sets up an Item object
    """

    def __init__(self, name, coordinates, room, group, surf):
        """
        Initializes an item object

        Attributes:
            player_has: boolean of whether the player has
                the item
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """
        self._name = name
        self._player_has = False
        super().__init__(coordinates, room, group, surf)

    def get_player_has(self):
        """
        returns a boolean based on if the player has the item
        """
        return self._player_has

    def set_player_has(self, status):
        """
        sets whether the player has the item
        """
        self._player_has = status
        # to be changed later, if the player and the item have
        # the same coords, the player_has status will become true
