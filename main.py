import pygame
from constants import *
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 

        updatable.update(dt)
        for a in asteroids:
            if a.collision_check(player):
                print("Game Over!")
                sys.exit() 

        for a in asteroids:
            for s in shots:
                if s.collision_check(a):
                    s.kill()
                    a.split()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Sleeps for 1/60 seconds so it only runs 60 times in a sec.

if __name__ == "__main__":
    main()
