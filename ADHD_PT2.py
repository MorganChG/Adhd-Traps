import pygame
import random

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
SCREEN_CAPTION = pygame.display.set_caption("Grass Genorator")
CLOCK = pygame.time.Clock()
    

class Tile:
    def __init__(self, starting_position) -> None:
        self.color = (40,40,40)
        self.starting_position = starting_position
        self.positions = []
        self.previous_pos = []
        self.rects = []
        self.positions.append(self.starting_position)
        self.previous_dir = ""
    
    def is_previous_position(self,position):
        for i in range(len(self.previous_pos)):
            if position == self.previous_pos[i]:
                return True
        return False
    
    def move(self):
        new_pos = []
        if len(self.positions) > 1000000:
            self.positions.clear()
            SCREEN.fill((240,240,240))
            #self.color = (random.randrange(40,240,10),random.randrange(40,240,10),random.randrange(40,240,10))
            self.positions.append(self.starting_position)
        for i in range(len(self.positions)):
            
            nCheck = random.randint(0,100)
            sCheck = random.randint(0,100)
            wCheck = random.randint(0,100)
            eCheck = random.randint(0,100)
            
            if nCheck > 50 and self.previous_dir != "N":
                NPOSY = self.positions[i][1] + -10
                if self.is_previous_position((self.positions[i][0], NPOSY)) == False:
                    new_pos.append((self.positions[i][0], NPOSY))
                    self.previous_dir = "N"
            
            if sCheck > 50 and self.previous_dir != "S":
                SPOSY = self.positions[i][1] + 10
                if self.is_previous_position((self.positions[i][0], SPOSY)) == False:
                    new_pos.append((self.positions[i][0], SPOSY))
                    self.previous_dir = "S"
            
            if wCheck > 50 and self.previous_dir != "W":
                WPOSX = self.positions[i][0] + -10
                if self.is_previous_position((WPOSX, self.positions[i][1])) == False:
                    new_pos.append((WPOSX, self.positions[i][1]))
                    self.previous_dir = "W"
            
            if eCheck > 50 and self.previous_dir != "E":
                EPOSX = self.positions[i][0] + 10
                if self.is_previous_position((EPOSX, self.positions[i][1])) == False:
                    new_pos.append((EPOSX, self.positions[i][1]))
                    self.previous_dir = "E"
            
            try:
                rect = pygame.Rect(new_pos[i][0],new_pos[i][1],10,10)
                pygame.draw.rect(SCREEN,self.color, rect)
                
            except IndexError:
                pass
            
        if len(new_pos) >= 3:
            self.previous_pos = self.positions
            self.positions = new_pos
            #self.color = (random.randrange(40,240,10),random.randrange(40,240,10),random.randrange(40,240,10))
    
            

def main():
    running = True
    SCREEN.fill((240,240,240))
    tile = Tile((300,300))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        tile.move()

        pygame.display.update()  
        #SCREEN.fill((240,240,240)) 
        CLOCK.tick(30)
main()