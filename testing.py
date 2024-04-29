import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, TILE_SIZE

pygame.init()


screen = pygame.display.set_mode(
    (SCREEN_WIDTH * TILE_SIZE, SCREEN_HEIGHT * TILE_SIZE)
)
screen.fill((255, 255, 255))
pygame.display.flip()


def create_text(text):
    font = pygame.font.SysFont("Comic Sans MS", 32)
    text_surf = pygame.font.Font.render(
        font, text, False, (255, 255, 255), (0, 0, 0)
    )
    new_surf = pygame.Surface(
        (SCREEN_WIDTH * TILE_SIZE, SCREEN_HEIGHT * TILE_SIZE)
    )
    return (text_surf, new_surf)


RUN = True

while RUN:
    for event in pygame.event.get():
        # kill program on exit
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUN = False
            if event.key == pygame.K_SPACE:
                text = create_text("Hi there! Can you bring me some manure?")
                screen.blit(text[1], (0, 0))
                x = text[0].get_width()
                screen.blit(
                    text[0],
                    (
                        (SCREEN_WIDTH * TILE_SIZE - x) // 2,
                        SCREEN_HEIGHT * TILE_SIZE // 2,
                    ),
                )
                pygame.display.flip()
            if event.key == pygame.K_x:
                screen.fill((255, 255, 255))
                pygame.display.flip()
