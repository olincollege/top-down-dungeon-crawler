"""
tests the methods from player.py
"""

import pytest
import pygame
from Model.player import Player
from Model.tile import Item
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

pick_up_cases = [(test_play, test_item)]


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_pick_up(player, item):
    """
    tests the pick_up method in the Player class
    """
    player.pick_up(item)
    inv_items = player.inventory
    assert item.name in inv_items


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_give(player, item):
    """
    tests the give method in the Player class
    """
    player.give(item.name)

    assert item.name not in player.inventory


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_list_inventory(player, item):
    """
    tests the list_inventory method in the Player class
    """
    player.pick_up(item)
    assert player.list_inventory() == "Current Inventory: " + item.name
