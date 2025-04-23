import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 
        self.radius = radius
        self.rect = pygame.Rect(0, 0, radius * 2, radius * 2)  # Create a bounding box
        self.rect.center = self.position  # Center the rect on the circle's positio

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update position based on velocity and time elapsed
        self.position += self.velocity * dt
        self.rect.center = self.position  # Update rect to match position

    def split(self):
    # Store all the groups before killing the asteroid
        original_groups = self.groups()
        
        # 1. Kill this asteroid
        self.kill()

        # 2. If this is already a small asteroid, don't spawn new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # 4. Create two new velocity vectors by rotating the current one
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        # 5. Calculate the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 6. Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # 7. Set their velocities (making them faster)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2

        # 8. Add them to all the original groups
        for group in original_groups:
            group.add(asteroid1)
            group.add(asteroid2)