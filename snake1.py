import pygame
import time

ICON_PNG = "snake.jpg"
WINDOW_CAPTION = "Snake Game"
WINDOW_X = 1000
WINDOW_Y = 720
snake_speed = 10

pygame.init()

screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
game_icon = pygame.image.load(ICON_PNG)
pygame.display.set_icon(game_icon)
pygame.display.set_caption(WINDOW_CAPTION)
clock = pygame.time.Clock()

red = (235, 52, 52)
green = (188, 227, 199)
black = (0, 0, 0)
white = (245, 249, 255)
snake_x = 490
snake_y = 350
snake_x_change = 0
snake_y_change = 0

font = pygame.font.Font("ariblk.ttf", 50) 
def message(msg, text_colour, bkgd_colour):
    txt = font.render(msg, True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake_x_change = 20
                snake_y_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake_y_change = -20
                snake_x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake_y_change = 20
                snake_x_change = 0

    snake_x += snake_x_change
    snake_y += snake_y_change

    if snake_x >= WINDOW_X or snake_x < 0 or snake_y >= WINDOW_Y or snake_y < 0:
        quit_game = True

    screen.fill(green)
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(snake_speed)

screen.fill(green)
message("You died!", black, white)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
