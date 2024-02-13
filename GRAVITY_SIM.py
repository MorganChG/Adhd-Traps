import math, os, pygame

WIN = pygame.display.set_mode((600,600))


def gforce(p1,p2):
  try:
    G = 2
    
    r_vec_x = p1.pos[0] - p2.pos[0]
    r_vec_y = p1.pos[1] - p2.pos[1]

    r_mag = math.sqrt(r_vec_x**2 + r_vec_y **2)

    r_hat_x = r_vec_x/r_mag
    r_hat_y = r_vec_y/r_mag

    force_mag = G * p1.mass * p2.mass/r_mag**2
    force_vec_x = -force_mag * r_hat_x
    force_vec_y = -force_mag * r_hat_y
    return (force_vec_x,force_vec_y)
  except OverflowError:
    pass

class Planet:
  def __init__(self, color, pos,momentum, mass, radius) -> None:
     self.pos = pos
     self.prev_pos = []
     self.color = color
     self.mass = mass
     self.momentum = momentum
     self.radius = radius
     self.dt = 0.02
  def draw(self):
    pygame.draw.circle(WIN,self.color,self.pos,self.radius)
  
  def draw_line(self):
    self.prev_pos.append(self.pos)
    for pos in self.prev_pos:
      pygame.draw.circle(WIN,(240,240,240),pos,1)
    
    if len(self.prev_pos) > 500:
      self.prev_pos.pop(0)
 
    
  def move(self, star, planet):
    p_force = gforce(self,star)
    p_force_2 = gforce(self,planet)
    self.momentum = ((self.momentum[0] + (p_force_2[0] + p_force[0]) * self.dt), (self.momentum[1] + (p_force_2[1] + p_force[1]) * self.dt))
    self.pos = ((self.pos[0] + self.momentum[0]/self.mass * self.dt), (self.pos[1] + self.momentum[1]/self.mass * self.dt))
     
class Star:
  def __init__(self) -> None:
    self.pos = (300,300)
    self.color = (240,240,80)
    self.mass = 75
    self.momentum = (0,0)
    self.radius = 10
    self.dt = 0.001
  
  def draw(self):
    pygame.draw.circle(WIN, self.color,self.pos,self.radius)
    
  def move(self,planet,planet_2):
    s_force = gforce(self,planet)
    s_force_2 = gforce(self,planet_2)
    self.momentum = ((self.momentum[0] + (s_force[0] + s_force_2[0]) * self.dt), (self.momentum[1] + (s_force[1] + s_force_2[1]) * self.dt))
    self.pos = ((self.pos[0] + self.momentum[0]/self.mass * self.dt), (self.pos[1] + self.momentum[1]/self.mass * self.dt))
    


def main():
  earth = Planet((40,240,40), (300,180), (25,0), 25, 5)
  mars = Planet((240,40,40), (300,165), (-0.9, 0), earth.mass/25, 2)
  sun = Star()
  
  
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False 
    WIN.fill((40,40,40))
    earth.draw_line()
    mars.draw_line()
    earth.draw()
    mars.draw()
    sun.draw()
    mars.move(sun,earth)
    earth.move(sun,mars)
    sun.move(earth,mars)
    
    pygame.display.update()
main()