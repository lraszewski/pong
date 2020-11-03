import pygame

class Ball(pygame.Rect):

    # Constructor
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    # Move the Ball
    def move(self):
        self.x += self.velocity
        self.y += self.angle