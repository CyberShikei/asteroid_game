from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

import pygame

# Shot class


class Shot(CircleShape):
    def __init__(self,
                 x, y,
                 rotation=0,
                 radius=SHOT_RADIUS):
        # call the parent class constructor
        super().__init__(x, y, radius)

        self.set_velocity(rotation)

    def set_velocity(self, rotation):
        self.velocity = pygame.math.Vector2(0, 1)
        self.velocity.rotate_ip(rotation)
        self.velocity.scale_to_length(PLAYER_SHOOT_SPEED)
