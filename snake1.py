import pygame
import time

screen = pygame.display.set_mode((1000,720))
game_icon = pygame.image.load('placeholder.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

red = (235, 52, 52)
blue = (52, 122, 235)
black = (0, 0, 0)
white = (245, 249, 255)
snake_x = 490
snake_y = 350
snake_x_change = 0
snake_y_change = 0

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            if event.key == pygame.K_UP:
                snake_y_change = -20
                snake_x_change = 0
            if event.key == pygame.K_DOWN:
                snake_y_change = 20
                snake_x_change = 0

snake_x += snake_x_change
snake_y += snake_y_change


screen.fill(green)

pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
pygame.display.update()

clock.tick(10)