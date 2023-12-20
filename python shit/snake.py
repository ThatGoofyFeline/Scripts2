import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
initial_speed = 5
snake_speed = initial_speed
FPS = 30

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the snake and the food
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate a new food position
def generate_food(snake):
    food = None
    while food is None:
        food = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if food in snake:
            food = None
    return food

# Function to draw the gridded background
def draw_grid_background():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

# Main game loop
snake = [[GRID_SIZE // 2, GRID_SIZE // 2]]
snake_direction = RIGHT
food = generate_food(snake)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT
            elif event.key == pygame.K_q:
                snake_speed = max(1, snake_speed - 1)
            elif event.key == pygame.K_e:
                snake_speed += 1

    # Update snake position
    if pygame.time.get_ticks() % (FPS // snake_speed) == 0:
        new_head = [snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]]
        snake.insert(0, new_head)

        # Check for collisions
        if new_head == food:
            food = generate_food(snake)
        else:
            snake.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_SIZE
            or new_head[1] < 0
            or new_head[1] >= GRID_SIZE
            or new_head in snake[1:]
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the gridded background
    draw_grid_background()

    # Draw the snake and food
    draw_snake(snake)
    draw_food(food)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)