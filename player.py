import pygame
from circleshape import CircleShape 
from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, 
    PLAYER_SPEED, PLAYER_SHOT_SPEED,
    PLAYER_COOLDOWN
)
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen, (255, 255, 255), self.triangle(), 2
        )

    def update(self, dt): 
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_LEFT]:
            self.__rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.__rotate(dt)
        if keys[pygame.K_UP]:
            self.__move(dt)
        if keys[pygame.K_DOWN]:
            self.__move(-dt)
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.__shoot(dt)

    def __rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def __move(self, dt):
        self.position += pygame.Vector2(0, -1).rotate(self.rotation) * (PLAYER_SPEED * dt) # direction * distance 

    def __shoot(self, dt):
        x, y = self.position
        shot = Shot(x, y)
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.cooldown = PLAYER_COOLDOWN 
