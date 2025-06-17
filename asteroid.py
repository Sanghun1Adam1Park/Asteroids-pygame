import pygame 
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

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
    
    def split(self):
        self.kill()
  
        if self.radius <= ASTEROID_MIN_RADIUS: return
        
        rangle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(rangle) * 1.2
        new_vector_2 = self.velocity.rotate(-rangle) * 1.2     
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
            
        a1 = Asteroid(x, y, new_radius)
        a2 = Asteroid(x, y, new_radius)

        a1.velocity = new_vector_1
        a2.velocity = new_vector_2
