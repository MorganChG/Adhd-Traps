import pygame

Win = pygame.display.set_mode((600,600), pygame.NOFRAME)
clock = pygame.time.Clock()

class Bubble:
    def __init__(self, pos) -> None:
        self.pos = pos
        
        self.ring_color = (240,240,240)
        self.backgd_color = (40,40,40)
        
        self.radius = 0
        self.backgd_radius = -1
    
    def draw(self):
        pygame.draw.circle(Win, self.ring_color, self.pos, self.radius)
        pygame.draw.circle(Win, self.backgd_color, self.pos, self.backgd_radius)
    
    def grow(self):
        self.radius += 1
        self.backgd_radius += 1.007
    
    def delete(self):
        if self.backgd_radius > self.radius:
            return True
        return False
    
    #def set_color(self, idx):
        #self.ring_color = (2*idx,80,idx) if (2*idx < 240) else (idx,80,idx)


def check_mouse_input(event):
    if event.type == pygame.MOUSEMOTION:
        return True
    return False

#def check_close_window(event, bool):
    #if event.type == pygame.QUIT:
        #bool = False
    #return bool
#
def check_exit_button(event, bool):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            bool = False
    return bool

def check_change_button(event, bool):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:
            if bool: bool = False
            else: bool = True
    return bool
    
def create_bubble(queue, bool):
    bubble = Bubble(pygame.mouse.get_pos())
    if bool:
        queue.append(bubble)
    queue.insert(0, bubble)
    return queue

def queue_draw(queue):
    for index,bubble in enumerate(queue):
        #bubble.set_color(index)
        bubble.draw()
        if bubble.delete():
            queue.pop(index)
        bubble.grow()
        

def main():
    run = True
    tail = True
    queue = []
    while run:
        for event in pygame.event.get():
            run = check_exit_button(event, run)
            tail = check_change_button(event, tail)
            if check_mouse_input(event):
                create_bubble(queue, tail)
        
        queue_draw(queue)
        
        pygame.display.update()
        clock.tick(240)
        Win.fill((40,40,40))
        
main()