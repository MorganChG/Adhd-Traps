import pygame
import math

pygame.init()

WIN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()
class Ball:
    def __init__(self) -> None:
        self.pos = (300,300)
        self.color = (240,240,240)
        self.radius = 3
        self.angle = 1
    
    def draw(self):
        pygame.draw.circle(WIN, self.color, self.pos, self.radius)
    
    def move(self):
        x,y = self.pos
        x = math.cos(self.angle) * x
        self.pos = (x,y)
def main():
    run = True
    ball = Ball()
    WIN.fill((40,40,40))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        ball.draw()
        ball.move()
        pygame.display.update()
        CLOCK.tick(30)
main()