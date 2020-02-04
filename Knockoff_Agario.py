import pygame, sys, time, random, math
from pygame.locals import *
fpsClock = pygame.time.Clock()

pygame.init()
w = 640
h = 480
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Knockoff Agario')
#pygame.mouse.set_visible(0)

#definitions
colourRed = pygame.Color(255,0,0)
colourBlue = pygame.Color(0,0,255)
colourGreen = pygame.Color(0,255,0)
colourWhite = pygame.Color(255,255,255)

drops = []
for i in range (50):
    drops.append ([random.randint(0,w),random.randint(0,h)])


#initial setup
done = False
(x,y) = pygame.mouse.get_pos()
colour = colourBlue
radius = 20
speed = 3
blob = [w/2, h/2]


while not done:
    screen.fill(colourWhite)
    for event in pygame.event.get():
        if (event.type == KEYUP) or (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                done = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == MOUSEMOTION:
            (rel_x, rel_y) = event.rel
            (x,y) = event.pos
        if event.type == MOUSEBUTTONUP:
            colour = colourBlue
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                colour = colourRed
            elif event.button == 2:
                colour = colourWhite
            elif event.button == 3:
                colour = colourGreen

    if math.fabs(x - blob[0]) > 3 or math.fabs(y - blob[1]) > 3: # Used to center the screen 
        if y - blob[1] != 0:
            theta = math.atan(math.fabs(x - blob[0])/ math.fabs(y - blob[1])) 
            new_dx = speed * math.sin(theta)
            new_dy = speed * math.cos(theta)

        if x > blob[0]:
            new_dx *= -1
        #blob[0] += new_dx
        
        if y > blob[1]:
            new_dy *= -1
        #blob[1] += new_dy    

        pygame.draw.circle (screen, colour,(int(blob[0]),int(blob[1])), radius, 0)
        for d in drops:
            d[0] += new_dx
            d[1] += new_dy
            pygame.draw.circle (screen, colourGreen, (int(d[0]),int(d[1])), 5, 0)
            dx = blob[0] - d[0]
            dy = blob[1] - d[1]
            dist = (dx ** 2 +  dy ** 2) ** .5
            if dist < radius:
                radius += 1
                drops.remove (d)
        pygame.display.update()
        fpsClock.tick(30)