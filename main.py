# Add a scoring system
# Implement multiple lives and respawning
# Add an explosion effect for the asteroids
# Add acceleration to the player movement
# Make the objects wrap around the screen instead of disappearing
# Add a background image
# Create different weapon types
# Make the asteroids lumpy instead of perfectly round
# Make the ship have a triangular hit box instead of a circular one
# Add a shield power-up
# Add a speed power-up
# Add bombs that can be dropped
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
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

    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) #player.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() 

        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
