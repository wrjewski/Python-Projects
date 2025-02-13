import os
import pygame
import random

# Force a specific SDL video driver
os.environ["SDL_VIDEODRIVER"] = "windib"

# Initialize pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 800, 600

# Create display window
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    if screen is None:
        raise Exception("Pygame display could not be initialized.")
except Exception as e:
    print(f"Error: {e}")
    pygame.quit()
    exit()

pygame.display.set_caption("Basic Flight Simulator")

# Define colors
WHITE = (255, 255, 255)
BLUE = (129,177,217)

# Load Aircraft image
aircraft = pygame.image.load("aircraft.png")
aircraft = pygame.transform.scale(aircraft, (80, 80))
aircraft_x = WIDTH // 2 - 40
aircraft_y = HEIGHT - 120

# Load cloud images
cloud_images = [
    pygame.image.load("cloud1.png"),
    pygame.image.load("cloud2.png"),
    pygame.image.load("cloud3.png"),
    pygame.image.load("cloud4.png")
]

# Resize clouds
cloud_images = [pygame.transform.scale(cloud, (150, 100)) for cloud in cloud_images]

# Cloud positions and speeds
clouds = []
for _ in range(6):  # Number of clouds
    cloud_x = random.randint(WIDTH, WIDTH + 300)  # Start off-screen
    cloud_y = random.randint(50, HEIGHT - 200)  # Random vertical position
    cloud_speed = random.uniform(1, 3)  # Random speed
    cloud_image = random.choice(cloud_images)  # Random cloud type
    clouds.append({"x": cloud_x, "y": cloud_y, "speed": cloud_speed, "image": cloud_image})

# Create a clock to control frame rate
clock = pygame.time.Clock()

# Movement variables
speed_x = 0
speed_y = 0
acceleration = 0.2
max_speed = 6
friction = 0.05  # Slows the aircraft when no keys are pressed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Accelerate smoothly
    if keys[pygame.K_LEFT] and aircraft_x > 0:
        speed_x -= acceleration
    elif keys[pygame.K_RIGHT] and aircraft_x < WIDTH - 80:
        speed_x += acceleration
    else:
        speed_x *= (1 - friction)  # Apply friction

    if keys[pygame.K_UP] and aircraft_y > 0:
        speed_y -= acceleration
    elif keys[pygame.K_DOWN] and aircraft_y < HEIGHT - 80:
        speed_y += acceleration
    else:
        speed_y *= (1 - friction)  # Apply friction

    # Limit speed
    speed_x = max(-max_speed, min(speed_x, max_speed))
    speed_y = max(-max_speed, min(speed_y, max_speed))

    # Apply movement
    aircraft_x += speed_x
    aircraft_y += speed_y

    # Keep aircraft within screen boundaries
    if aircraft_x < 0:
        aircraft_x = 0
    if aircraft_x > WIDTH - 80:
        aircraft_x = WIDTH - 80
    if aircraft_y < 0:
        aircraft_y = 0
    if aircraft_y > HEIGHT - 80:
        aircraft_y = HEIGHT - 80

    # Move and draw clouds
    for cloud in clouds:
        cloud["x"] -= cloud["speed"]  # Move cloud left

        # If cloud moves off-screen, reset to the right
        if cloud["x"] < -150:
            cloud["x"] = random.randint(WIDTH, WIDTH + 300)
            cloud["y"] = random.randint(50, HEIGHT - 200)
            cloud["speed"] = random.uniform(1, 3)

    # Fill background with sky color
    screen.fill(BLUE)

    # Draw clouds
    for cloud in clouds:
        screen.blit(cloud["image"], (cloud["x"], cloud["y"]))

    # Draw aircraft
    screen.blit(aircraft, (aircraft_x, aircraft_y))

    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
