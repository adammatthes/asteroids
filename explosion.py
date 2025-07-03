import pygame
from constants import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.center_x = x
        self.center_y = y
        self.radius = 5
        self.max_radius = 50
        self.growth_speed = 2
        self.alpha = 255
        self.fade_speed = 10
        self.finished = False

        radii_val = self.max_radius * 2
        self.image = pygame.Surface((radii_val, radii_val), pygame.SRCALPHA)
        self.rectangle = self.image.get_rect(center=(self.center_x, self.center_y))

    def update(self, dt):
        if self.finished:
            self.kill()
            return

        self.radius += self.growth_speed
        if self.radius > self.max_radius:
            self.radius = self.max_radius

        self.alpha -= self.fade_speed
        if self.alpha <= 0:
            self.alpha = 0
            self.finished = True

        self.image.fill((0, 0, 0, 0))

        alpha_modifier = self.alpha / 255
        current_color = (
            int(RED[0] * alpha_modifier),
            int(RED[1] * alpha_modifier),
            int(RED[2] * alpha_modifier),
            self.alpha
        )

        alpha_yellow = YELLOW + (self.alpha,)
        alpha_orange = ORANGE + (self.alpha,)
        max_radii = (self.max_radius, self.max_radius)
        pygame.draw.circle(self.image, alpha_yellow, max_radii, int(self.radius * 0.6))
        pygame.draw.circle(self.image, alpha_orange, max_radii, int(self.radius * 0.8), 2)
        pygame.draw.circle(self.image, current_color, max_radii, int(self.radius))

    def draw(self, surface):
        if not self.finished:
            surface.blit(self.image, self.rectangle)


class ExplosionManager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)

    def update(self, dt):
        new_explosion = Explosion(dt, dt)

    def draw(self, screen):
        pass

