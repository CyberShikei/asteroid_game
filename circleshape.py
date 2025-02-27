import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 255, 255),
                           self.position,
                           int(self.get_radius())
                           )

    def update(self, dt):
        self.position += self.velocity * dt

    def get_radius(self):
        return self.radius

    def colides_with(self, other):
        dist = self.position.distance_to(other.position)
        condition = dist < self.radius + other.radius
        return condition
