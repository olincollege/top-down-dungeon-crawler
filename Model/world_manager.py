"""
e
"""

import json
from Model.room import Room


class WorldManager:
    """
    e
    """

    def __init__(self):
        # load in json and create a room for each object
        # use properties to fill room parameters
        # may need to update room.py to accept a jsonobject for items,
        # portals, etc and process those in the room.py file
        # should possess a dictionary of each room name + room instance

        self._room_list = {}

        with open("Resources/JSON/rooms.json") as rooms:
            parsed_rooms = json.load(rooms)

        for room_name, room_data in parsed_rooms.items():

            portals_json = room_data["portals"]
            npc_json = room_data["npcs"]
            item_json = room_data["items"]

            self._room_list[room_name] = Room(
                name=room_name,
                filepath=room_data["filepath"],
                portals=portals_json,
                npcs=npc_json,
                items=item_json,
            )

    # get room by name function
    def get_room(self, name):
        """
        Args:
            name: String representing the name of a room.
        """
        return self._room_list[name]
