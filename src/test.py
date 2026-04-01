import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Soccer Game")

# Player setup
player_x = 100
player_y = 250
player_size = 50
player_speed = 5

# Ball setup
ball_x = 400
ball_y = 300
ball_radius = 15
ball_speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ball follows player (simple interaction)
    if abs(player_x - ball_x) < 60 and abs(player_y - ball_y) < 60:
        if player_x < ball_x:
            ball_x += ball_speed
        if player_x > ball_x:
            ball_x -= ball_speed
        if player_y < ball_y:
            ball_y += ball_speed
        if player_y > ball_y:
            ball_y -= ball_speed

    # Drawing
    screen.fill((0, 100, 0))  # green field

    # Player (blue square)
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_size, player_size))

    # Ball (white circle)
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()