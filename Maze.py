import pygame, random


display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

WHITE = (240,240,240)
BLACK = (40,40,40)

class Cell:
    def __init__(self,pos) -> None:
        self.color = BLACK
        self.x, self.y = pos
        self.walls = ["top","bottom","left","right"]
        self.walls_color = (100,100,100)
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width,self.height)
    
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)
        for wall in self.walls:
            if wall == "top":
                pygame.draw.line(display, self.walls_color, (self.x, self.y), (self.x + self.width, self.y), 1)
            if wall == "bottom":
                pygame.draw.line(display, self.walls_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 1)
            if wall == "left":
                pygame.draw.line(display, self.walls_color, (self.x, self.y), (self.x, self.y + self.height), 1)
            if wall == "right":
                pygame.draw.line(display, self.walls_color, (self.x + self.width, self.y), (self.x + self.width , self.y + self.height), 1)
    
    def return_pos(self):
        return(self.x, self.y)
    
    def return_walls(self):
        return(self.walls)
    
    
    
def main():
    run = True
    cells = []
    display.fill(BLACK)
    for x in range(0, 600, 30):
        for y in range(0, 600, 30):
            cell = Cell((x, y))
            cell.walls.pop(random.randint(0,3))
            cells.append(cell)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for cell in cells:
            cell.draw()
        pygame.display.update()
        clock.tick(60)
main()