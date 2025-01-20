import pygame
from circleshape import CircleShape
from constants import RED_COLOR


class Heart(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, RED_COLOR, (int(self.position.x), int(self.position.y)), self.radius
        )
