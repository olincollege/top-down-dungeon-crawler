"""
File to test controller.py

Functions that we aren't testing:
    init: we are not testing initialization functions.
    text_box, world, current_room: all these properties will be tested
    elsewhere as part of other tests.
    clear_text_box, create_text_box: these functions affect Surfaces,
    and it is difficult to check equality with Surfaces
    check_win: this requires two separate world states, and it is
    very difficult to test properly
    check_step: all this function does is call three other functions,
    (made so we didn't have to call each one individually every time),
    and we are testing those individually
    instruct: this function affects Surfaces, and it is difficult to
    check equality with Surfaces
"""

import pygame
import pytest
from Model import constants, player
from view import View
from controller import TopDownController

pygame.init()

view = View()

test_cont = TopDownController()
test_play = player.Player(
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

track_portal_cases = [
    # Not on portal tile
    (test_play, 0, test_cont.current_room, (0, 0), 0),
    # On portal tile
    (test_play, 1, test_cont.world.get_room("Green_Forest"), (12, 7), 2),
]

track_item_cases = [
    # Not on item
    (test_play, 0, []),
    (test_play, 1, ["silver coin"]),
]
# (test_play, 1, ["silver coin"]) - doesn't work??

move_left_cases = [
    # No collisions or textboxes
    (test_play, 0, None),
    # Collision with no textbox
    (test_play, 1, None),
    # Textbox with no collision
    (test_play, 2, "a"),
    # Both textbox and collision
    (test_play, 3, "a"),
]

move_right_cases = [
    # No collisions or textboxes
    (test_play, 0, None),
    # Collision with no textbox
    (test_play, 1, None),
    # Textbox with no collision
    (test_play, 2, "a"),
    # Both textbox and collision
    (test_play, 3, "a"),
]

move_up_cases = [
    # No collisions or textboxes
    (test_play, 0, None),
    # Collision with no textbox
    (test_play, 1, None),
    # Textbox with no collision
    (test_play, 2, "a"),
    # Both textbox and collision
    (test_play, 3, "a"),
]

move_down_cases = [
    # No collisions or textboxes
    (test_play, 0, None),
    # Collision with no textbox
    (test_play, 1, None),
    # Textbox with no collision
    (test_play, 2, "a"),
    # Both textbox and collision
    (test_play, 3, "a"),
]


@pytest.mark.parametrize("test_player, test_num, player_inv", track_item_cases)
def test_track_item(test_player, test_num, player_inv):
    """
    Tests the track item function in the controller to make sure the
    player has the correct inventory after the test

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        player_inv: a list of strings representing the expected state of
        the player's inventory after the test
    """
    match test_num:
        case 1:
            test_player.set_coordinates((32, 64))
        case 0:
            test_player.set_coordinates((0, 0))
    test_cont.track_item(test_player)
    assert test_player.inventory == player_inv


@pytest.mark.parametrize("test_player, test_num, text_box", move_left_cases)
def test_move_left(test_player, test_num, text_box):
    """
    Tests the move left function in controller

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        text_box: a string representing the textbox, or None if there is none
    """
    test_cont.clear_text_box()
    final_coords = (0, 0)
    match test_num:
        case 0:
            test_player.set_coordinates((96, 512))
            final_coords = (64, 512)
        case 1:
            test_player.set_coordinates((32, 512))
            final_coords = (32, 512)
        case 2:
            test_player.set_coordinates((96, 512))
            test_cont.create_textbox(text_box)
            final_coords = (96, 512)
        case 3:
            test_player.set_coordinates((32, 512))
            test_cont.create_textbox(text_box)
            final_coords = (32, 512)
    test_cont.move_left(test_player)
    assert test_player.coordinates == final_coords


@pytest.mark.parametrize("test_player, test_num, text_box", move_right_cases)
def test_move_right(test_player, test_num, text_box):
    """
    Tests the move right function in controller

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        text_box: a string representing the textbox, or None if there is none
    """
    test_cont.clear_text_box()
    final_coords = (0, 0)
    match test_num:
        case 0:
            test_player.set_coordinates((96, 512))
            final_coords = (128, 512)
        case 1:
            test_player.set_coordinates((320, 512))
            final_coords = (320, 512)
        case 2:
            test_player.set_coordinates((96, 512))
            test_cont.create_textbox(text_box)
            final_coords = (96, 512)
        case 3:
            test_player.set_coordinates((320, 512))
            test_cont.create_textbox(text_box)
            final_coords = (320, 512)
    test_cont.move_right(test_player)
    assert test_player.coordinates == final_coords


@pytest.mark.parametrize("test_player, test_num, text_box", move_up_cases)
def test_move_up(test_player, test_num, text_box):
    """
    Tests the move up function in controller

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        text_box: a string representing the textbox, or None if there is none
    """
    test_cont.clear_text_box()
    final_coords = (0, 0)
    match test_num:
        case 0:
            test_player.set_coordinates((256, 544))
            final_coords = (256, 512)
        case 1:
            test_player.set_coordinates((64, 64))
            final_coords = (64, 64)
        case 2:
            test_player.set_coordinates((224, 512))
            test_cont.create_textbox(text_box)
            final_coords = (224, 512)
        case 3:
            test_player.set_coordinates((64, 64))
            test_cont.create_textbox(text_box)
            final_coords = (64, 64)
    test_cont.move_up(test_player)
    assert test_player.coordinates == final_coords


@pytest.mark.parametrize("test_player, test_num, text_box", move_down_cases)
def test_move_down(test_player, test_num, text_box):
    """
    Tests the move down function in controller

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        text_box: a string representing the textbox, or None if there is none
    """
    test_cont.clear_text_box()
    final_coords = (0, 0)
    match test_num:
        case 0:
            test_player.set_coordinates((96, 544))
            final_coords = (96, 576)
        case 1:
            test_player.set_coordinates((96, 576))
            final_coords = (96, 576)
        case 2:
            test_player.set_coordinates((224, 512))
            test_cont.create_textbox(text_box)
            final_coords = (224, 512)
        case 3:
            test_player.set_coordinates((96, 576))
            test_cont.create_textbox(text_box)
            final_coords = (96, 576)
    test_cont.move_down(test_player)
    assert test_player.coordinates == final_coords


@pytest.mark.parametrize(
    "test_player, test_num, final_room, final_coords, final_dir",
    track_portal_cases,
)
def test_track_portal(
    test_player, test_num, final_room, final_coords, final_dir
):
    """
    Tests the track portal function in the controller

    Args:
        player: a Player instance that represents the player's information
        test_num: an int representing which test will be run
        final_room: the room that the player should be in after the test
        final_coords: the coordinates that the player should have after the test
        final_dir: the coordinates that the player should have after the test
    """
    match test_num:
        case 0:
            test_player.set_coordinates((0, 0))
            test_player.set_current_sprite(0)
        case 1:
            test_player.set_coordinates((320, 32))
            test_player.set_current_sprite(0)

    test_cont.track_portal(test_player)
    assert test_player.room == final_room
    assert test_player.coordinates == (
        final_coords[0] * constants.TILE_SIZE,
        final_coords[1] * constants.TILE_SIZE,
    )
    assert test_player.current_sprite == final_dir
