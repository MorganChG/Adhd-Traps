import pygame, random, noise
Win = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class Perlin:
    @classmethod
    def generate_perlin_noise(cls, mapWidth,mapHeight, scale, seed , target_X, target_Y):
        if scale <= 0:
            scale = 0.01
        for y in range(mapHeight):
            for x in range(mapWidth):
                sampleX = (x * scale) + target_X
                sampleY = (y * scale) + target_Y
                
                noiseValue = abs(noise.pnoise2(sampleX, sampleY, octaves = 6, persistence = 0.4, lacunarity=4.5,base = seed) * 240)
                
                rect = pygame.Rect(x, y,1,1)
                
                if noiseValue < 1:
                    pygame.draw.rect(Win, (40,40,200), rect)
                if noiseValue > 1:
                    pygame.draw.rect(Win, (40,40,240), rect)
                if noiseValue > 5:
                    pygame.draw.rect(Win, (240,200,140), rect)
                if noiseValue > 10:
                    pygame.draw.rect(Win, (140,240,140), rect)
                if noiseValue > 30:
                    pygame.draw.rect(Win, (40,200,40), rect)
                if noiseValue > 50:
                    pygame.draw.rect(Win, (40,40,40), rect)
                if noiseValue > 80:
                    pygame.draw.rect(Win, (240,240,240), rect)
                
                
                



def main():
    run = True
    Win.fill((40,40,40))
    seed = random.randint(0,100)
    x = 0
    y = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x += 1
                if event.key == pygame.K_LEFT:
                    x -= 1
                if event.key == pygame.K_UP:
                    y -= 1
                if event.key == pygame.K_DOWN:
                    y += 1
        
        Perlin.generate_perlin_noise(600, 600, 0.004, seed, x, y)
        clock.tick(120)
        pygame.display.update()
main()
