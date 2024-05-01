"""controller.py contains the class that controls the player
and its interactions"""

import pygame
from Model.constants import TILE_SIZE
from Model.world_manager import WorldManager
from Model.player import Player

TILE_SIZE = 32


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items

    Attributes:
        _world: a WorldManager instance that creates the world
        _current_room: a Room instance that represents the room the player
        is currently in
        _text_box: either a pygame Surface or None, representing whether or
        not there is a text box being displayed currently
        _instruct: an int representing which piece of information the
        instructions method should display
        _has_won: a Boolean representing whether or not the player
        has satisfied the win condition
    """

    def __init__(self):
        """
        Initializes an instance of a TopDownController
        """
        self._world = WorldManager()
        self._current_room = self._world.get_room("Tent_Interior")
        self._text_box = None
        self._instruct = 0  # Internal only
        self._has_won = False  # Internal only

    @property
    def text_box(self):
        """
        Getter for the text box attribute.

        Returns the self._text_box attribute.
        """
        return self._text_box

    @property
    def world(self):
        """
        Getter for the world attribute.

        Returns the self._world attribute.
        """
        return self._world

    @property
    def current_room(self):
        """
        Getter for the current room attribute.

        Returns the self._current_room attribute.
        """
        return self._current_room

    def clear_text_box(self):
        """
        Sets text box attribute to None.
        """
        self._text_box = None

    def create_textbox(self, samp_text):
        """
        Creates a textbox and updates the text box attribute.

        Args:
            samp_text: a string representing the text to be written
        """
        # Create Font object
        font = pygame.font.SysFont("Comic Sans MS", 32)

        # Render text onto font
        text_surf = pygame.font.Font.render(
            font, samp_text, False, (255, 255, 255), (0, 0, 0)
        )

        # Set text box attribute to rendered text
        self._text_box = text_surf

    def track_portal(self, player=Player):
        """
        Checks if a player stepped on a portal, and changes the current room
        a player is in based on the portal they entered

        Args:
            player: a Player instance representing the player's information
        """
        # Gets list of portals in the current room
        portals = self.current_room.portal_list

        for portal in portals:
            temp_portal_coords = portal.coordinates
            # Checks if the player and the portal are in the same place
            if player.coordinates == temp_portal_coords:
                self._current_room = self._world.get_room(portal.dest_room)
                # Changes the current room
                player.set_room(self._current_room)
                # Sets the player's coordinates to the coordinates of the
                # destination portal
                player.set_coordinates(portal.dest_coords)
                # Makes sure the player is facing the right way
                print(player.current_sprite)
                player.set_current_sprite(portal.dest_dir)
                print(player.current_sprite)

    def track_item(self, player=Player):
        """
        Checks if the player stepped on an item and picks it up

        Args:
            player: a Player instance representing the player's information
        """
        # Gets list of items in current room
        room_items = self.current_room.item_list

        for item in room_items:
            temp_item_coords = item.coordinates
            print(f"item coords {temp_item_coords}")
            # Checks if the player and the item are in the same place
            if player.coordinates == temp_item_coords:
                print(f"Picking up item at {temp_item_coords}")
                # Adds item to player's inventory
                player.pick_up(item)
                # Removes item from Room instance
                self.current_room.remove_item(item)
                # Displays text
                self.create_textbox(f"You picked up: {item.name}!")

    def check_win(self):
        """
        Checks if the player has won - i.e., satisfied all NPCs.

        Returns a Boolean that represents if the player has won
        or not.
        """
        # Tracks how many NPCs are satisfied
        npcs_satisfied = 0
        for npc in self._world.get_world_npcs():
            if npc.is_satisfied:
                npcs_satisfied += 1
        # Checks if the number satisfied is equal to the number of NPCs in the
        # world
        if npcs_satisfied == len(self._world.get_world_npcs()):
            return True
        return False

    def check_step(self, player=Player):
        """
        Calls both track_portal and track_item, and checks if
        the player has won.

        Made for convenience - all three functions are called together often.

        Args:
            player: a Player instance representing the player's information
        """
        self.track_item(player)
        self.track_portal(player)

        # Makes sure that the textbox only displays once by checking if
        # self._has_won is False, and then setting it to True once the player
        # wins.
        if self.check_win() and not self._has_won:
            self.create_textbox(
                "You win! Press X to continue exploring, or Escape to exit."
            )
            self._has_won = True

    def move_left(self, player=Player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """
        # Checks if there is a textbox
        if self._text_box is None:
            # Checks for collisions
            if player.check_collision(3, self.current_room.get_all_collide()):
                player.update_movement(3, 0, 0)
            else:
                player.update_movement(3, -TILE_SIZE, 0)
            # Checks if the new position is on a portal or item
            self.check_step(player)

    def move_right(self, player=Player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        # Checks if there is a textbox
        if self._text_box is None:
            # Checks for collisions
            if player.check_collision(1, self.current_room.get_all_collide()):
                player.update_movement(1, 0, 0)
            else:
                player.update_movement(1, TILE_SIZE, 0)
            # Checks if the new position is on a portal or item
            self.check_step(player)

    def move_down(self, player=Player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        # Checks if there is a textbox
        if self._text_box is None:
            # Checks for collisions
            if player.check_collision(2, self.current_room.get_all_collide()):
                player.update_movement(2, 0, 0)
            else:
                player.update_movement(2, 0, TILE_SIZE)
            # Checks if the new position is on a portal or item
            self.check_step(player)

    def move_up(self, player=Player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        # Checks if there is a textbox
        if self._text_box is None:
            # Checks for collisions
            if player.check_collision(0, self.current_room.get_all_collide()):
                player.update_movement(0, 0, 0)
            else:
                player.update_movement(0, 0, -TILE_SIZE)
            # Checks if the new position is on a portal or item
            self.check_step(player)

    def instruct(self):
        """
        Creates instruction textboxes.

        Displays a different set of instructions (out of 4 possible),
        depending on the self._instruct attribute.
        """
        # Creates number from 0-4
        num_instruct = self._instruct % 5

        # Finds what instructions should be displayed and updates self._instruct
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
            case 4:
                self.create_textbox("Escape to exit - press Q again for more!")
                self._instruct += 1
