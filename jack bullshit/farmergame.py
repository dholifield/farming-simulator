import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Farming Game")

# Load images for the GUI elements
background_image = pygame.image.load("background.png")
wheat_image = pygame.image.load("wheat.png")
corn_image = pygame.image.load("corn.png")
soybeans_image = pygame.image.load("soybeans.png")

# Create buttons for the different crops
wheat_button = pygame.Rect(100, 100, 64, 64)
corn_button = pygame.Rect(200, 100, 64, 64)
soybeans_button = pygame.Rect(300, 100, 64, 64)

# Create a Farmer object
farmer = Farmer()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for button clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if wheat_button.collidepoint(event.pos):
                farmer.plant_crop("wheat")
            elif corn_button.collidepoint(event.pos):
                farmer.plant_crop("corn")
            elif soybeans_button.collidepoint(event.pos):
                farmer.plant_crop("soybeans")

    # Draw the background and GUI elements
    screen.blit(background_image, (0, 0))
    screen.blit(wheat_image, wheat_button)
    screen.blit(corn_image, corn_button)
    screen.blit(soybeans_image, soybeans_button)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
