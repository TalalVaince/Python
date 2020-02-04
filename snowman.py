#Import and making the fps
import pygame, sys, time,random
from pygame.locals import *
from pygame.constants import *
fps = pygame.time.Clock()
pygame.init()

#Colors 
colorWhite = pygame.Color(255,255,255)
colorBlue = pygame.Color(0,0,255)
colorOrange = pygame.Color(255,179,0)
colorBlack = pygame.Color(0,0,0)
#Making the Screen Length 
w = 800
h = 600
screen  =  (pygame.display.set_mode((w, h)))
pygame.display.set_caption ('SnowMan')
#Creating A Function to create SnowMans
def drawSm(x,y,r,rec):
    arms = int(r*.14)
    eyes = int(r*0.15)
    r2 = int(r * 1.2)
    r3 = int(r2*1.3)
    #Body
    pygame.draw.circle(screen,colorWhite,(x,y),r)
    pygame.draw.circle(screen,colorWhite,(x,(y+(r*2))),r2)
    pygame.draw.circle(screen,colorWhite,(x,(y+(r * 4))),r3)
    #Eyes
    pygame.draw.circle(screen,colorBlack,((x+20),y-10),eyes)
    pygame.draw.circle(screen,colorBlack,((x-20),y-10),eyes)
    #Buttons
    pygame.draw.circle(screen,colorBlack,(x,(y+(r*2)+20)),eyes)
    pygame.draw.circle(screen,colorBlack,(x,(y+(r*2))),eyes)
    pygame.draw.circle(screen,colorBlack,(x,(y+(r*2)-20)),eyes)
    #Arms
    pygame.draw.rect(screen,(153,76,0),(x+60+(rec),(y+(r*2)-10),90+(r-50),5+(arms-7)))
    pygame.draw.rect(screen,(153,76,0),(x-148-(rec),(y+(r*2)-10),90+(r-50),5+(arms-7)))
    pygame.draw.rect(screen,(153,76,0),(x+130+(rec),(y+(r*2)-26),5,40))
    pygame.draw.rect(screen,(153,76,0),(x-130-(rec),(y+(r*2)-26),5,40))
    #Nose
    pygame.draw.polygon(screen, colorOrange,[[x+10, y], [x-1, y+20],[x-10,y ]],)
    #Hat
    pygame.draw.rect(screen,(0,0,0),((x-50),(y+r*-1),(100+(r-60)),5))
    pygame.draw.rect(screen,(0,0,0),(x-35,(y+(r*-2-5)),(70+(r-50)),60+(r-50)))

#Creating Necessary things for the program
dirx= 0
diry = 0
r = 50
x = 400
y = 300
rec = 0 
while True:
    #Main Loop
    #Filling the Screen 
    screen.fill(colorBlue)
    x += dirx
    y+= diry
    drawSm(x,y,r,rec)
    #Drawing Boundaries
    if x + r > w or x - r  < 0:
        dirx *= 0
    if y + int(((r*1.2)*1.3)*3.5) > h or y - int(((r*1.2)*1.3)*1.3) < 0:
        diry *= 0
    #Main Loop
    for event in pygame.event.get():
        
        print (event)
        #Exit 
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()
        #Movement of SnowMan 
        #Adjusting size
        if (event.type == KEYDOWN):
            if (event.key == (pygame.K_EQUALS)):
                r += 5
                rec += 10
            if (event.key == (pygame.K_MINUS)):
                if r > 5:
                    r -= 5
                    rec -= 10
            #KeyBoard Arrows
            if (event.key == 276): #LEFT
                dirx = -6
            if (event.key == 275): #RIGHT
                dirx = 6
            if (event.key == 273): #UP
                diry  = -6
            if (event.key == 274): #DOWN
                diry = 6
        if (event.type == KEYUP):
            #Adjusting Size 
            if (event.key == (pygame.K_EQUALS)):
                r += 0 
            if (event.key == (pygame.K_MINUS)):
                r += 0 
            #KeyBoard Arrows
            
       
    #Updating the screen
    pygame.display.update()
    fps.tick(30)