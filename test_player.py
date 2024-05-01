"""
Tests the methods from player.py

We will not be testing the following functions:

init: we are not testing initialization functions.
name, room, coordinates, sprite_list, current_sprite, inventory:
all of these are properties and therefore unnecessary to test.
set_room, set_coordinates, set_current_sprite: these are setters
and only have one line of code, so are also unnecessary to test.
check_npc_coords: this function returns a NPC object, which are too
unique to compare.
check_collision: this function requires a list of initialized tiles,
which is too difficult to create.
"""

import pytest
import pygame
from Model.constants import TILE_SIZE
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

update_mvmt_cases = [
    # Direction changes with no x or y change (collided)
    (test_play, 0, 2, 0, 0),
    # x (or y) change with no direction change
    (test_play, 1, 0, TILE_SIZE, 0),
    # x (or y) change with direction change
    (test_play, 2, 1, TILE_SIZE, 0),
]


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_pick_up(player, item):
    """
    Tests the pick_up method in the Player class

    Args:
        item: an Item instance representing the item to be picked up.
    """
    player.pick_up(item)
    inv_items = player.inventory
    assert item.name in inv_items


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_give(player, item):
    """
    Tests the give method in the Player class

    Args:
        item: an Item instance representing the item to be picked up.
    """
    player.give(item.name)

    assert item.name not in player.inventory


@pytest.mark.parametrize("player, item", pick_up_cases)
def test_list_inventory(player, item):
    """
    Tests the list_inventory method in the Player class

    Args:
        item: an Item instance representing the item to be picked up.
    """
    player.pick_up(item)
    assert player.list_inventory() == "Current Inventory: " + item.name


@pytest.mark.parametrize(
    "player, test_case, player_dir, x_move, y_move", update_mvmt_cases
)
def test_update_movement(player, test_case, player_dir, x_move, y_move):
    """
    Tests the update movement function in player

    Args:
        player: a Player instance that holds all the player's information
        test_case: an int representing which test will be run
        dir: an int representing the next direction of the player
        x_move: an int representing the x-change of the player
        y_move: an int representing the y-change of the player
    """
    player.set_current_sprite(0)
    player.set_coordinates((0, 0))
    final_dir = 0
    final_coords = (0, 0)
    match test_case:
        case 0:
            final_dir = 2
        case 1:
            final_coords = (TILE_SIZE, 0)
        case 2:
            final_dir = 1
            final_coords = (TILE_SIZE, 0)

    player.update_movement(player_dir, x_move, y_move)
    assert player.current_sprite == final_dir
    assert player.coordinates == final_coords
