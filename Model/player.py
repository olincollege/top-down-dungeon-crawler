"""
player.py lays out all the information for a player
"""

from Model.character import Character


class Player(Character):
    """
    Creates a player object, inherits from Character
    """

    def __init__(
        self,
        inventory,
        sprite_list,
        current_sprite,
        current_item,
        name,
        coordinates,
        room,
    ):  # pylint: disable=too-many-arguments
        """
        Initializes a new npc

        Attributes:
            inventory: list of items that the player has
            sprite_list: list of images reprisenting the
                4 states the character sprite can be in
            current_sprite: int reprisenting which sprite from the list
                is currently used
            current_item: item that the character currently has
            name: String of the name of the sprite
            coordinates: list of 2 ints, reprisenting the location of the sprite
            room: String of name of the room the sprite is in
            image: image reprisenting the sprite, auto set to be a blank pygame
                surface of 32x32 px. Can be set to be any image
        """

        self._inventory = inventory
        super().__init__(
            sprite_list,
            current_sprite,
            current_item,
            name,
            coordinates,
            room,
        )

    def check_step(self):
        """
        Checks to see if the player has the same coordinates as any
        special tile.

        Returns an Portal or Item instance corresponding to the tile that
        the player shares coordinates with, or None if no such tile exists
        """
        portals = self._room.portal_list
        room_items = self._room.item_list

        for portal in portals:
            temp_portal_coords = portal.coordinates
            if self.coordinates == temp_portal_coords:
                return portal

        for item in room_items:
            temp_item_coords = item.coordinates
            if self.coordinates == temp_item_coords:
                return item

        return None

    def check_npc_coords(self, room, player_dir):
        """
        Checks to see if the player is interacting with an NPC.

        Args:
            player: a Player instance representing the player's information
            room: an Room instance representing the room's information
            player_dir: an int representing which direction the player is
            facing.

        Returns a NPC instance corresponding to the NPC that
        the player is interacting with, or None if no such NPC exists
        """

        npc_list = room.npc_list
        player_coords = player.coordinates

        for npc in npc_list:

            npc_coords = npc.coordinates

            match player_dir:
                case 0:
                    player_up = (
                        player_coords[0],
                        player_coords[1] + 1,
                    )
                    if player_up == npc_coords:
                        return npc

                case 1:
                    player_right = (
                        player_coords[0] + 1,
                        player_coords[1],
                    )
                    if player_right == npc_coords:
                        return npc

                case 2:
                    player_down = (
                        player_coords[0],
                        player_coords[1] - 1,
                    )
                    if player_down == npc_coords:
                        return npc

                case 3:
                    player_left = (
                        player_coords[0] - 1,
                        player_coords[1],
                    )
                    if player_left == npc_coords:
                        return npc

        return None

    def equip(self, item_num):
        """
        changes what item is currently in the hand of the player

        Args:
            item_num: index of the item that the character wants to move from
                their inventory into their hand
        """
        self.set_current_item(self._inventory[item_num])

    def pick_up(self, item):
        """
        takes item to be picked up and places it in the inventory

        Args:
            item: item to be picked up
        """
        if len(self._inventory) == 9:
            print(
                "Inventory Full!"
            )  # maybe change this later depending on how we print out messages like this
        else:
            self._inventory.append(item)

    def list_inventory(self):
        """
        Returns a string of the current items in the inventory

        Returns:
            inv_string: string reprisentation of the names of the items
                in the player inventory
        """
        inv_string = ""

        for item in self._inventory:
            inv_string += f"{item.name}\n"

        return inv_string
