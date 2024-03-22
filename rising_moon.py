import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
MOON_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Growing Moon Animation")

# Initial moon size and position
moon_radius = 50
moon_x = WIDTH // 2
moon_y = HEIGHT // 2

# Animation variables
growing = True

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the moon
    pygame.draw.circle(screen, MOON_COLOR, (moon_x, moon_y), moon_radius)

    # Update the moon's size
    if growing:
        moon_radius += 1
    else:
        moon_radius -= 1

    # If the moon reaches a certain size, start shrinking it
    if moon_radius >= 100:
        growing = False

    # If the moon becomes very small, start growing it again
    if moon_radius <= 50:
        growing = True

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()