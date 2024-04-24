import pygame
import Model
import Model.player
import Model.character
from controller import TopDownController


class Mover:

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def change_x(self, new):
        self.x = new

    def change_y(self, new):
        self.y = new

    def move_left(self):
        self.x = self.x - 1

        # print(f"({self.x}, {self.y})")

    def move_right(self):
        self.x = self.x + 1

        # print(f"({self.x}, {self.y})")

    def move_up(self):
        self.y = self.y + 1

        # print(f"({self.x}, {self.y})")

    def move_down(self):
        self.y = self.y - 1

        # print(f"({self.x}, {self.y})")

    def move_diagpos(self):
        self.x = self.x + 1
        self.y = self.y + 1

        # print(f"({self.x}, {self.y})")

    def move_diagneg(self):
        self.x = self.x - 1
        self.y = self.y - 1

        # print(f"({self.x}, {self.y})")


pygame.init()

WIDTH = 1000
HEIGHT = 800

user = Model.character.Character(
    [
        "sprite_up32.png",
        "sprite_right32.png",
        "sprite_down32.png",
        "sprite_left32.png",
    ],
    3,
    None,
    "coco",
    (0, 0),
    "basement",
    ["sprite_left32.png"],
)

tdc = TopDownController()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
imp = user.get_sprite_list()[3]
screen.blit(imp, (0, 0))
pygame.display.flip()

RUN = True

while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_LEFT:
                    tdc.move_left(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("LEFT")
                case pygame.K_RIGHT:
                    tdc.move_right(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("RIGHT")
                case pygame.K_UP:
                    tdc.move_up(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("UP")
                case pygame.K_DOWN:
                    tdc.move_down(user)
                    imp = user.get_sprite_list()[user.get_current_sprite()]
                    screen.fill((0, 0, 0))
                    screen.blit(imp, user.coordinates)
                    pygame.display.flip()
                    print("DOWN")


pygame.quit()
