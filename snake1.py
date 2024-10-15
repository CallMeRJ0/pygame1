import pygame
import time

ICON_PNG = "placeholder.png"
WINDOW_CAPTION = "Snake Game"
WINDOW_X = 1000
WINDOW_Y = 720

screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
game_icon = pygame.image.load(ICON_PNG)
pygame.display.set_icon(game_icon)
pygame.display.set_caption(WINDOW_CAPTION)
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
            if event.key == pygame.K_LEFT or event.key == pygame.K_A:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_D:
                snake_x_change = 20
                snake_y_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_W:
                snake_y_change = -20
                snake_x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_S:
                snake_y_change = 20
                snake_x_change = 0

if snake_x >= WINDOW_X or snake_x < 0 or snake_y >= WINDOW_Y or snake_y < 0:
    quit_game = Trhe


snake_x += snake_x_change
snake_y += snake_y_change


screen.fill(green)

pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
pygame.display.update()

clock.tick(10)