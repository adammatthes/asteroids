import pygame
from circleshape import CircleShape
import math
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = 'yellow' if random.randint(0, 100) < 85 else 'purple'

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_velocity = self.velocity
        old_position = self.position
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vec1, vec2 = old_velocity.rotate(angle), old_velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(old_position.x, old_position.y, new_radius)
        ast1.velocity = vec1 * 1.2
        
        ast2 = Asteroid(old_position.x, old_position.y, new_radius)
        ast2.velocity = vec2


