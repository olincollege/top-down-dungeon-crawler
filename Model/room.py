""" """

import pygame
from pytmx.util_pygame import load_pygame
from Model.tile import Tile
from Model.tile import Portal


class Room(pygame.sprite.Sprite):
    """
    Creates a room for the player to traverse
    Inherits from DataSprite
    """

    def __init__(self, name, filepath, portals, items, npcs):
        """
        initializes the Room

        Attributes:
            name: String of the name of the sprite
            filepath: String representing the path to the .tmx map file
            portals: A list of dictionaries in which each dictionary represents
            key/value pair information about a portal. Assumes that the list
            order matches the order in which they appear on the map.
            items: A list of dictionaries in which each dictionary represents
            key/value pair information about an item. Assumes that the list
            order matches the order in which they appear on the map.
            NPCs: A list of dictionaries in which each dictionary represents
            key/value pair information about an NPC. Assumes that the list
            order matches the order in which they appear on the map.
        """
        # super init
        super().__init__()
        # set from parameters
        self._name = name
        # other attributes
        self._was_visited = False
        # unpack dictionary information (neither of these are good at all)
        # make it tile based in the future for loops
        self._npc_list = []
        self._item_list = []
        self._portal_list = []
        self._collide_list = []
        # defining map and tilegroups
        self._tile_group = pygame.sprite.Group()
        self._map_tmx = load_pygame(filepath)
        # construct the map group
        for layer in self._map_tmx.visible_layers:
            # if layer is portals
            if layer.name == "Portals":
                portal_count = 0
                for x, y, surf in layer.tiles():
                    try:
                        portal_data = portals[portal_count]
                        self._portal_list.append(
                            Portal(
                                coordinates=(x, y),
                                room=self,
                                surf=surf,
                                group=self._tile_group,
                                dest_coords=portal_data["dest_coords"],
                                dest_room=portal_data["dest_room"],
                                is_locked=portal_data["is_locked"],
                                key=portal_data["key"],
                            )
                        )
                        portal_count += 1
                    except AttributeError:
                        print(
                            f"Image error in room {self._name} layer {layer.name} at tile {(x,y)}"
                        )
                    except IndexError:
                        print(
                            f"Index error in room {self._name} layer {layer.name} at tile {(x,y)}"
                        )
            # if layer is collidable
            elif layer.name in ("Collidables", "Collidables_Deco"):
                for x, y, surf in layer.tiles():
                    try:
                        self._collide_list.append(
                            Tile(
                                coordinates=(x, y),
                                room=self,
                                surf=surf,
                                group=self._tile_group,
                            )
                        )
                    except AttributeError:
                        print(
                            f"Image error in room {self._name} layer {layer.name} at tile {(x,y)}"
                        )

            # if layer is not empty
            elif hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    try:
                        Tile(
                            coordinates=(x, y),
                            room=self,
                            surf=surf,
                            group=self._tile_group,
                        )
                    except AttributeError:
                        print(
                            f"Image error in room {self._name} layer {layer.name} at tile {(x,y)}"
                        )

    @property
    def name(self):
        """
        e
        """
        return self._name

    @property
    def npc_list(self):
        """
        e
        """
        return self._npc_list

    @property
    def portal_list(self):
        """
        e
        """
        return self._portal_list

    @property
    def collide_list(self):
        """
        e
        """
        return self._collide_list

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
