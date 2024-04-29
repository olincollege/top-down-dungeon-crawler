""" """

import pygame
from pytmx.util_pygame import load_pygame
from Model.tile import Tile, Portal, Item


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
        self._lower_tile_group = pygame.sprite.Group()
        self._upper_tile_group = pygame.sprite.Group()
        self._map_tmx = load_pygame(filepath)
        # construct the map group
        for layer in self._map_tmx.visible_layers:
            portal_count = 0
            item_count = 0
            for x, y, surf in layer.tiles():
                try:
                    # if layer is ceiling
                    if layer.name in ("Ceiling", "Ceiling_Deco"):
                        Tile(
                            coordinates=(x, y),
                            room=self,
                            surf=surf,
                            group=self._upper_tile_group,
                        )
                    # if layer is portals
                    elif layer.name == "Portals":
                        portal_data = portals[portal_count]
                        self._portal_list.append(
                            Portal(
                                coordinates=(x, y),
                                room=self,
                                surf=surf,
                                group=self._lower_tile_group,
                                dest_coords=portal_data["dest_coords"],
                                dest_room=portal_data["dest_room"],
                                dest_dir=portal_data["dest_dir"],
                                is_locked=portal_data["is_locked"],
                                key=portal_data["key"],
                            )
                        )
                        portal_count += 1
                    elif layer.name == "Items":
                        item_name = items[item_count]
                        self._item_list.append(
                            Item(
                                coordinates=(x, y),
                                room=self,
                                surf=surf,
                                group=self._lower_tile_group,
                                name=item_name,
                            )
                        )
                        item_count += 1
                    # if layer is collidable
                    elif layer.name in ("Collidables", "Collidables_Deco"):
                        self._collide_list.append(
                            Tile(
                                coordinates=(x, y),
                                room=self,
                                surf=surf,
                                group=self._lower_tile_group,
                            )
                        )
                    # if layer is not empty
                    elif hasattr(layer, "data"):
                        Tile(
                            coordinates=(x, y),
                            room=self,
                            surf=surf,
                            group=self._lower_tile_group,
                        )
                except AttributeError:
                    print(
                        f"No image in map {self.name} on layer {layer.name} at tile {(x,y)}"
                    )
                except IndexError:
                    print(
                        f"Too many portals in map {self.name} on layer {layer.name} at tile {(x,y)}"
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
    def was_visited(self):
        """
        returns whether the player has been to the room or not
        """
        return self._was_visited

    def get_tile_groups(self):
        """
        Function that gets both room tile groups and returns them
        in a dictionary.

        Returns a dictionary whose keys are "upper" and "lower" and
        whose values are the corresponding tile groups.
        """
        return {
            "Upper": self._upper_tile_group,
            "Lower": self._lower_tile_group,
        }

    def remove_item(self, item=Item):
        """
        Take an item out of the room.
        """
        print(f"Player picked up item {item.name}!")
        self._item_list.remove(item)
        item.remove(self._lower_tile_group)
