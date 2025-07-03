import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'green', self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius
        elif self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius
        elif self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
