import pygame, random

Win = pygame.display.set_mode((600,600), pygame.NOFRAME)
Clock = pygame.time.Clock()

class Bubble:
    def __init__(self, delay):
        self.pos = (random.randrange(0,600, 10), random.randrange(0,600, 10))
        self.maxRadius = 25
        self.fillMaxRaidus = 23
        self.radius = 1
        self.fillRaidus = 0
        
        self.grow = True
        self.delay = delay

        
        
        self.color = (240,240,240)
        self.backgroundColor = (40,40,40)
    
    def draw(self):
        pygame.draw.circle(Win, self.color, self.pos, self.radius)
        pygame.draw.circle(Win, self.backgroundColor, self.pos, self.fillRaidus)
    
    def growShrink(self):
        self.draw()
        if self.delay >= 1:
            self.delay -= 1
        if self.grow and self.delay == 0:
            self.radius += 1.1
            self.fillRaidus += 1
        
            if self.radius >= self.maxRadius:
                self.grow = False
        else:
            self.radius -= 1.1
            self.fillRaidus -= 1
            if self.radius <= 0:
                self.pos = (random.randrange(0,600, 10), random.randrange(0,600, 10))
                self.grow = True
                self.delay = random.randrange(0,30)
                

def createBubbles():
    bubbles = []
    for i in range(175):
        bubbles.insert(0,Bubble(random.randrange(0,30)))
    return bubbles

def bubbleOperation(bubbles):
    for bubble in bubbles:
        bubble.growShrink()
def main():
    run = True
    bubbles = createBubbles()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    run = False
        Win.fill((40,40,40))
        bubbleOperation(bubbles)      
        pygame.display.update()
        Clock.tick(30)
main()