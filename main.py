import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from explosion import Explosion, ExplosionManager

def main():
    print("Starting Asteroids!")
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    fps = 60
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Explosion.containers = (explosions, updatable, drawable)
    #ExplosionManager.containers = (explosions, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    my_asteroid_field = AsteroidField()
    #my_explosion_manager = ExplosionManager()
    my_score = Score()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')
        #dt = game_clock.tick(fps) / 1000
        updatable.update(dt)
        for a in asteroids:
            if my_player.check_collision(a):
                print("Game Over!")
                print("Final Score:", my_score.total)
                return
            for a1 in asteroids:
                if a1.position == a.position:
                    continue
                if a1.check_collision(a) or a.check_collision(a1):
                    a1.bounce(a)

            for s in shots:
                if s.check_collision(a):
                    if a.color == 'purple':
                        my_score.multiplier += 1 if my_score.multiplier < 5 else 0  
                    a.split(explosions)
                    s.kill()
                    my_score.increase_score()
        
        my_score.render(screen, dt)


        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
