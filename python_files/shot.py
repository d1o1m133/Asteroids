import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
        # Create a bounding box (rect) for the shot
        self.rect = pygame.Rect(0, 0, SHOT_RADIUS * 2, SHOT_RADIUS * 2)
        self.rect.center = (position.x, position.y)  # Initialize rect position

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)


    def update(self, dt):
        distance = self.velocity * dt
        self.position += distance  # Corrected from self.poisiton
        self.rect.center = (int(self.position.x), int(self.position.y))
