import pygame, random
from pygame import gfxdraw


Win = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
White = (240,240,240)
Light_Grey = (190, 190, 190) 
Grey = (40,40,40)
Black = (10,10,10)
class Point:
    def __init__(self, x, y) -> None:
        self.pos = (x,y)
        self.color = White
        self.line_color = Light_Grey
        self.raidus = 5
    
    def draw(self):
        pygame.draw.circle(Win, White, center= self.pos, radius= self.raidus)
    
    def connect_point(self, other):
        pygame.draw.aaline(Win, self.line_color, self.pos, other)
    
        

class Ball:
    def __init__(self) -> None:
        self.pos = (300,300)
        self.color = White
        self.current_color = "Red"
        self.radius = 10
        self.vel = (1,1)
        self.speed = (0.01,0.009)
        self.bounce = False
    
    def draw(self):
        x,y = self.pos
        gfxdraw.aacircle(Win, round(x), round(y), self.radius + 1, Black)
        gfxdraw.filled_circle(Win, round(x), round(y), self.radius,self.color)
    
    def move(self):
        x,y = self.pos
        a,b = self.vel
        sx, sy = self.speed
        if self.pos[0] > 490 or self.pos[0] < 110:
            sx *= -1
            self.bounce = True
        if self.pos[1] > 490 or self.pos[1] < 110:
            sy *= -1
            self.bounce = True
        
        g, h = a - x, b - y 
        
        new_x = x + 500 * sx
        new_y = y + 500 * sy
        
        self.pos = (new_x,new_y)
        self.speed = (sx,sy)
    
    def change_color(self):
        print(self.current_color)
        if self.bounce == True:
            if self.current_color == "Red":
                self.bounce = False
                self.color = (40,240,40)
                self.current_color = "Green"
                print("hello")
            elif self.current_color == "Green":
                self.bounce = False
                self.color = (40,40,240)
                self.current_color = "Blue"
                print("hello")
            elif self.current_color == "Blue":
                self.bounce = False
                self.color = (240,40,40)
                self.current_color = "Red"
                print("hello")
    
                

def main():
    Tleft_corner = Point(100,100)
    Bleft_corner = Point(100,500)
    Tright_corner = Point(500,100)
    Bright_corner = Point(500,500)
    points = [Tleft_corner, Bleft_corner, Tright_corner, Bright_corner]
    running = True
    Win.fill(Grey)
    ball = Ball()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ball.change_color()
        ball.draw()
        ball.move()
        #print(ball.current_color)
        for point in points:
            point.draw()
        Tleft_corner.connect_point(Tright_corner.pos)
        Tleft_corner.connect_point(Bleft_corner.pos)
        Tright_corner.connect_point(Bright_corner.pos)
        Bleft_corner.connect_point(Bright_corner.pos)
        
        pygame.display.update()
        clock.tick(60)
main()