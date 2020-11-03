import pygame
import random
from paddle import Paddle
from ball import Ball

class Pong:

    # Constants
    WIDTH = 1920
    HEIGHT = 1080
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100
    BALL_WIDTH = 10
    VELOCITY = 10
    COLOUR = (255, 255, 255)

    # Constructor
    def __init__(self):

        pygame.init()

        # Create Window
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        # Players abd Ball
        self.paddles = []
        self.balls = []

        # Create Left Paddle
        self.paddles.append(Paddle(
            self.VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        # Create Right Paddle
        self.paddles.append(Paddle(
            self.VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        # Create Ball
        self.balls.append(Ball(
            self.VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))
    
    # Check if a ball has hit a wall, and bounce it if it has
    def wall_collision(self):
        for ball in self.balls:
            if ball.x > self.WIDTH or ball.x < 0:
                sys.exit(1)
            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    # Check if a ball has hit a paddle, and bounce it if it has
    def paddle_collision(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)
                    break

    def game(self):
        while True:

            # Handle Events
            for event in pygame.event.get():

                # Exit if escape is pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # Check for Collisions
            self.wall_collision()
            self.paddle_collision()

            # Black Fill
            self.window.fill((0, 0, 0))

            # Draw Paddles
            for paddle in self.paddles:
                paddle.move(self.HEIGHT)
                pygame.draw.rect(self.window, self.COLOUR, paddle)
            
            # Draw Ball
            for ball in self.balls:
                ball.move()
                pygame.draw.rect(self.window, self.COLOUR, ball)

            # Refresh Display
            pygame.display.flip()
            self.clock.tick(60)


# Main entry Point
if __name__ == '__main__':
    pong = Pong()
    pong.game()