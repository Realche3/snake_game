# Auhor "Mohamed Cherif Bah"
# Date "2024-09-06"

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Game clock and snake speed
clock = pygame.time.Clock()
snake_speed = 5
block_size = 10
current_level = 1
snake_length_check = 5
# Define font for score
font_style = pygame.font.SysFont("bahnschrift", 25)
# Font fo display text 
font = pygame.font.SysFont(None, 35)
# Function to draw the snake
def draw_snake(snake_list, block_size):
    for block in snake_list:
        pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

# Function to display messages
def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [screen_width / 6, screen_height / 3])

#Levels function 
def level_up():
    global current_level
    current_level += 1
    global snake_speed
    snake_speed += 2
    global snake_length_check 
    snake_length_check += 5
    # You can add more level-specific logic here (like increasing difficulty or adding new elements)

#Display text on the gamescreen 
def display_text(text, color, position):
    """
    Displays text on the screen.
    :param text: The text to display
    :param color: The color of the text (tuple of RGB values)
    :param position: The (x, y) position to display the text
    """
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position and movement
    x = screen_width / 2
    y = screen_height / 2
    x_change = 0
    y_change = 0

    score = 0
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    while not game_over:

        screen.fill(black)  # Clear the screen

        # Display text in top left corner
        display_text("Score: "+str(score)+"", white, (10, 10))
        
        # Display text in top right corner
        display_text("Level: "+ str(current_level)+"", white, (screen_width - 120, 10))
        
        pygame.display.update()  # Update the display

        while game_close:
            screen.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling for snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Update snake position
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True
        x += x_change
        y += y_change
       # screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        # Snake body mechanics
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list, block_size)
        pygame.display.update()

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snake_length += 1
            score +=5

        # Check if snake size has increased by 5 and level up 
        if snake_length >= snake_length_check :
            level_up()

        clock.tick(snake_speed)

    pygame.quit()
    quit()



# Start the game
game_loop()
