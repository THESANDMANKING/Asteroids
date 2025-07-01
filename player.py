from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED,PLAYER_SPEED,SHOT_RADIUS,PLAYER_SHOOT_SPEED
import pygame


class Player(CircleShape):
    # Always use self.whatever when initializing fields/variables
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    # Makes the player's character look like a Triangle
    # But uses the CircleShape for the hitbox so they hitbox is a circle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Movement Keys
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # Fires Bullets
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Calculates where the shots should be spawning at (the front of the ship)
        shot_rotation = pygame.Vector2(0,1).rotate(self.rotation)
        # Tells the game to spawn the Shot class at the player's x and y position,
        # How big the shot should be
        # and the velocity of the shot
        spawn_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, shot_rotation * PLAYER_SHOOT_SPEED)



        


class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)
