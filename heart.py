import pygame
from circleshape import CircleShape


class Heart(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "red", (int(self.position.x), int(self.position.y)), self.radius
        )
