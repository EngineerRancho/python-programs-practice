import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
STEP_COLOR = (0, 0, 0)
BALL_RADIUS = 20
STEP_HEIGHT = 50
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball on Steps")

# Initial ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT - BALL_RADIUS
ball_velocity_y = -10  # Initial upward velocity

# Number of steps and step width
num_steps = 5
step_width = WIDTH // num_steps

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the steps
    for i in range(num_steps):
        pygame.draw.rect(
            screen,
            STEP_COLOR,
            (i * step_width, HEIGHT - (i + 1) * STEP_HEIGHT, step_width, STEP_HEIGHT),
        )

    # Update ball position and velocity
    ball_y += ball_velocity_y
    ball_velocity_y += 1  # Simulate gravity

    # Check for collisions with the steps
    if ball_y >= HEIGHT - BALL_RADIUS:
        ball_y = HEIGHT - BALL_RADIUS
        ball_velocity_y = -abs(ball_velocity_y)  # Reverse and dampen the velocity

    # Draw the bouncing ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, int(ball_y)), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
