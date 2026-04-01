import pygame
import sys
from sprites import Player

pygame.init()
clock= pygame.time.Clock()

WIDTH,HEIGHT= 800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("footballRetro")

player = Player(100, 250, 50, 3)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnigng = False

    keys = pygame.key.get_pressed()

    player.move(keys)
    player.stay_in_bounds(WIDTH,HEIGHT)

    screen.fill((0, 100, 0))

    player.draw(screen)
    print(player.x, player.size)
   


    # Update display
    pygame.display.flip()
    clock.tick(60)
