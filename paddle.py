import pygame

class Paddle(pygame.Rect):

    # Constructor
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):

        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        
        super().__init__(*args, **kwargs)

    # Move Paddles
    def move(self, board_height):

        keys_pressed = pygame.key.get_pressed()

        # Up
        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        # Down
        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity