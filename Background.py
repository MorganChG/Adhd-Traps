import pygame,random

pygame.init()

Win = pygame.display.set_mode((800,800))
Grey = (40,40,40)
White = (240,240,240)
clock = pygame.time.Clock()
balls_pos = [(100,50), (300,400), (300,100), (200,100)]

class Ball:
    def __init__(self):
        self.pos = (random.randrange(10,790, 10),random.randrange(10,790, 10)) 
        self.new_pos = ()
        self.radius = 1
        self.color = Grey
        self.line_color =  White
        self.at_new = True
       
    
    def draw(self):
        pygame.draw.circle(Win, (240,40,40), self.pos, self.radius)
    
    def draw_line(self, other):
        difference_x = abs(self.pos[0] - other[0])
        difference_y = abs(self.pos[1] - other[1])
        if difference_x <= 100:
            if difference_y <= 100:
                 pygame.draw.line(Win, self.line_color, self.pos, other, 1)
                 
    def move(self):
        if self.at_new:
            self.new_pos = (random.randrange(-10,800, 10),random.randrange(-10, 800, 10))
            self.at_new = False  
        
        ax, ay = self.pos
        bx, by = self.new_pos
        cx , cy = bx - ax, by - ay
        
        x = ax + cx * 0.001
        y = ay + cy * 0.001
        
        self.pos = (x,y)
        
        #print(self.pos, self.new_pos)
        
        if round(self.pos[0]) == self.new_pos[0] and round(self.pos[1]) == self.new_pos[1]:
            self.at_new = True
        
        

def main():
    balls = []
    for i in range(200):
        ball = Ball()
        balls.append(ball)
        
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                    
        Win.fill(Grey)
        for ball in balls:
            ball.draw()
            ball.move()
            for ball2 in balls:
                ball.draw_line(ball2.pos)
            
        pygame.display.update()
        clock.tick(60)
        
main()