import pygame
import sys
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from heart import Heart

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def setup_game():
    """Initializes game state."""
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    hearts = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Heart.containers = drawable, updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Initialize "hearts"
    heart_radius = 10
    heart_spacing = 5
    initial_spacing = 5
    for i in range(player.health):
        heart_x = (
            initial_spacing + heart_radius + i * (2 * heart_radius + heart_spacing)
        )
        heart_y = heart_radius + 5
        heart = Heart(heart_x, heart_y, heart_radius)
        hearts.add(heart)

    return updatable, drawable, asteroids, shots, player, hearts


def start_screen(screen):
    title_font = pygame.font.Font(None, 48)
    font = pygame.font.Font(None, 24)
    title = title_font.render("asteroids-py", True, WHITE)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    text = font.render("Press Enter to Start", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    screen.fill(BLACK)
    screen.blit(title, title_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False


def draw_score(screen, score):
    """Draws the player's score in the top-right corner."""
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score:", True, WHITE)
    score_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

    score_points_text = font.render(str(score), True, WHITE)
    score_points_rect = score_points_text.get_rect(
        topright=(SCREEN_WIDTH - 10, score_rect.bottom + 5)
    )
    screen.blit(score_points_text, score_points_rect)


def draw_play_again_button(screen):
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 100, 40)
    pygame.draw.rect(screen, WHITE, button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render("Play Again", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect


def game_over(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press Enter to play again", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    play_again_button_rect = draw_play_again_button(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_again_button_rect.collidepoint(event.pos):
                        main()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    start_screen(screen)

    updatable, drawable, asteroids, shots, player, hearts = setup_game()
    dt = 0

    while True:
        # Check if user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) and not player.invulnerable:
                player.health -= 1
                if hearts:
                    hearts.sprites()[-1].kill()
                if player.health <= 0:
                    print("Game over! Restarting game...")
                    game_over(screen)
                else:
                    print(f"Player hit! Lives remaining: {player.health}")
                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    bullet.kill()
                    points = asteroid.split()
                    player.score += points

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for heart in hearts:
            heart.draw(screen)

        draw_score(screen, player.score)

        pygame.display.flip()

        # max 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
