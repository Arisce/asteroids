import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            positive_rotated_vector = self.velocity.rotate(angle)
            negative_rotated_vector = self.velocity.rotate(-angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            smaller_positive = Asteroid(self.position.x, self.position.y, smaller_radius)
            smaller_negative = Asteroid(self.position.x, self.position.y, smaller_radius)
            smaller_positive.velocity = positive_rotated_vector * 1.2
            smaller_negative.velocity = negative_rotated_vector * 1.2