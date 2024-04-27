"""
npc.py lays out information for npc's,
"""

from character import Character


class Npc(Character):
    """
    Class Npc defines a new npc, inherits from
    Character Class in character.py
    """

    def __init__(
        self,
        voice_line,
        is_satisfied,
        item_wants,
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
            voice_line: String reprisenting what the npc says when
                a player interacts/goes in room
            is_satisfied: boolean of whether the npc has gotten the item
                or not
            item_wants: item that the npc needs to be satisfied
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

        self._voice_line = voice_line
        self._is_satisfied = is_satisfied
        self._item_wants = item_wants
        super().__init__(
            sprite_list,
            current_sprite,
            current_item,
            name,
            coordinates,
            room,
        )  # pylint: disable=too-many-arguments

    @property
    def get_voice_line(self):
        """
        Returns the voice line of the npc
        """
        return self._voice_line

    @property
    def get_is_satisfied(self):
        """
        Returns whether the npc is satisfied
        """
        return self._is_satisfied

    @property
    def get_item_wants(self):
        """
        Returns the desired item of the npc
        """
        return self._item_wants

    def recieve(self, given_item):
        """
        when npc recieves an item, this method will take it, and
        check whether it is the item that the npc wants. if it is,
        the npc will become satisfied, if not, npc will remain
        unsatisfied

        Args:
            given_item: item that the npc recieves
        """
        if given_item == self._item_wants:
            self._is_satisfied = True
