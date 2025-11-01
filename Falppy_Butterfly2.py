import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Butterfly")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (34, 139, 34)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Load butterfly image
butterfly_img = pygame.image.load(r"C:\Users\Sangita\OneDrive\Desktop\BWU_23_396\PYTHON_PROJECT\1656e3fa305853d.jpg")
butterfly_img = pygame.transform.scale(butterfly_img, (50, 40))

# Butterfly properties
butterfly_x = 100
butterfly_y = HEIGHT // 2
butterfly_velocity = 0
gravity = 0.5
jump_strength = -8
   
# Pipe properties
pipe_width = 70
pipe_gap = 200
pipe_speed = 4
pipes = []
score = 0

# Font
font = pygame.font.SysFont("Arial", 32)


def create_pipe():
    """Creates a pair of pipes (top and bottom)."""
    height = random.randint(100, HEIGHT - pipe_gap - 100)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    return top_pipe, bottom_pipe


# Create first pipe
pipes.extend(create_pipe())

running = True
while running:
    screen.fill(BLUE)  # Background color

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                butterfly_velocity = jump_strength

    # Gravity effect
    butterfly_velocity += gravity
    butterfly_y += butterfly_velocity

    # Draw butterfly
    screen.blit(butterfly_img, (butterfly_x, butterfly_y))

    # Pipe movement
    for pipe in pipes:
        pipe.x -= pipe_speed
        pygame.draw.rect(screen, GREEN, pipe)

    # Add new pipes when the first pipe goes out of screen
    if pipes[0].x < -pipe_width:
        pipes = pipes[2:]
        pipes.extend(create_pipe())
        score += 1

    # Collision detection
    butterfly_rect = pygame.Rect(butterfly_x, butterfly_y, 50, 40)
    for pipe in pipes:
        if butterfly_rect.colliderect(pipe):
            running = False

    if butterfly_y <= 0 or butterfly_y >= HEIGHT:
        running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
