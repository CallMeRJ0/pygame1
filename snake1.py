import pygame
import random

ICON = "snake.jpg"
APPLE = "apple.png"
WINDOW_CAPTION = "Snake Game"
screen_x = 1000
screen_y = 800
snake_speed = 10

pygame.init()

screen = pygame.display.set_mode((screen_x, screen_y))
game_icon = pygame.image.load(ICON)
pygame.display.set_icon(game_icon)
pygame.display.set_caption(WINDOW_CAPTION)
clock = pygame.time.Clock()

red = (235, 52, 52)
green = (188, 227, 199)
black = (0, 0, 0)
white = (245, 249, 255)
head_color = (255, 215, 0)

food_image = pygame.image.load(APPLE).convert_alpha()
food_image = pygame.transform.scale(food_image, (20, 20))

snake_x = 490
snake_y = 350
snake_x_change = 0
snake_y_change = 0
snake_list = []
snake_length = 1
score = 0

food_x = 0
food_y = 0

font = pygame.font.Font("ariblk.ttf", 30)

def load_high_score():
    try:
        with open("HI_score.txt", "r") as hi_score_file:
            value = hi_score_file.read().strip()
            return int(value) if value else 0
    except FileNotFoundError:
        with open("HI_score.txt", "w") as hi_score_file:
            hi_score_file.write("0")
        return 0
    except Exception as e:
        print(f"Error: {e}")

def save_high_score(high_score):
    global score
    if score > high_score:
        with open("HI_score.txt", "w") as hi_score_file:
            hi_score_file.write(str(score))

def HighscoreCounter(high_score, text_colour, bkgd_colour, x, y):
    txt = font.render(str(high_score) + " high score", True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x, y))
    screen.blit(txt, text_box)

def scoreCounter(snake_list, text_colour, bkgd_colour, x, y):
    global score
    score = int(len(snake_list) - 1)
    txt = font.render(str(score) + " score", True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x, y))
    screen.blit(txt, text_box)

def draw_snake(snake_list):
    if snake_list:
        pygame.draw.rect(screen, head_color, [snake_list[-1][0], snake_list[-1][1], 20, 20])
    for segment in snake_list[:-1]:
        pygame.draw.rect(screen, red, [segment[0], segment[1], 20, 20])

def message(msg, text_colour, bkgd_colour, x, y):
    txt = font.render(msg, True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x, y))
    screen.blit(txt, text_box)

def spawnFood():
    global food_x, food_y
    food_x = round(random.randrange(20, screen_x - 20) / 20) * 20
    food_y = round(random.randrange(60, screen_y - 20) / 20) * 20

def reset_game():
    global snake_x, snake_y, snake_x_change, snake_y_change, quit_game, snake_list, snake_length, score
    snake_x = 490
    snake_y = 350
    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1
    score = 0
    spawnFood()
    quit_game = False

high_score = load_high_score()
spawnFood()
quit_game = False

while True:
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                save_high_score(high_score)
                quit()
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

        if snake_x >= screen_x or snake_x < 0 or snake_y >= screen_y or snake_y < 0:
            quit_game = True

        if (food_x <= snake_x < food_x + 20) and (food_y <= snake_y < food_y + 20) or \
           (food_x <= snake_x + 20 < food_x + 20) and (food_y <= snake_y + 20 < food_y + 20):
            spawnFood()
            snake_length += 1

        snake_speed = (len(snake_list) * 2 + 6) if len(snake_list) > 1 else 10

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if snake_head in snake_list[:-1]:
            quit_game = True

        screen.fill(green)
        draw_snake(snake_list)
        scoreCounter(snake_list, black, white, screen_x - 80, 30)
        HighscoreCounter(high_score, black, white, 110, 30)
        screen.blit(food_image, (food_x, food_y))
        
        pygame.display.update()
        clock.tick(snake_speed)

    screen.fill(green)
    message("Press R to restart and press Q to quit program.", black, white, screen_x / 2, (screen_y / 2) - screen_y / 30)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                save_high_score(high_score)
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    save_high_score(high_score)
                    quit()
                elif event.key == pygame.K_r:
                    reset_game()
                    break

        if not quit_game:
            break
