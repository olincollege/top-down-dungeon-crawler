"""
This file contains the Room class, which represents each map the player can
explore in the game.
"""

import pygame
from pytmx.util_pygame import load_pygame
from Model.tile import Tile, Portal, Item, NPC


class Room(pygame.sprite.Sprite):
    """
    A single map posessing tiles, items, and NPCs that the player can explore.

    Attributes:
        _name: The unique string name of the Room.
        _npc_list: A list of all of the NPC objects in the Room.
        _item_list: A list of all of the item objects in the Room.
        _portal_list: A list of all of the portal tiles in the Room.
        _collide_list: A list of all of the collidables tiles in the Room.
        _tile_groups: A dictionary in which the keys are the name of a tile
        group (Lower, Upper, NPC) and the values are the group itself.
    """

    def __init__(self, name, filepath, portals, items, npcs):
        """
        Initializes an instance of the Room class.

        Args:
            name: String of the name of the sprite.
            filepath: String representing the path to the .tmx map file.
            portals: A list of dictionaries in which each dictionary represents
            key/value pair information about a portal. Assumes that the list
            order matches the order in which they appear on the map.
            items: A list of names of items of this map.. Assumes that the list
            order matches the order in which they appear on the map.
            npcs: A list of dictionaries in which each dictionary represents
            key/value pair information about an NPC. Assumes that the list
            order matches the order in which they appear on the map.
        """
        # super init and set name
        super().__init__()
        self._name = name
        # create destination lists for special tiles
        self._npc_list = []
        self._item_list = []
        self._portal_list = []
        self._collide_list = []
        # defining map and tilegroups
        self._tile_groups = {
            "Lower": pygame.sprite.Group(),
            "NPC": pygame.sprite.Group(),
            "Upper": pygame.sprite.Group(),
        }
        # construct the npc group
        for npc in npcs:
            self._npc_list.append(
                NPC(
                    name=npc["name"],
                    surf=pygame.image.load(npc["filepath"]),
                    coordinates=tuple(npc["coordinates"]),
                    group=self._tile_groups["NPC"],
                    voice_lines=npc["voice_lines"],
                    item_wants=npc["item_wants"],
                )
            )
        # construct the map groups
        for layer in load_pygame(filepath).visible_layers:
            portal_count = 0
            item_count = 0
            for x, y, surf in layer.tiles():
                try:
                    # if layer is ceiling
                    if layer.name in ("Ceiling", "Ceiling_Deco"):
                        Tile(
                            coordinates=(x, y),
                            surf=surf,
                            group=self._tile_groups["Upper"],
                        )
                    # if layer is portals
                    elif layer.name == "Portals":
                        portal_data = portals[portal_count]
                        self._portal_list.append(
                            Portal(
                                coordinates=(x, y),
                                surf=surf,
                                group=self._tile_groups["Lower"],
                                dest_coords=portal_data["dest_coords"],
                                dest_room=portal_data["dest_room"],
                                dest_dir=portal_data["dest_dir"],
                            )
                        )
                        portal_count += 1
                    # if layer is items
                    elif layer.name == "Items":
                        item_name = items[item_count]
                        self._item_list.append(
                            Item(
                                coordinates=(x, y),
                                surf=surf,
                                group=self._tile_groups["Lower"],
                                name=item_name,
                            )
                        )
                        item_count += 1
                    # if layer is collidable
                    elif layer.name in ("Collidables", "Collidables_Deco"):
                        self._collide_list.append(
                            Tile(
                                coordinates=(x, y),
                                surf=surf,
                                group=self._tile_groups["Lower"],
                            )
                        )
                    # if layer is not empty
                    elif hasattr(layer, "data"):
                        Tile(
                            coordinates=(x, y),
                            surf=surf,
                            group=self._tile_groups["Lower"],
                        )
                # if no image, usually if pulling from the wrong tileset
                except AttributeError:
                    print(
                        f"No image in map {self.name} on layer {layer.name} at tile {(x,y)}"
                    )
                # if number of portals is different in JSON than in map object
                except IndexError:
                    print(
                        f"Too many portals in map {self.name} on layer {layer.name} at tile {(x,y)}"
                    )

    # getters
    @property
    def name(self):
        """
        Returns the name of the Room.
        """
        return self._name

    @property
    def npc_list(self):
        """
        Returns a list of the NPCs in the Room.
        """
        return self._npc_list

    @property
    def portal_list(self):
        """
        Returns a list of the portal tiles in the Room.
        """
        return self._portal_list

    @property
    def collide_list(self):
        """
        Returns a list of the collidable tiles in the Room.
        """
        return self._collide_list

    @property
    def item_list(self):
        """
        Returns a list of the items in the Room.
        """
        return self._item_list

    @property
    def tile_groups(self):
        """
        Returns the dictionary of tile groups.
        """
        return self._tile_groups

    # slightly more complex getter for collisions
    def get_all_collide(self):
        """
        Return all collidable objects, including collidable tiles and npcs.
        """
        return self.collide_list + self.npc_list

    # take an item out of the Room
    def remove_item(self, item=Item):
        """
        Function that removes an item from the Room and takes it off the map.

        Args:
            item: An item object that the player is picking up.
        """
        print(f"Player picked up item {item.name}!")
        self._item_list.remove(item)
        item.remove(self._tile_groups["Lower"])
