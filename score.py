import pygame
from constants import *


class Score():
    def __init__(self):
        self.total = 0
        self.multiplier = 1
        self.font = pygame.font.SysFont('Arial', 40, bold=True)
    
    def __str__(self):
        return f'Score: {self.total}    {"Multiplier Activated!" if self.multiplier > 1 else ""}'

    def increase_score(self):
        self.total += 1 * self.multiplier

    def reset_score(self):
        self.total = 0

    def render(self, screen):
        color = 'white' if self.multiplier == 1 else 'purple'
        surface = self.font.render(self.__str__(), True, color)
        screen.blit(surface, (SCORE_X, SCORE_Y))
