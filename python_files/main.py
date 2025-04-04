import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_loop = True
    while game_loop == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    screen.fill("black")
    pygame.display.flip()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")






if __name__ == "__main__":
    main()