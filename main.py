import pygame

import sys

from constants import *

from circleshape import CircleShape

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from shot import Shot
# Screen initalization and setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Grouping of sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Establishing containers for Player Class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Instantiation (?!) Of the Player Sprite
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield = AsteroidField()
    # Infinite loop to ensure screen loads black and refreshes
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0, 0, 0))
        # dt has to be updated with clock tick FIRST before updating!
        dt = clock.tick(60) / 1000
        for object in updatable:
            object.update(dt)
        # collision detection defining game over condition and gameplay
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()  
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
                       

if __name__ == "__main__":
    main()




