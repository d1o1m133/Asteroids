import pygame
import sys
from shot import Shot
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    # 1. Create two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Create a group to hold all asteroid sprites
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    
    
    # 2. Set the groups as containers for the Player
    Player.containers = (updatable, drawable)
    # Set up containers for Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    # Create the player after setting the containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    game_loop = True
    while game_loop == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3a. Update all updatables
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()
        
        
        screen.fill("black")
        
        # 3b. Draw all drawables
        for drawable_object in drawable:
            drawable_object.draw(screen)
            
        pygame.display.flip()

        elapsed_time = clock.tick(60) 
        dt = elapsed_time / 1000

if __name__ == "__main__":
    main()