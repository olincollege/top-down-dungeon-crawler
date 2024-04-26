"""controller.py contains the class that controls the player
and it's interactions"""

TILE_HEIGHT = 32
TILE_WIDTH = 32


class TopDownController:
    """
    Controls the player and the player's interactions with NPCs and items
    """

    def __init__(self):
        pass

    def change_room(self, player, portal):
        """
        Changes the current room a player is in based on the portal
        they entered

        Args:
            player: a Player instance representing the player's information
            portal: a Portal instance that represents the portal's information
        """
        next_room = portal.get_dest_room
        player.set_room(next_room)

    def move_left(self, player):
        """
        Moves the player left

        Args:
            player: a Player instance representing the player's information
        """
        if not player.check_collision(3):

            player_coords = player.coordinates

            player.set_coordinates(
                player_coords[0] - TILE_WIDTH, player_coords[1]
            )

            player.set_current_sprite(3)

            new_coords = player.coordinates

            player.set_rect(new_coords)

    def move_right(self, player):
        """
        Moves the player right

        Args:
            player: a Player instance representing the player's information
        """
        if not player.check_collision(1):
            player_coords = player.coordinates

            player.set_coordinates(
                player_coords[0] + TILE_WIDTH, player_coords[1]
            )

            player.set_current_sprite(1)

            new_coords = player.coordinates

            player.set_rect(new_coords)

    def move_down(self, player):
        """
        Moves the player down

        Args:
            player: a Player instance representing the player's information
        """
        if not player.check_collision(2):
            player_coords = player.coordinates
            player.set_coordinates(
                player_coords[0], player_coords[1] + TILE_HEIGHT
            )

            player.set_current_sprite(2)

            new_coords = player.coordinates

            player.set_rect(new_coords)

    def move_up(self, player):
        """
        Moves the player up

        Args:
            player: a Player instance representing the player's information
        """
        if not player.check_collision(0):
            player_coords = player.coordinates

            player.set_coordinates(
                player_coords[0], player_coords[1] - TILE_HEIGHT
            )

            player.set_current_sprite(0)

            new_coords = player.coordinates

            player.set_rect(new_coords)
