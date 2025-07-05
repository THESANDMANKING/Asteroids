import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            # Calculates a random float inbetween 20 and 50
            # This is used as an angle for the next step
            random_vector = random.uniform(20,50)
            # Calculates a new asteroid's rotation
            # One with a positive vector and one with a negative vector
            new_asteroid_1 = self.velocity.rotate(random_vector)
            new_asteroid_2 = self.velocity.rotate(-random_vector)
            # Calculates a new raduis for the new asteroids
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            # Increase's the velocity/speed of the new asteroids
            asteroid_1_velocity = new_asteroid_1 * 1.2
            asteroid_2_velocity = new_asteroid_2 * 1.2
            # Creates the new asteroid objects
            new_asteroid_object_1 = Asteroid(self.position, new_radius, asteroid_1_velocity)
            new_asteroid_object_2 = Asteroid(self.position, new_radius, asteroid_2_velocity)
            return [new_asteroid_object_1, new_asteroid_object_2]


    