"""
This file contains the WorldManager class, which manages all of the rooms
to make sure that instances of Rooms never diverge from each other.
"""

from json import load
from Model.room import Room


class WorldManager:
    """
    The world of the game, including all existing rooms.

    Attributes:
        _room_list: A dictionary in which the keys are the names of all
        Rooms in the game, and the values are the Room objects.
    """

    def __init__(self):
        """
        Initializes an instance of the WorldManager class.
        """
        # create an empty dictionary for rooms
        self._room_list = {}

        # load in json file as a variable
        with open("Resources/JSON/rooms.json", encoding="utf-8") as rooms:
            parsed_rooms = load(rooms)

        # for each room in the parsed json room dictionary
        for room_name, room_data in parsed_rooms.items():
            # load in special objects
            portals_json = room_data["portals"]
            npc_json = room_data["npcs"]
            item_json = room_data["items"]

            # initialize a room and add it to the dictionary
            self._room_list[room_name] = Room(
                name=room_name,
                filepath=room_data["filepath"],
                portals=portals_json,
                npcs=npc_json,
                items=item_json,
            )

    # get room by name
    def get_room(self, name):
        """
        Function to retrieve a particular room from the world.

        Args:
            name: String representing the name of a room.

        Returns: The corresponding Room object.
        """
        return self._room_list[name]

    # get a list of NPCs
    def get_world_npcs(self):
        """
        Returns a list of the world's npcs. The NPCs will be in their active
        state, with all attributes up to date.
        """
        world_npcs = []
        # for each room
        for _, r_object in self._room_list.items():
            # add npcs to total
            temp = r_object.npc_list
            world_npcs += temp
        return world_npcs
