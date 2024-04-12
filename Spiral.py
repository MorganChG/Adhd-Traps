import pygame, math, random

Win = pygame.display.set_mode((600,600), pygame.NOFRAME)
clock = pygame.time.Clock()


class Ball:
    def __init__(self):
        self.pos = (0,0)
        
        self.radius = 3
        
        self.r = 80
        self.b = 240
        self.color = (self.r,120,self.b)
        
        self.circleRadius = 21
        self.angle = 0
        self.angleIncrement = 0
        self.gravity = 0
        self.maxGravity = 20
        
        
    
    def starting_pos(self):
        self.pos = (300,300)
       
        
        
    def draw(self):
        if self.r != 240:
            self.r += 10
        if self.b != 40:
            self.b -= 2
        self.color = (self.r,40,self.b)
        pygame.draw.circle(Win, self.color, self.pos, self.radius)

    
    def move(self):
        x,y = self.pos
        
        x = (x) - math.cos(math.radians(self.angle)) * self.circleRadius
        y = (y) - math.sin(math.radians(self.angle)) * self.circleRadius
        
        if self.gravity <= self.maxGravity:
            self.gravity += 1

        self.angle += self.gravity
        
        
        self.pos = (x,y)
        if self.gravity > self.maxGravity:
            self.gravity = 0
            self.starting_pos()
            self.angleIncrement += 2.5
            self.angle = 0
            self.angle += self.angleIncrement
            if self.angleIncrement > 360:
                self.angleIncrement = 0
                Win.fill((40,40,40))
            self.r = 80
            self.b = 240
            

def main():
    Win.fill((40,40,40))
    run = True
    ball = Ball()
    ball.starting_pos()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    run = False
                
        ball.draw()
        
        ball.move()
        
        
        pygame.display.update()
        clock.tick(60)
        #Win.fill((40,40,40))
main()