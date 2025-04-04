import pygame
from player import Player
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")


    game_loop = True
    while game_loop == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        player.update(dt)

        screen.fill("black")
        player.draw(screen) #draw the player
        pygame.display.flip()

        elapsed_time = clock.tick(60) 
        dt = elapsed_time / 1000


    





if __name__ == "__main__":
    main()