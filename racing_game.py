import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (50, 50, 50)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car sizes
CAR_WIDTH = 50
CAR_HEIGHT = 100

# Player car
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 10
player_speed = 5

# Enemy car
enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
enemy_y = -CAR_HEIGHT
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, CAR_WIDTH, CAR_HEIGHT))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(GRAY)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - CAR_WIDTH:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -CAR_HEIGHT
        enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
        score += 1

    # Draw cars
    draw_car(player_x, player_y, RED)
    draw_car(enemy_x, enemy_y, WHITE)

    # Collision check
    player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, CAR_WIDTH, CAR_HEIGHT)

    if player_rect.colliderect(enemy_rect):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
