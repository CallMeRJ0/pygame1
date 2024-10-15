import pygame
import time

screen = pygame.display.set_mode((1000,720))
game_icon = pygame.image.load('placeholder.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game")

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

red = (235, 52, 52)
blue = (52, 122, 235)
black = (0, 0, 0)
white = (245, 249, 255)

snake_x = 490
snake_y = 350