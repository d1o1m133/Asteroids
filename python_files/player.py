import pygame
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
from constants import PLAYER_SHOOT_SPEED

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__( x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):

        if self.shoot_timer <= 0:
            # Your existing shooting code here (creating bullets, etc.)
            # Reset the timer to the cooldown period
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            # Assuming the triangle points upward at 0 rotation
            # Get the vertices of the triangle
            vertices = []
            
            # Front vertex (the tip)
            front = pygame.Vector2(0, -self.radius)
            front.rotate_ip(self.rotation)
            front_pos = self.position + front
            
            # Create shot at front vertex
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            Shot(front_pos, velocity)
            
            # Optional debugging - draw a dot at the calculated tip position
            # pygame.draw.circle(screen, (255, 0, 0), (int(front_pos.x), int(front_pos.y)), 3)