import pygame
import pygetwindow as gw

def run_animation():
    # Initialize Pygame
    pygame.init()

    # Load character images
    character_images = [
        pygame.image.load("character_frame1.png"),
        pygame.image.load("character_frame2.png")
    ]

    # Get the size of the first character image
    image_width = character_images[0].get_width()
    image_height = character_images[0].get_height()

    # Set screen dimensions (same size as the image with some padding for movement)
    screen_width = image_width + 100  # Adding a little space for movement
    screen_height = image_height + 100  # Adding a little space for movement
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)  # NOFRAME removes window borders
    pygame.display.set_caption("Retro Character Animation")

    # Create a transparent surface
    background_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)  # Surface with alpha

    # Position the window in the top-right corner
    screen_info = pygame.display.Info()
    screen_x = screen_info.current_w - screen_width  # Set the window at the right edge
    screen_y = 0  # Set the window at the top of the screen

    # Use pygetwindow to move the Pygame window to the top-right
    window = gw.getWindowsWithTitle("Retro Character Animation")[0]
    window.moveTo(screen_x, screen_y)

    # Character position and animation variables
    x = 50
    y = screen_height - image_height - 50  # Make sure the character stays inside the screen
    frame = 0
    speed = 5

    # Game loop (this will run continuously)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle character movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed

        # Update animation frame
        frame += 1
        if frame >= len(character_images):
            frame = 0

        # Fill the background surface with transparent color
        background_surface.fill((0, 0, 0, 0))  # (R, G, B, Alpha) = transparent background

        # Draw character onto the screen
        screen.fill((0, 0, 0))  # Optional: Clear the screen
        screen.blit(background_surface, (0, 0))  # Draw transparent background surface
        screen.blit(character_images[frame], (x, y))  # Draw the character image

        pygame.display.flip()

        # Control animation speed
        pygame.time.Clock().tick(10)

    pygame.quit()
