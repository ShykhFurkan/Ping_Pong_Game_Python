import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = -5
PADDLE_SPEED = 10
MAX_SCORE = 20
LIVES = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

def draw_window(paddle, ball, score, lives):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

    pygame.display.update()

def main():
    paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
    
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y
    
    score = 0
    lives = LIVES
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0:
            ball_speed_y = -ball_speed_y

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x = -ball_speed_x

        if ball.colliderect(paddle):
            ball_speed_y = -ball_speed_y
            score += 1
            if score >= MAX_SCORE:
                ball_speed_x *= 1.1
                ball_speed_y *= 1.1

        if ball.bottom >= HEIGHT:
            lives -= 1
            ball.x = WIDTH // 2 - BALL_RADIUS
            ball.y = HEIGHT // 2 - BALL_RADIUS
            ball_speed_x = random.choice([BALL_SPEED_X, -BALL_SPEED_X])
            ball_speed_y = BALL_SPEED_Y

            if lives <= 0:
                running = False
        
        draw_window(paddle, ball, score, lives)
        clock.tick(FPS)
    
    pygame.quit()
    print(f"Game Over! Your score: {score}")

if __name__ == "__main__":
    main()
