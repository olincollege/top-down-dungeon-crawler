"""controller.py contains the class that controls the player
and it's interactions"""

from Model.tile import Portal, Item
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

    def track_step(self, player=Player):
        """
        Changes the current room a player is in based on the portal
        they entered

        Args:
            player: a Player instance representing the player's information
            portal: a Portal instance that represents the portal's information
        """

        portals = self.current_room.portal_list
        room_items = self.current_room.item_list

        for portal in portals:
            temp_portal_coords = portal.coordinates
            if player.coordinates == temp_portal_coords:
                self._current_room = self._world.get_room(portal.dest_room)
                player.set_room(self._current_room)
                player.set_coordinates(portal.dest_coords)

        for item in room_items:
            temp_item_coords = item.coordinates
            if player.coordinates == temp_item_coords:
                player.pick_up(item)
                # remove item from room item list and tile group

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

        self.track_step(player)

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

        self.track_step(player)

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

        self.track_step(player)

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

        self.track_step(player)
