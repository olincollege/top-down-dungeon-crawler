"""controller.py contains the class that controls the player
and it's interactions"""

from Model.tile import Portal, Item
from Model.player import Player
from Model.world_manager import WorldManager

TILE_HEIGHT = 32
TILE_WIDTH = 32


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items
    """

    def __init__(self):
        self._world = WorldManager()
        self._current_room = self._world.get_room("Tent_Interior")

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
        tile = player.check_step()
        if isinstance(tile, Portal):
            self._current_room = self._world.get_room(tile.dest_room)
            player.set_room(self._current_room)
            player.set_coordinates(
                (tile.dest_coords[0] * 32, tile.dest_coords[1] * 32)
            )
        elif isinstance(tile, Item):
            player.pick_up(tile)
            tile.set_player_has = True

    def move_left(self, player=Player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """

        player_coordinates = player.coordinates

        player.set_pos((player_coordinates[0] - 1, player_coordinates[1]))
        print(f"xpos = {player.pos[0]}, ypos = {player.pos[1]}")
        print(f"Checking collision, it is {player.check_collision()}")

        if player.check_collision():
            player.set_pos((player_coordinates[0] + 1, player_coordinates[1]))

        player.set_current_sprite(3)

        new_pos = player.pos

        player.set_rect(new_pos)

        self.track_step(player)

    def move_right(self, player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        player_coordinates = player.coordinates

        player.set_pos((player_coordinates[0] + 1, player_coordinates[1]))
        print(f"xpos = {player.pos[0]}, ypos = {player.pos[1]}")

        print(f"Checking collision, it is {player.check_collision()}")
        if player.check_collision():
            print("COLLISION!!!")
            player.set_pos((player_coordinates[0] - 1, player_coordinates[1]))

        player.set_current_sprite(1)

        new_pos = player.pos

        player.set_rect(new_pos)

        self.track_step(player)

    def move_down(self, player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        player_coordinates = player.coordinates
        player.set_pos((player_coordinates[0], player_coordinates[1] + 1))
        print(f"xpos = {player.pos[0]}, ypos = {player.pos[1]}")
        print(f"Checking collision, it is {player.check_collision()}")
        if player.check_collision():
            print("COLLISION!!!")
            player.set_pos((player_coordinates[0], player_coordinates[1] - 1))

        player.set_current_sprite(2)

        new_pos = player.pos

        player.set_rect(new_pos)

        self.track_step(player)

    def move_up(self, player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        player_coordinates = player.coordinates

        player.set_pos((player_coordinates[0], player_coordinates[1] - 1))
        print(f"xpos = {player.pos[0]}, ypos = {player.pos[1]}")
        print(f"Checking collision, it is {player.check_collision()}")
        if player.check_collision():
            print("COLLISION!!!")
            player.set_pos((player_coordinates[0], player_coordinates[1] + 1))

        player.set_current_sprite(0)

        new_pos = player.pos

        player.set_rect(new_pos)

        self.track_step(player)
