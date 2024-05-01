"""
Tests the methods in the room.py file

****
Below, we set up the code to run a pytest. However, there
were issues when setting up the pytest and it would not function. 
We contacted CAs about this issue and no one was able to figure out
the issue. We left the code here, but commented out the test itself.
If the grader understands what the issue is please let us know



"""
from json import load

# import pytest
import pygame
from Model.room import Room
from Model.tile import Item
from controller import TopDownController
from view import View

pygame.init()
view = View()
test_cont = TopDownController()

with open("Resources/JSON/rooms.json", encoding="utf-8") as rooms:
    parsed_rooms = load(rooms)

room_data = parsed_rooms["Barn_Interior"]
portals_json = room_data["portals"]
npc_json = room_data["npcs"]
item_json = room_data["items"]


test_room = Room(
    name="Barn_Interior",
    filepath=room_data["filepath"],
    portals=portals_json,
    npcs=npc_json,
    items=item_json,
)

test_item = Item(
    "silver_coin",
    (0, 0),
    pygame.sprite.Group(),
    pygame.image.load("Resources/npc_images/npc_male.png"),
)


test_cases = [test_room, test_item]
# @pytest.mark.parametrize("room, item", test_cases)
# def test_remove_item(room, item):
#     """
#     e
#     """
#     room.remove_item(item)
#     assert item.name not in room.item_list
