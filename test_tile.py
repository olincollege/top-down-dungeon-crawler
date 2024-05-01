"""
Tests the methods in the tile.py file
"""

import pygame
import pytest
from Model.player import Player
from Model.tile import NPC, Item
from controller import TopDownController
from view import View


pygame.init()
view = View()


test_cont = TopDownController()
test_play = Player(
    [
        "Resources/Player Images/red_up_32.png",
        "Resources/Player Images/red_right_32.png",
        "Resources/Player Images/red_down_32.png",
        "Resources/Player Images/red_left_32.png",
    ],
    0,
    "Coco",
    (0, 0),
    test_cont.current_room,
)

test_item = Item(
    "silver_coin",
    (0, 0),
    pygame.sprite.Group(),
    pygame.image.load("Resources/npc_images/npc_male.png"),
)

test_npc = NPC(
    ["before", "current", "after"],
    "silver_coin",
    pygame.image.load("Resources/npc_images/npc_male.png"),
    pygame.sprite.Group(),
    "Felix",
    (0, 0),
)

test_cases = [(test_npc, test_play, test_item)]


@pytest.mark.parametrize("npc, player, item", test_cases)
def test_det_voice(npc, player, item):
    """
    Tests the det_voice method in the NPC class of tile.py

    Only testing the 'before' test because to update the state of the 
    npc the player has to interact with it in a way that can not be done
    in a unit test
    """
    player.pick_up(item)
    voice_line = npc.det_voice(player)
    assert voice_line == "before"
