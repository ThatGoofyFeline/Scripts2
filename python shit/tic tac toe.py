import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the grid
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw the grid lines
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

# Function to draw the X and O symbols
def draw_symbols():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH),
                                 ((col + 1) * SQUARE_SIZE - LINE_WIDTH, (row + 1) * SQUARE_SIZE - LINE_WIDTH), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH),
                                 (col * SQUARE_SIZE + LINE_WIDTH, (row + 1) * SQUARE_SIZE - LINE_WIDTH), LINE_WIDTH)
            elif grid[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - LINE_WIDTH, LINE_WIDTH)

# Function to check for a win
def check_win():
    # Check rows and columns
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ' or grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ' or grid[0][2] == grid[1][1] == grid[2][0] != ' ':
        return True

    return False

# Function to check for a tie
def check_tie():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == ' ':
                return False
    return True

# Main game loop
current_player = 'X'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            # Check if the clicked cell is empty
            if grid[clicked_row][clicked_col] == ' ':
                grid[clicked_row][clicked_col] = current_player

                if check_win():
                    print(f'Player {current_player} wins!')
                    pygame.quit()
                    sys.exit()
                elif check_tie():
                    print('It\'s a tie!')
                    pygame.quit()
                    sys.exit()

                # Switch to the other player
                current_player = 'O' if current_player == 'X' else 'X'

    # Draw the game board
    screen.fill(WHITE)
    draw_grid()
    draw_symbols()

    # Update the display
    pygame.display.flip()

# 100 lines!