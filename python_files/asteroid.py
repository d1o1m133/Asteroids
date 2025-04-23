from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update position based on velocity and time elapsed
        self.position += self.velocity * dt