import pygame  # Import the pygame library
import random  # Import the random library

ICON = "snake.jpg"  # Define the icon for the game
APPLE = "apple.png"  # Define the apple image
WINDOW_CAPTION = "Snake Game"  # Set the window title
screen_x = 1000  # Set the width of the game window
screen_y = 800  # Set the height of the game window
snake_speed = 10  # Set the initial speed of the snake

pygame.init()  # Initialize all imported pygame modules

screen = pygame.display.set_mode((screen_x, screen_y))  # Create the game window
game_icon = pygame.image.load(ICON)  # Load the game icon
pygame.display.set_icon(game_icon)  # Set the game icon
pygame.display.set_caption(WINDOW_CAPTION)  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to control game speed

red = (235, 52, 52)  # Define the color red
green = (188, 227, 199)  # Define the color green
black = (0, 0, 0)  # Define the color black
white = (245, 249, 255)  # Define the color white
head_color = (255, 215, 0)  # Define the color for the snake's head

food_image = pygame.image.load(APPLE).convert_alpha()  # Load the apple image and convert it
food_image = pygame.transform.scale(food_image, (20, 20))  # Scale the apple image to 20x20 pixels

snake_x = 490  # Set the initial x-coordinate of the snake
snake_y = 350  # Set the initial y-coordinate of the snake
snake_x_change = 0  # Initialize x-direction movement to 0
snake_y_change = 0  # Initialize y-direction movement to 0
snake_list = []  # Create a list to store the snake's segments
snake_length = 1  # Set the initial length of the snake
score = 0  # Initialize the score

food_x = 0  # Initialize the x-coordinate of the food
food_y = 0  # Initialize the y-coordinate of the food

font = pygame.font.Font("ariblk.ttf", 30)  # Load the font for rendering text

def load_high_score():  # Function to load the high score
    try:
        with open("HI_score.txt", "r") as hi_score_file:  # Open the high score file for reading
            value = hi_score_file.read().strip()  # Read the value and remove whitespace
            return int(value) if value else 0  # Return the value as an integer or 0 if empty
    except FileNotFoundError:  # Handle the case where the file does not exist
        with open("HI_score.txt", "w") as hi_score_file:  # Create the file and write 0
            hi_score_file.write("0")
        return 0  # Return 0 as the high score
    except Exception as e:  # Handle other exceptions
        print(f"Error: {e}")  # Print the error message

def save_high_score(high_score):  # Function to save the high score
    global score  # Use the global score variable
    if score > high_score:  # Check if the current score is higher than the high score
        with open("HI_score.txt", "w") as hi_score_file:  # Open the file for writing
            hi_score_file.write(str(score))  # Write the current score as the new high score

def HighscoreCounter(high_score, text_colour, bkgd_colour, x, y):  # Function to display the high score
    txt = font.render(str(high_score) + " high score", True, text_colour, bkgd_colour)  # Render the high score text
    text_box = txt.get_rect(center=(x, y))  # Get the rectangle for positioning the text
    screen.blit(txt, text_box)  # Draw the high score text on the screen

def scoreCounter(snake_list, text_colour, bkgd_colour, x, y):  # Function to display the current score
    global score  # Use the global score variable
    score = int(len(snake_list) - 1)  # Update the score based on the length of the snake
    txt = font.render(str(score) + " score", True, text_colour, bkgd_colour)  # Render the score text
    text_box = txt.get_rect(center=(x, y))  # Get the rectangle for positioning the text
    screen.blit(txt, text_box)  # Draw the score text on the screen

def draw_snake(snake_list):  # Function to draw the snake
    if snake_list:  # Check if the snake list is not empty
        pygame.draw.rect(screen, head_color, [snake_list[-1][0], snake_list[-1][1], 20, 20])  # Draw the snake's head
    for segment in snake_list[:-1]:  # Loop through the segments of the snake
        pygame.draw.rect(screen, red, [segment[0], segment[1], 20, 20])  # Draw each segment of the snake

def message(msg, text_colour, bkgd_colour, x, y):  # Function to display a message on the screen
    txt = font.render(msg, True, text_colour, bkgd_colour)  # Render the message text
    text_box = txt.get_rect(center=(x, y))  # Get the rectangle for positioning the text
    screen.blit(txt, text_box)  # Draw the message on the screen

def spawnFood():  # Function to spawn food at a random location
    global food_x, food_y  # Use the global food coordinates
    food_x = round(random.randrange(20, screen_x - 20) / 20) * 20  # Randomize food x-position
    food_y = round(random.randrange(60, screen_y - 20) / 20) * 20  # Randomize food y-position

def reset_game():  # Function to reset the game state
    global snake_x, snake_y, snake_x_change, snake_y_change, quit_game, snake_list, snake_length, score  # Use global variables
    snake_x = 490  # Reset the x-coordinate of the snake
    snake_y = 350  # Reset the y-coordinate of the snake
    snake_x_change = 0  # Reset x-direction movement
    snake_y_change = 0  # Reset y-direction movement
    snake_list = []  # Reset the snake's segments
    snake_length = 1  # Reset the snake's length
    score = 0  # Reset the score
    spawnFood()  # Spawn food in a new location
    quit_game = False  # Set quit_game to False

high_score = load_high_score()  # Load the high score at the start
spawnFood()  # Spawn food at the start
quit_game = False  # Initialize the game state

while True:  # Main game loop
    while not quit_game:  # Loop until the game is quit
        for event in pygame.event.get():  # Process events
            if event.type == pygame.QUIT:  # Check for quit event
                pygame.quit()  # Quit pygame
                save_high_score(high_score)  # Save the high score
                quit()  # Exit the program
            if event.type == pygame.KEYDOWN:  # Check for key presses
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # Move left
                    snake_x_change = -20  # Change x-direction to left
                    snake_y_change = 0  # Reset y-direction
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # Move right
                    snake_x_change = 20  # Change x-direction to right
                    snake_y_change = 0  # Reset y-direction
                if event.key == pygame.K_UP or event.key == pygame.K_w:  # Move up
                    snake_y_change = -20  # Change y-direction to up
                    snake_x_change = 0  # Reset x-direction
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # Move down
                    snake_y_change = 20  # Change y-direction to down
                    snake_x_change = 0  # Reset x-direction

        snake_x += snake_x_change  # Update the snake's x-coordinate
        snake_y += snake_y_change  # Update the snake's y-coordinate

        if snake_x >= screen_x or snake_x < 0 or snake_y >= screen_y or snake_y < 0:  # Check for collision with walls
            quit_game = True  # End the game

        if (food_x <= snake_x < food_x + 20) and (food_y <= snake_y < food_y + 20) or \
           (food_x <= snake_x + 20 < food_x + 20) and (food_y <= snake_y + 20 < food_y + 20):  # Check if the snake has eaten food
            spawnFood()  # Spawn new food
            snake_length += 1  # Increase the length of the snake

        snake_speed = (len(snake_list) * 2 + 6) if len(snake_list) > 1 else 10  # Adjust snake speed based on length

        snake_head = [snake_x, snake_y]  # Create a new head for the snake
        snake_list.append(snake_head)  # Add the head to the snake's segments
        if len(snake_list) > snake_length:  # Check if the snake is too long
            del snake_list[0]  # Remove the oldest segment

        if snake_head in snake_list[:-1]:  # Check for self-collision
            quit_game = True  # End the game

        screen.fill(green)  # Clear the screen with green color
        draw_snake(snake_list)  # Draw the snake on the screen
        scoreCounter(snake_list, black, white, screen_x - 80, 30)  # Display the current score
        HighscoreCounter(high_score, black, white, 110, 30)  # Display the high score
        screen.blit(food_image, (food_x, food_y))  # Draw the food on the screen
        
        pygame.display.update()  # Update the display
        clock.tick(snake_speed)  # Control the frame rate

    screen.fill(green)  # Clear the screen with green color
    message("Press R to restart and press Q to quit program.", black, white, screen_x / 2, (screen_y / 2) - screen_y / 30)  # Display the game over message
    pygame.display.update()  # Update the display

    while True:  # Loop for game over state
        for event in pygame.event.get():  # Process events
            if event.type == pygame.QUIT:  # Check for quit event
                pygame.quit()  # Quit pygame
                save_high_score(high_score)  # Save the high score
                quit()  # Exit the program
            if event.type == pygame.KEYDOWN:  # Check for key presses
                if event.key == pygame.K_q:  # Check if 'Q' is pressed to quit
                    pygame.quit()  # Quit pygame
                    save_high_score(high_score)  # Save the high score
                    quit()  # Exit the program
                elif event.key == pygame.K_r:  # Check if 'R' is pressed to restart
                    reset_game()  # Reset the game state
                    break  # Break out of the loop

        if not quit_game:  # If the game is not quit
            break  # Exit the game over loop