"""
Lays out the information for a room
"""

from data_sprite import DataSprite


class Room(DataSprite):
    """
    Creates a room for the player to traverse
    Inherits from DataSprite
    """

    def __init__(self, name, coordinates, room, image):
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
        super().__init__(name, coordinates, room, image)
        # self._map = #json file of the map here

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
