"""
File to test controller.py

Functions that we aren't testing:
    init: we are not testing initialization functions, especially since
    we are testing all of the getters that we use in the implementation.
    text_box, world, current_room: all these properties will be tested
    elsewhere as part of other tests.
    clear_text_box, create_text_box: these functions have no return
    check_win: don't know how :((
    check_step: all this function does is call three other functions,
    (made so we didn't have to call each one individually every time),
    and we are testing each of those individually
"""

import pygame
import pytest
from Model.constants import TILE_SIZE
from Model.world_manager import WorldManager
from view import View
from Model.constants import TILE_SIZE
from Model.room import Room
from Model.player import Player
from controller import TopDownController

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

track_portal_cases = [
    (test_play, 0, test_cont.current_room, (0, 0), 0),
    (test_play, 1, test_cont.world.get_room("Green_Forest"), (12, 7), 2),
]


@pytest.mark.parametrize(
    "player, test_num, final_room, final_coords, final_dir", track_portal_cases
)
def test_track_portal(player, test_num, final_room, final_coords, final_dir):
    """
    Tests the track portal function in the controller

    Args:
        player: a Player instance that represents the player's information
        test_num: a number representing which test will be run
        final_room: the room that the player should be in after the test
        final_coords: the coordinates that the player should have after the test
        final_dir: the coordinates that the player should have after the test
    """
    match test_num:
        case 0:
            player.set_coordinates((0, 0))
        case 1:
            player.set_coordinates((320, 32))

    test_cont.track_portal(player)
    assert player.room == final_room
    assert player.coordinates == (
        final_coords[0] * TILE_SIZE,
        final_coords[1] * TILE_SIZE,
    )
    assert player.current_sprite == final_dir
