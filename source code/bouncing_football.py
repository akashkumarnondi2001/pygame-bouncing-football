import math

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Football")

# Load and resize the background image to fit the screen
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (width, height))
background_rect = background_img.get_rect()

# Load and resize the football image
football_img = pygame.image.load("football.png")
football_img = pygame.transform.scale(football_img, (100, 100))

# Define the football's properties
x = width // 2
y = height // 2
radius = 50
speed = 5
angle = math.pi / 4
spin_speed = math.pi / 20  # Angular velocity of the spin in radians per frame
spin_angle = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background_img, background_rect)

    # Rotate the football image and draw it
    football_rotated = pygame.transform.rotate(
        football_img, math.degrees(spin_angle)
    )
    football_rect = football_rotated.get_rect(center=(int(x), int(y)))
    screen.blit(football_rotated, football_rect)

    # Update the spin angle
    spin_angle += spin_speed

    # Move the football
    x += 2 * speed * math.cos(angle)
    y += 2 * speed * math.sin(angle)

    # Check for collisions with the walls
    if x - radius < 0 or x + radius > width:
        angle = math.pi - angle
    if y - radius < 0 or y + radius > height:
        angle = -angle

    # Update the display
    pygame.display.update()

    # Wait for a short time to control the speed of the animation
    pygame.time.wait(10)

# Quit Pygame
pygame.quit()
