"""
player.py lays out all the information for a player
"""

from character import Character


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
        image,
    ):
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
            image,
        )

    def equip(self, item_num):
        """
        changes what item is currently in the hand of the player

        Args:
            item_num: index of the item that the character wants to move from
                their inventory into their hand
        """
        self.set_current_item(self._inventory[item_num])

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
