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
        with open("rooms.json") as rooms:
            parsed_rooms = json.load(rooms)

        portals_json = parsed_rooms["portals"]
        npc_json = parsed_rooms["npcs"]
        item_json = parsed_rooms["items"]

        real_portal = []

        for portal in portals_json:
            real_portal += [json.loads(portal)]

        real_npcs = []

        for npc in npc_json:
            real_npcs += [json.loads(npc)]

        real_items = []

        for item in item_json:
            real_items += [json.loads(item)]

        test_room = Room(
            parsed_rooms["name"],
            parsed_rooms["filepath"],
            real_portal,
            real_npcs,
            real_items,
        )

    # get room by name function