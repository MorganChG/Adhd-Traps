import pygame

Win = pygame.display.set_mode((1920,1200), pygame.NOFRAME)
clock = pygame.time.Clock()

class Square:
    def __init__(self, pos) -> None:
        self.x, self.y = pos
        
        self.width = 10
        self.height = 10
        
        self.r_weight = 1
        self.b_weight = 1
        self.r_max = False
        
        self.r = 0
        self.b = (self.y/10) * self.b_weight
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
        self.color = (self.r, 0, self.b)
        
    
    def draw(self):
        pygame.draw.rect(Win, self.color, self.rect)
        
    def gradient_shift(self):
        if self.r_max == False:
            self.r += 1
            if self.r >= 240:
                self.r_max = True
        else:
            self.r -= 2
            if self.r <= 0:
                self.r_max = False
        self.color = (self.r, 0, self.b)
        self.draw()
        
    

def check_exit_button(event, bool):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            bool = False
    return bool

def create_squares():
    squares = []
    for i in range(0,1920,10):
        for j in range(0,1200,10):
            squares.append(Square((i,j)))
    return squares

def draw_squares(queue):
    for ele in queue:
        ele.draw()
        ele.gradient_shift()
        
def change_square_color(queue):
    for ele in queue:
        ele.gradient_shift()
    

def main():
    
    run = True
    queue = create_squares()
    draw_squares(queue)
    while run:
        for event in pygame.event.get():
            run = check_exit_button(event, run)
        change_square_color(queue)
        pygame.display.update()
        clock.tick(30)
main()
    