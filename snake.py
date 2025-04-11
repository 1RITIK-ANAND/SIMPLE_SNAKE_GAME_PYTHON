import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Modern Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
DARK_GREEN = (0, 200, 70)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

# Font for score
font = pygame.font.SysFont('Arial', 24)

# Clock to control speed
clock = pygame.time.Clock()
speed = 10  # lower = slower

# Snake & Food initialization
snake = [[100, 100]]
direction = 'RIGHT'
change_to = direction
score = 0

# Generate food at random grid-aligned position
def spawn_food():
    return [random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE)]

food = spawn_food()

# Game over function
def game_over():
    msg = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(msg, (WIDTH // 3, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    screen.fill(GRAY)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    # Move the snake
    head = snake[0][:]
    if direction == 'UP':
        head[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        head[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        head[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        head[0] += BLOCK_SIZE

    # Add new head to snake
    snake.insert(0, head)

    # Eating food
    if head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    # Game over conditions
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        game_over()

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE), border_radius=5)

    # Draw snake
    for i, block in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (*block, BLOCK_SIZE, BLOCK_SIZE), border_radius=4)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(speed)
