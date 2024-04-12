import pygame

Win = pygame.display.set_mode((600,600), pygame.NOFRAME)


class Bubble:
    def __init__(self, x, y):
        self.pos = (x,y)
        self.radius = 10
        
        self.defaultColor = (80,80,80)
        self.highlightColor = (160,160,160)
        self.popColor = (200,200,200)
        self.color = self.defaultColor
        
        self.color_choices = ['R', 'G', 'B', 'W']
        self.cycleCount = 3
        self.currentColor = self.color_choices[self.cycleCount]
        
        self.popped = False
    
    def draw(self):
        pygame.draw.circle(Win, self.color, self.pos, self.radius)
    
    def pop(self):
        mousePos = pygame.mouse.get_pos()
        mouseState = pygame.mouse.get_pressed()
        
        distanceFromBubbleX = abs(mousePos[0] - self.pos[0])
        distanceFromBubbleY = abs(mousePos[1] - self.pos[1])
        
        clicked = False

        if (distanceFromBubbleX < 10 and distanceFromBubbleY < 10 and self.popped == False):
            self.color = self.highlightColor
            if (mouseState[0] and clicked == False):
                clicked = True
                self.popped = True
                self.color = self.popColor
        else: 
            if (self.popped == False):
                self.color = self.defaultColor
    
    def change_color(self):
        
        self.cycleCount += 1
        if self.cycleCount >= 4:
            self.cycleCount = 0
        self.currentColor = self.color_choices[self.cycleCount]
            
        
        if self.currentColor == 'R':
            self.highlightColor= (160,40,40)
            self.popColor = (200,40,40)
        elif self.currentColor == 'G':
            self.highlightColor= (40,160,40)
            self.popColor = (40,200,40)
        elif self.currentColor == 'B':
            self.highlightColor= (40,40,160)
            self.popColor = (40,40,200)
        else:
            self.highlightColor = (160,160,160)
            self.popColor = (200,200,200)

def create_bubbles():
    bubbles = []
    offset = 20
    
    for i in range(0,35):
        for j in range(0,35):
            bubbles.append(Bubble(i * offset,j * offset))

    return bubbles

def bubble_operations(bubbles, bool):
    for bubble in  bubbles:
            bubble.draw()
            bubble.pop()
            if bool:
                bubble.change_color()
        

def main():
    
    Win.fill((20,20,20))
    
    run = True
    bubbles = create_bubbles()
    button_pressed = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bubbles = create_bubbles()
                if event.key == pygame.K_BACKSPACE:
                    run = False
                if event.key == pygame.K_c:
                    button_pressed = True
                    print(button_pressed)
        
        bubble_operations(bubbles, button_pressed)
        if button_pressed:
            button_pressed = False
            print(button_pressed)

        
        pygame.display.update()
main()