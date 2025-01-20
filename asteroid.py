import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PRIMARY_COLOR


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, PRIMARY_COLOR, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Return points based on asteroid size
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            points = 20  # Large asteroid
        elif self.radius > ASTEROID_MIN_RADIUS:
            points = 50  # Medium asteroid
        else:
            points = 100  # Small asteroid

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return points

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_b * 1.2
        return points
