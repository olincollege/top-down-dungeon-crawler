"""controller.py contains the class that controls the player
and it's interactions"""

from Model.player import Player
from Model.world_manager import WorldManager

TILE_SIZE = 32


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items
    """

    def __init__(self):
        self._world = WorldManager()
        self._current_room = self._world.get_room("Green_Forest")

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
                print(
                    f"Player picked up {item.name}! Current inventory: {player.list_inventory()}"
                )

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

        if player.check_collision(3, self.current_room.collide_list):
            print("COLLIDE")
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1])
            )
        else:
            player.set_coordinates(
                (player.coordinates[0] - TILE_SIZE, player.coordinates[1])
            )

        player.set_current_sprite(3)

        player.set_rect(player.coordinates)

        self.check_step(player)

    def move_right(self, player=Player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """

        if player.check_collision(1, self.current_room.collide_list):
            print("COLLIDE")
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1])
            )
        else:
            player.set_coordinates(
                (player.coordinates[0] + TILE_SIZE, player.coordinates[1])
            )

        player.set_current_sprite(1)

        player.set_rect(player.coordinates)

        self.check_step(player)

    def move_down(self, player=Player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """

        if player.check_collision(2, self.current_room.collide_list):
            print("COLLIDE")
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1])
            )
        else:
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1] + TILE_SIZE)
            )

        player.set_current_sprite(2)

        player.set_rect(player.coordinates)

        self.check_step(player)

    def move_up(self, player=Player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """

        if player.check_collision(0, self.current_room.collide_list):
            print("COLLIDE")
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1])
            )
        else:
            player.set_coordinates(
                (player.coordinates[0], player.coordinates[1] - TILE_SIZE)
            )

        player.set_current_sprite(0)

        player.set_rect(player.coordinates)

        self.check_step(player)
