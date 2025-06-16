import pygame 
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (205, 205, 205), self.position, self.radius, 2
        )

    def update(self, dt): 
       self.position += self.velocity * dt 

    def __move(self, dt):
        self.position += pygame.Vector2(0, -1).rotate(self.rotation) * (PLAYER_SPEED * dt) # direction * distance 

