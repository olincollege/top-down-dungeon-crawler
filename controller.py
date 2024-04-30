"""controller.py contains the class that controls the player
and it's interactions"""

import pygame
from constants import TILE_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from Model.player import Player
from Model.world_manager import WorldManager

TILE_SIZE = 32


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items
    """

    def __init__(self):
        self._world = WorldManager()
        self._current_room = self._world.get_room("Tent_Interior")
        self._text_box = None
        self._instruct = 0

    @property
    def text_box(self):
        """
        Getter for the text box
        """
        return self._text_box

    @property
    def world(self):
        """
        Getter for the world attribute.
        """
        return self._world

    @property
    def current_room(self):
        """
        Getter for the current room.
        """
        return self._current_room

    def clear_text_box(self):
        """
        Sets text box attribute to None
        """
        self._text_box = None

    def create_textbox(self, samp_text):
        """
        Creates a textbox.

        Args:
            samp_text: a string representing the text to be written
        """
        font = pygame.font.SysFont("Comic Sans MS", 32)
        text_surf = pygame.font.Font.render(
            font, samp_text, False, (255, 255, 255), (0, 0, 0)
        )
        self._text_box = text_surf

    def track_portal(self, player=Player):
        """
        Checks if a player stepped on a portal, and changes the current room
        a player is in based on the portal they entered

        Args:
            player: a Player instance representing the player's information
        """

        portals = self.current_room.portal_list

        for portal in portals:
            temp_portal_coords = portal.coordinates
            if player.coordinates == temp_portal_coords:
                self._current_room = self._world.get_room(portal.dest_room)
                player.set_room(self._current_room)
                player.set_coordinates(portal.dest_coords)
                player.set_current_sprite(portal.dest_dir)

    def track_item(self, player=Player):
        """
        Checks if the player stepped on an item and picks it up

        Args:
            player: a Player instance representing the player's information
        """
        room_items = self.current_room.item_list

        for item in room_items:
            temp_item_coords = item.coordinates
            if player.coordinates == temp_item_coords:
                player.pick_up(item)
                self.current_room.remove_item(item)
                self.create_textbox(f"You picked up: {item.name}!")

    def check_step(self, player=Player):
        """
        Calls both track_portal and track_item

        Made for convenience - both are called together often.

        Args:
            player: a Player instance representing the player's information
        """
        self.track_item(player)
        self.track_portal(player)

    def move_left(self, player=Player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """
        if self._text_box is None:
            if player.check_collision(3, self.current_room.get_all_collide()):
                player.update_movement(3, 0, 0)
            else:
                player.update_movement(3, -TILE_SIZE, 0)
            self.check_step(player)

    def move_right(self, player=Player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        if self._text_box is None:
            if player.check_collision(1, self.current_room.get_all_collide()):
                player.update_movement(1, 0, 0)
            else:
                player.update_movement(1, TILE_SIZE, 0)
            self.check_step(player)

    def move_down(self, player=Player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        if self._text_box is None:
            if player.check_collision(2, self.current_room.get_all_collide()):
                player.update_movement(2, 0, 0)
            else:
                player.update_movement(2, 0, TILE_SIZE)
            self.check_step(player)

    def move_up(self, player=Player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        if self._text_box is None:
            if player.check_collision(0, self.current_room.get_all_collide()):
                player.update_movement(0, 0, 0)
            else:
                player.update_movement(0, 0, -TILE_SIZE)
            self.check_step(player)

    def instruct(self):
        """
        Creates instruction textboxes
        """
        num_instruct = self._instruct % 4

        match num_instruct:
            case 0:
                self.create_textbox("X to close text - press Q again for more!")
                self._instruct += 1
            case 1:
                self.create_textbox(
                    "Arrow keys to move - press Q again for more!"
                )
                self._instruct += 1
            case 2:
                self.create_textbox(
                    "I to open inventory - press Q again for more!"
                )
                self._instruct += 1
            case 3:
                self.create_textbox(
                    "Space to interact with NPCs - press Q again for more!"
                )
                self._instruct += 1
