import pygame
from circleshape import CircleShape
import math
import random
from constants import *
from explosion import Explosion

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = 'yellow' if random.randint(0, 100) < 95 else 'purple'

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, explosion_group):
        old_radius = self.radius
        old_velocity = self.velocity
        old_position = self.position
        explode = Explosion(self.position.x, self.position.y)
        explosion_group.add(explode)
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vec1, vec2 = old_velocity.rotate(angle), old_velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(old_position.x - new_radius, old_position.y, new_radius)
        ast1.velocity = vec1 * 1.2
        
        ast2 = Asteroid(old_position.x + new_radius, old_position.y, new_radius)
        ast2.velocity = vec2

    def bounce(self, other):
        delta = self.position - other.position
        distance = (delta).length()
        
        n = pygame.Vector2(1, 0) if distance == 0 else (delta).normalize()
        t = n.rotate(90)

        v1n = self.velocity.dot(n)
        v1t = self.velocity.dot(t)

        v2n = other.velocity.dot(n)
        v2t = other.velocity.dot(t)

        v1n_final = v2n
        v2n_final = v1n

        vel1_final = (v1n_final) * n + (v1t * t)
        vel2_final = (v2n_final) * n + (v2t * t)

        self.velocity = vel1_final
        other.velocity = vel2_final
        


