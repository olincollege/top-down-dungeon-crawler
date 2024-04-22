import pygame


class Mover:

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    @property
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

user = Mover(0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RUN = True

while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         user.move_left()
        #     if event.key == pygame.K_RIGHT:
        #         user.move_right()
        #     if event.key == pygame.K_UP:
        #         user.move_up()
        #     if event.key == pygame.K_DOWN:
        #         user.move_down()
        #     if event.key == pygame.K_1:
        #         user.move_diagpos()
        #     if event.key == pygame.K_2:
        #         user.move_diagneg()
        if event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_LEFT:
                    user.move_left()
                    print("LEFT")
                case pygame.K_RIGHT:
                    user.move_right()
                    print("RIGHT")
                case pygame.K_UP:
                    user.move_up()
                    print("UP")
                case pygame.K_DOWN:
                    user.move_down()
                    print("DOWN")
                case pygame.K_1:
                    user.move_diagpos()
                    print("DIAGONAL POSITIVE")
                case pygame.K_2:
                    user.move_diagneg()
                    print("DIAGONAL NEGATIVE")


pygame.quit()
