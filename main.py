import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # calculating dt
        dt = clock.tick(60)/1000
        # update player
        updatable.update(dt)
        # check for player collision
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # check for shot collision
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    break

        # rendering
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()

# ----------------------------------------
# Boot.dev Reminder:
# Activate venv each new terminal:
# cd ~/bootdev/asteroids
# source .venv/bin/activate
# uv run main.py
# ----------------------------------------
