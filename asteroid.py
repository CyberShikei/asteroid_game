from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

import pygame

# Asteroid class


class Asteroid(CircleShape):
    def __init__(self,
                 x, y,
                 radius=ASTEROID_MIN_RADIUS,
                 ):
        # call the parent class constructor
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 255, 255),
                           (int(self.position.x), int(self.position.y)),
                           self.radius
                           )

    def update(self, dt):
        # moves in a straight line
        vel = self.velocity
        self.position += vel * dt
