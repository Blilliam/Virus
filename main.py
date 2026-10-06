import warnings
import pygame
from game import Game
from box import Box
from config import Config

warnings.filterwarnings("ignore", category=UserWarning)

c = Config.load()

pygame.init()

# Fullscreen
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Simulation Controller")

# Clock
gameSpeed = 0.5

clock = pygame.time.Clock()
FPS = 60

# Create game
game = Game(screen_width, screen_height)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    # Get frame delta time in seconds
    dt = clock.tick(60) / 1000.0  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.handleClick(event)

    game.update(dt)
    
    screen.fill((30, 30, 30))
    game.draw(screen)
    pygame.display.flip()

pygame.quit()
