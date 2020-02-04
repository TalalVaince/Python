#Necessary for Pygame to operate 
import pygame, sys, time, random, math
from pygame.locals import *
fpsClock = pygame.time.Clock()
pygame.mixer.init()
pygame.init()

#Creates the screen Length
w = 800 
h = 600
screen = pygame.display.set_mode((w,h)) 
#Importing Background
image = pygame.image.load("max.jpg")
play_image = pygame.image.load('ahah.jpg')
#Names 
pygame.display.set_caption('Tron')
#Allows Music to play
pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
#Colors 
White = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
grey = pygame.Color(96,96,96)

#Title
font2 = pygame.font.Font('freesansbold.ttf', 70)
text = font2.render('Tron', True, blue)
textstart = text.get_rect()
textstart.center = (w//2,h//2*0.5)
#Needed to keep track of score
score1 = 0 
score2 = 0
#Neeeded to Change Controls
P1_controls = 0
P2_controls = 0
#Necessary to create text
def text_objects(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()
def text_objects2(text, font):
    textSurface = font.render(text, True,White)
    return textSurface, textSurface.get_rect()

#A Function that allows me to create text
def message_display(text,size,x,y,text_objects):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((w//x),(h//y))
    screen.blit(TextSurf, TextRect)
#A Function that allows to create
def buttons(x,y,x2,y2,color):
    pygame.draw.rect(screen,(color),((x),(y),x2,y2))
#The Bike(aka square) that the player controls is created into function to make it easier to reference throughout the game
def lightbike(color,x,y):
    pygame.draw.rect(screen,(color),((x),(y),5,5))
def how_to_play():
    joystick_count = pygame.joystick.get_count()

    while True:
        screen.fill(White)
        screen.blit(image, (-240,-100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mouse = pygame.mouse.get_pos()#Obtains the current position of the mouse
        click = pygame.mouse.get_pressed()#See's if the user clicks something on the mouse
        #Green Going to toucg Himself 
        pygame.draw.line(screen,green,(100,500),(200,500),4)
        pygame.draw.line(screen,green,(100,500),(100,550),4)
        pygame.draw.line(screen,green,(100,550),(200,550),4)
        pygame.draw.line(screen,green,(200,550),(200,510),4)
        #Green Hitting Blue
        pygame.draw.line(screen,green,(400,500),(500,500),4)
        pygame.draw.line(screen,blue,(500,500),(500,590),4)
        #Text
        message_display("Do not Touch Yourself, Or you Die",25,2,2,text_objects2)
        message_display("Do not Touch Your Opponent, Or you Die",25,2,1.7,text_objects2)
        message_display("You Move with Arrow Keys, WASD and the Joysticks",25,2,1.5,text_objects2)
        for i in range(joystick_count):#Goes through the amount of joysticks found
            joystick = pygame.joystick.Joystick(i)#Shows pygame that these are joysticks
            joystick.init()
            if joystick.get_button (0): # if the first button is pressed it will also return the user to the main screen
                intro()
        #Back Button
        if 690 + 100 > mouse[0] > 690 and 20 + 50 > mouse[1] > 20: 
            buttons(690,20,100,50,grey)
            if click[0] == 1:
                intro()
        else:

            buttons(690,20,100,50,black) 
        message_display("Back",20,1.08,13,text_objects2)
        
        pygame.display.update() 
        fpsClock.tick(30)
#These are the controls for Player 1
def controls_1(x):
    x = 1 # The Parameter is set to one to later be used 
    z = 0 # Z is used for certain scenieros 
    joystick_count = pygame.joystick.get_count() #This command collects the amount of joysticks connected to the console 
    while True: 
        #Main Loop
        screen.fill(White)#fills the screen with white
        for event in pygame.event.get(): #The For loop that gathers all the information through the interaction of buttons on the computer
            if event.type == pygame.QUIT: #Allows the user to quit the game when the "x" button is clicked 
                pygame.quit()
                sys.exit(0)
        mouse = pygame.mouse.get_pos()#Obtains the current position of the mouse
        click = pygame.mouse.get_pressed()#See's if the user clicks something on the mouse 
        #Controls Box
        pygame.draw.line(screen,black,(300,500),(500,500),1) #Creates lines to create a box that does not have a color filled inside of it 
        pygame.draw.line(screen,black,(300,400),(500,400),1)
        pygame.draw.line(screen,black,(300,400),(300,500),1)
        pygame.draw.line(screen,black,(500,400),(500,500),1)
        #Triangle 1
        if 260 + 30 > mouse[0] > 260 and 400 + 100 > mouse[1] > 400: # This If statement basically says if the mouse position is in this area change the color of the triangle 
            pygame.draw.polygon(screen,grey,[[290,400],[290,500],[260,450]])#The draw function that creates the triangle 
            if click[0] == 1: # If the user lefts clicks it will gather this information 
                x -= 1  # Scrolls through the options    
        else: #If mouse position isn't in the triangles area, it will change the triangles color
            pygame.draw.polygon(screen,black,[[290,400],[290,500],[260,450]])
            
        # Triangle 2 
        if 510 + 30 > mouse[0] > 510 and 400 + 100 > mouse[1] > 400: 
            pygame.draw.polygon(screen,grey,[[510,400],[510,500],[540,450]])
            if click[0] == 1:
                x += 1 # Scrolls the other way
        else:
            pygame.draw.polygon(screen,black,[[510,400],[510,500],[540,450]])
        # This right here allows me to create the scrolling mechanism 
        if x == 1: #X is originally set as 1 so the first thing that appears is arrow keys
            message_display("Arrow Keys",35,2,1.33,text_objects)
        if x == 2:
            message_display("JoyStick(1)",35,2,1.33,text_objects)
            if joystick_count == 0: # This basically states that if no joystick is found, it will give this message 
                message_display("JoyStick Not Found",10,2,1.44,text_objects)

        if x == 3:
            message_display("JoyStick(2)",35,2,1.33,text_objects)
            if joystick_count <= 1: #This is for the second joystick
                message_display("JoyStick Not Found",10,2,1.44,text_objects)
        #Avoiding blank spaces
        if x > 3: #If you were to click more then joystick(2), this conditional statement bring the user back to arrow keys
            x = 1
        if x <= 0: #If you were to click the left triangle while you were at the arrow keys, this would bring you to joystick(2)
            x = 3 
        if x == 3 and joystick_count <= 1: #If 1 joystick was detected and the player some reason chooses joystick(2), it will not let them play
            z = 1
        elif x == 2 and joystick_count == 0: #same goes for this, if no joysticks were detected and they still choose joystick(1), it will not let them play
            z = 1 
        else:
            z = 0 # if these conditions do not occur, the play button will be available 
        if z == 0:
            if 300 + 200 > mouse[0] > 300 and 100 + 100 > mouse[1] > 100:
                buttons(300,100,200,100,grey)
                if click[0] == 1:
                    AI_GAME(score2,score1,P1_controls+x) #This bring them to the game and the +x allow the function to see what controls to use 
            else: # This else statement basically change the color back to black when the mouse is not over it 
                buttons(300,100,200,100,black)
            message_display("Play",20,2,4,text_objects2)
            
            
        #Back Button
        if 690 + 100 > mouse[0] > 690 and 20 + 50 > mouse[1] > 20: 
            buttons(690,20,100,50,grey)
            if click[0] == 1:
                play() #Bring you back to the place where you can choose 2 player or 1 player
        else:

            buttons(690,20,100,50,black) 
        message_display("Back",20,1.08,13,text_objects2)
        
        #Needed for a screen to play 
        pygame.display.update() 
        fpsClock.tick(30)
def controls_2(x,y):#This is the screen available for two player, it allows to change the controls for each player hence the reason it has two parameters
    x = 1 #Player1
    y = 1 #Player2
    z = 0 # See if there are nothing that can interfere in the game outcome 
    joystick_count = pygame.joystick.get_count() # counts the amount of joysticks 
    while True:
        #Main Loop
        screen.fill(White)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Player 1 Box
        pygame.draw.line(screen,black,(100,500),(300,500),1)
        pygame.draw.line(screen,black,(100,400),(300,400),1)
        pygame.draw.line(screen,black,(100,400),(100,500),1)
        pygame.draw.line(screen,black,(300,400),(300,500),1)
        #THe arrows that allow you to switch through each control option for Player 1 
        if 60 + 30 > mouse[0] > 60 and 400 + 100 > mouse[1] > 400: # Any coding like this basically says that if you go over a button it will change colors and allow you to click it 
            pygame.draw.polygon(screen,grey,[[90,400],[90,500],[60,450]])
            if click[0] == 1:
                x -= 1 #For the left
        else:
            pygame.draw.polygon(screen,black,[[90,400],[90,500],[60,450]])
        if 310 + 30 > mouse[0] > 310 and 400 + 100 > mouse[1] > 400:
            pygame.draw.polygon(screen,grey,[[310,400],[310,500],[340,450]])
            if click[0] == 1:
                x += 1 # For the right 
        else:
            pygame.draw.polygon(screen,black,[[310,400],[310,500],[340,450]])
        #Player 2 Box
        pygame.draw.line(screen,black,(500,500),(700,500),1)
        pygame.draw.line(screen,black,(500,400),(700,400),1)
        pygame.draw.line(screen,black,(500,400),(500,500),1)
        pygame.draw.line(screen,black,(700,400),(700,500),1)
        #The arrows that allow you to switch through each control option for Player 2 
        #Arrow 1 
        if 460 + 30 > mouse[0] > 460 and 400 + 100 > mouse[1] > 400:
            pygame.draw.polygon(screen,grey,[[490,400],[490,500],[460,450]])
            if click[0] == 1:
                y -= 1 #For the Left
        else:
            pygame.draw.polygon(screen,black,[[490,400],[490,500],[460,450]])
        #Arrow 2
        if 710 + 30 > mouse[0] > 710 and 400 + 100 > mouse[1] > 400:
            pygame.draw.polygon(screen,grey,[[710,400],[710,500],[740,450]])
            if click[0] == 1:
                y += 1 #For the Right
        else: 
            pygame.draw.polygon(screen,black,[[710,400],[710,500],[740,450]])
        
        
        
        # Player 1 Box
        if x == 1: 
            message_display("Arrow Keys",35,4,1.33,text_objects)
        if x == 2 : #in this case, it is not 3 due to the fact there are 2 options 
            message_display("JoyStick(2)",35,4,1.33,text_objects)
            if joystick_count <= 1:
                message_display("JoyStick Not Found",10,4,1.4,text_objects)
        if x <= 0: #If left is pressed too much, it will bring them back to Joystick(2)
            x = 2
        if x > 2:
            x = 1 
        #Player 2 Box
        if y == 1:
            message_display("WASD",35,1.33,1.33,text_objects)

        if y == 2:
            message_display("JoyStick(1)",35,1.33,1.33,text_objects)
            if joystick_count == 0:
                message_display("JoyStick Not Found",10,1.33,1.4,text_objects)
        if y <= 0:
            y = 2
        if y > 2:
            y = 1 
        #Making Certain Scenario's Not happen
        
        if joystick_count == 0 and x == 2 or joystick_count == 0 and y == 2: #only one is found due to the fact that if one joystick is detected, that will be that only thing that matters for this case
            z = 1
        else: 
            z = 0
        
            
        #Play
        if z == 0: # If nono of those scenarios are found, everything goes regularly
            if 300 + 200 > mouse[0] > 300 and 100 + 100 > mouse[1] > 100: 
                buttons(300,100,200,100,grey)
                if click[0] == 1:
                    game_loop(score2, score1,P1_controls+x,P2_controls+y) #This brings the player to the main game loop. + y determines which controls for player2 and + x is for player 1 
                    
            else: 
                buttons(300,100,200,100,black)
            message_display("Play",20,2,4,text_objects2)
            
        #Back Button
        if 690 + 100 > mouse[0] > 690 and 20 + 50 > mouse[1] > 20: #The inclusion of the back button allows you to go back to the play menu
            buttons(690,20,100,50,grey)
            if click[0] == 1:
                play() 
        else:
            buttons(690,20,100,50,black) 
        message_display("Back",20,1.08,13,text_objects2)
        
        #needed for pygame to run 
        pygame.display.update()
        fpsClock.tick(30)
def play():#This screen allows you to choose either single player or 2 player 
    while True:
        screen.fill(White)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(play_image, (-100,-1000))#Puts  an image as the background
        screen.blit(text, textstart) #This is so the title screen Remains in the same spot 
        #2 Player
        if 450 + 300 > mouse[0] > 450 and 400 + 100 > mouse[1] > 400: # if the mouse hovers over the button, the button will change to green indicating you are over the button 
            buttons(450,400,300,100,green)
            if click[0] == 1: # if you left click, it will bring you to the 2 player menu 
                controls_2(P1_controls,P2_controls) # Needed parameters 
        else:
            buttons(450,400,300,100,red) #if no mouse is over it, it becomes red 
        #1 Player
        if 50 + 300 > mouse[0] > 50 and 400 + 100 > mouse[1] > 400:#Samething goes for player 1 box
            buttons(50,400,300,100,green)
            if click[0] == 1: # if you left click, it will bring you to the 1 player menu 
                controls_1(P1_controls)
        else:
            buttons(50,400,300,100,red)
        #Back Button
        if 30 + 100 > mouse[0] > 30 and 20 + 50 > mouse[1] > 20:
            buttons(30,20,100,50,grey)
            if click[0] == 1:
                intro()
        else:
            buttons(30,20,100,50,black)
        #Text to show what these buttons are 
        message_display("Back",20,10,13,text_objects2)
        message_display("Two Player",40,1.33,1.33,text_objects)
        message_display("One Player",40,4,1.33,text_objects)
        pygame.display.update()
        fpsClock.tick(30)
        
        
def Blue_Wins(): #If Blue Wins this screen will pop up 
    while True:
        screen.fill(black)
        message_display("Blue Wins!!!",70,2,2,text_objects2)#This is the text the displays the blue wins
        message_display("Press Enter",30,4,4,text_objects2)#Indicates the user to press enter 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows user to quit 
                pygame.quit()
                sys.exit(0)
            if (event.type == KEYDOWN): # If a button is pressed 
                if (event.key == K_RETURN): # if enter is pressed
                    intro()#Returns the user to the main screen 
        joystick_count = pygame.joystick.get_count() #Counts how many joysticks are detected 
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            if joystick.get_button (0): # if the first button is pressed it will also return the user to the main screen
                intro()
        if joystick_count >= 1: #If there are joysticks found, it will display this text
            message_display("Press the Red Button(0)",30,4,5,text_objects2)

        pygame.display.update()
        fpsClock.tick(30)
def Green_Wins(): # if Green Wins this screen will pop up. Same code to the Blue_Wins but the text is different 
    while True:
        screen.fill(black)
        message_display("Green Wins!!!",70,2,2,text_objects2)
        message_display("Press Enter",30,4,4,text_objects2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if (event.type == KEYDOWN):
                if (event.key == K_RETURN):
                    intro()
        joystick_count = pygame.joystick.get_count() 
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            if joystick.get_button (0):
                intro()
        if joystick_count >= 1:
            message_display("Press the Red Button(0)",30,4,5,text_objects2)
        pygame.display.update()
        fpsClock.tick(30)

def intro(): #Main Menu 

    intro = True

    while intro == True:
        screen.fill(White)
        screen.blit(image, (-240,-100))
        for event in pygame.event.get():
            
            if (event.type == KEYUP) or (event.type == KEYDOWN):
                if (event.key == K_ESCAPE): # If the escape is pressed, the game will end 
                    intro = False 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mouse = pygame.mouse.get_pos() #Gets the mouse position 
        click = pygame.mouse.get_pressed() # Tracks the clicks of a mouse 
        
            
        #Play
        if 115 + 90 > mouse[0] > 115 and 280 + 42 > mouse[1] > 280:
            buttons(115,280,90,42,green)
            if click[0] == 1:
                play() #Directs the user to the play menu 
        else:
            buttons(115,280,90,42,red)
            
        #Options
        if 76 + 180 > mouse[0] > 76 and 347 + 57 > mouse[1] > 347:
            buttons(76,347,180,57,green)
            if click[0] == 1:
                how_to_play()#directs the user to the options menu
        else: 
            buttons(76,347,180,57,red)
            
        #Quit
        if 116 + 90 > mouse[0] > 116 and 430 + 90 > mouse[1] > 430:
            buttons(116,430,90,55,green)
            if click[0] == 1:
                pygame.quit() # Allows the user to quit the program if they do not desire to play 
                sys.exit(0)
        else:
            buttons(116,430,90,55,red)
        #Text
        screen.blit(text, textstart)#Title Screen 
        message_display("How to Play",30,4.7,1.6,text_objects)
        message_display("Play",40,5,2,text_objects)
        message_display("Exit",40,5,1.3,text_objects)
        #Needed
        pygame.display.update()
        fpsClock.tick(30)
        
def game_loop(score2, score1,P1_controls,P2_controls): #The first parameter is player2 score, the second is player 1 score and the other 2 parameters are their controls which they chose previously.
    # The speed must be 5 due to the fact that the length of the lightbike is 5. Collision works better this way 
    speedP1,speedPN1 = 5,-5 # The speed of the P1(player 1)
    speedP2, speedPN2 = 5, -5# The speed of P2(player 2)
    
    dir_x = speedPN1 #Tron starts with both player approaching each other 
    dir_y = 0
    dir_x2 = speedP2
    dir_y2 = 0
    
    x = 600 # Original x Coordinate of P1
    y = 300 # Original y Coordinate of P1
    x2 = 200# Original x Coordinate of P2
    y2 = 300# Original y Coordinate of P2
    
    
    main_loop = True
    
    list1 = []#P1 coordinates are stored in List 1 while P2 coordinates are stored in list2
    list2 = []
    
    
    player1_score = 0 #This is used later to determine who wins in the game 
    player2_score = 0
    
    
    
    while main_loop == True: 
            #Main loop
            screen.fill(black)
            #This constantly updates the coordinates of P1(basically the reason they move)
            x += dir_x 
            y += dir_y
            #This constantly updates the coordinates of P1(basically the reason they move)
            x2 += dir_x2
            y2 += dir_y2
            #Displays the score of each player
            message_display(str(score1),20,1.9,12,text_objects2)
            message_display(str(score2),20,2.1,12,text_objects2)
            message_display((":"),20,2,12,text_objects2)
            #The lightbike of each player
            lightbike(blue,x,y)
            lightbike(green,x2,y2)
            #stores all the coordinates of the players in these two list
            list1.append([x,y])
            list2.append([x2,y2])
           
            #Joystick
            joystick_count = pygame.joystick.get_count() #Get the amount of Joysticks 
            for i in range(joystick_count):#Goes through the amount of joysticks found
                joystick = pygame.joystick.Joystick(i)#Shows pygame that these are joysticks
                joystick.init()
                if P2_controls == 2: #Here is where controls selection comes to play. If y was equal to 2 in controls_2, this is the result, allows you to control joystick(1)
                    if i == 0:#Joystick 1
                            if round(joystick.get_axis(0)) == 1: #UP
                                if dir_y2 == 0:#This basically disallows the user from kill himself by just going up and down(aka going inside of itself)
                                    dir_y2  = speedPN2 #Adjusts the speed of the light bike to dir_y2 which is then added to y2 which move the lightbike
                                if dir_x2 != 0: #Doesn't let the user go Diagonally 
                                    dir_x2 = 0
                            if round(joystick.get_axis(0)) == -1:#DOWN
                                if dir_y2 == 0:
                                    dir_y2 = speedP2
                                if dir_x2 != 0:
                                    dir_x2 = 0
                                    
                            if round(joystick.get_axis(1)) == -1:#RIGHT
                                if dir_x2 == 0: #Restricts the users from killing himself horizontally 
                                    dir_x2 = speedPN2
                                if dir_y2 != 0: #Restricts the user from going Diagonally 
                                    dir_y2 = 0
                            if round(joystick.get_axis(1)) == 1:#LEFT
                                if dir_x2 == 0:
                                    dir_x2 = speedP2
                                if dir_y2 != 0:
                                    dir_y2 = 0
                if P1_controls == 2:# If control selection had x == 2 aka player 1 choosing joystick(2)
                        if i == 1:#Joystick 2  
                            #Same concept but everything is applied to dir_x and dir_y instead of dir_x2 and dir_y2. 
                            if round(joystick.get_axis(0)) == 1:#UP
                                if dir_y == 0:
                                    dir_y  = speedPN1
                                if dir_x != 0:
                                    dir_x = 0
                            if round(joystick.get_axis(0)) == -1:#DOWN
                                if dir_y == 0:
                                    dir_y = speedP1
                                if dir_x != 0:
                                    dir_x = 0
                            if round(joystick.get_axis(1)) == -1: #Right 
                                if dir_x == 0:
                                    dir_x = speedPN1
                                if dir_y != 0:
                                    dir_y = 0 
                            if round(joystick.get_axis(1)) == 1:#Left
                                    if dir_x == 0:
                                        dir_x = speedP1
                                    if dir_y != 0:
                                        dir_y = 0
                
            for event in pygame.event.get():
                print (event)
                #Exit 
                if event.type ==  QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN): #This if statement tracks any 
                   
                    #Player1
                    if P1_controls == 1:  # If arrows keys were selected, this is the outcome
                        #Arrow Keys                                 
                        if (event.key == 276): #LEFT
                            if dir_x == 0:
                                dir_x = speedPN1
                            if dir_y != 0:
                                dir_y = 0
                        if (event.key == 275): #RIGHT
                            if dir_x == 0:
                                dir_x = speedP1
                            if dir_y != 0:
                                dir_y = 0
                        if (event.key == 273): #UP
                            if dir_y == 0:
                                dir_y  = speedPN1
                            if dir_x != 0:
                                dir_x = 0
                        if (event.key == 274): #DOWN
                            if dir_y == 0:
                                dir_y = speedP1
                            if dir_x != 0:
                                dir_x = 0
                            
                    #Player2
                    if P2_controls == 1:  # If WASD was selected, this is the outcome
                        #WASD
                        if (event.key == K_a): #Left
                            if dir_x2 == 0:
                                dir_x2 = speedPN2
                            if dir_y2 != 0:
                                dir_y2 = 0
                        if (event.key == K_d): #Right
                            if dir_x2 == 0:
                                dir_x2 = speedP2
                            if dir_y2 != 0:
                                dir_y2 = 0
                        if (event.key == K_w): #Up
                            if dir_y2 == 0:
                                dir_y2  = speedPN2
                            if dir_x2 != 0:
                                dir_x2 = 0
                        if (event.key == K_s): #Down
                            if dir_y2 == 0:
                                dir_y2 = speedP2
                            if dir_x2 != 0:
                                dir_x2 = 0
                            
            #Boundaries
            if x + 2 > w or x - 2 < 0 or y + 2 > h or y - 2 < 0: # -2 and +2 are there as I am taking in the Lightbike size too. If this wasn't included, you would be able to go a little beyond the borders
                print ("Player 2 Wins(Green)")
                return game_loop(score2+1,score1,P1_controls,P2_controls) #Here the use of recursion keep track of the score. Adding one will update the score board and also store this data
            if y2 + 2 > h or y2 - 2 < 0 or x2 + 2 > w or x2 - 2 < 0:
                print ("Player 1 Wins(Blue)")
                return game_loop(score2,score1+1,P1_controls,P2_controls)
            #Determining Who Wins 
            for i,j in zip(list1,list2): #Zip must be used in this instance as it is needed to go through both list at the same time. 
                lightbike(blue,i[0],i[1]) #Draws a new square according to every coordinate 
                lightbike(green,j[0],j[1])
                if list1.count(j) > 0 and list2.count(i) > 0: #If both players hit each other at the same time, a tie will occur
                    print ("Tie")
                    game_loop(score2,score1,P1_controls,P2_controls)
                if list1.count(i) > 1: #This will happen if blue hits himself. This basically sees if there is more then 1 of the same coordinate in the list. 
                    print ("Player 2 Wins(Green)") 
                    return game_loop(score2,score1+1,P1_controls,P2_controls)
                if list1.count(j) > 0: #This Happens if green hits blue. It checks if one of the coordinate of list2 occurs in list1.
                    player1_score += 1 # This is needed, it prevents a glitch in the scoring mechanism (The glitch being that it adds 1 to each score) 
                    if player2_score != 0:
                        print ("Player 1 Wins(Blue)")
                        return game_loop(score2,score1+1,P1_controls,P2_controls)
                if list2.count(i) > 0: #Happens if blue hits green.
                    player2_score += 1
                    if player1_score != 0:
                        print ("Player 2 Wins(Green)") 
                        return game_loop(score2+1,score1,P1_controls,P2_controls)
                if list2.count(j) > 1: #Checks if there is more then one occurrence in list2(green).In other words, if green hits himself blue will win 
                    print ("Player 1 Wins(Blue)")
                    return game_loop(score2,score1+1,P1_controls,P2_controls)
                
                
               
               
            
            #This is here deletes some of the list after the length of the list is more then 450. 
            if len(list1) > 450: #Makes the game more interesting 
                del list1[0:1]
            if len(list2) > 450:
                del list2[0:1]
            #Winners 
            if score1 == 4: #If Blue gets 4 wins 
                Blue_Wins()
            if score2 ==4:
                Green_Wins()            
            
            pygame.display.update()
            fpsClock.tick(30)
            
           

    
               
def AI_GAME(score2,score1,P1_controls):
    
    dir_x = -5
    dir_y = 0
    dir_x2 = 5
    dir_y2 = 0
    
    x = 600
    y = 300
    x2 = 200
    y2 = 300
    
    
    cool = True
    list1 = []
    list2 = []
    
    player1_score = 0
    player2_score = 0
    
    speedP1,speedPN1 = 5,-5
    
    while cool == True: 
            screen.fill(black)
            y2 += dir_y2
            x2 += dir_x2
            
            x += dir_x
            y += dir_y
            
            #AI
            if len(list2) != 0:# This if statement prevents the AI from moving at its first coordinate 
                if len(list2)%2 == 0: #Every 2 moves, the AI will change directions 
                    if dir_x2 == 5 or dir_x2 == -5:
                        if dir_x2 == -5:
                            possible_cor = ([-5,0],[0,5],[0,-5])#These are the possible coordinates if the AI was going left (taken out due to the fact the AI should only be going right)
                            choices = random.choice(possible_cor) #This function pick randomly from the list. This AI has random movements
                            dir_x2 = choices[0] 
                            dir_y2 = choices[1]
                        
                        if dir_x2 == 5:
                            possible_cor = ([5,0],[0,-5],[0,5])
                            choices = random.choice(possible_cor)
                            dir_y2 = choices[1]
                            dir_x2 = choices[0]  
                         
                    if dir_y2 == 5 or dir_y2 == -5:
                        if dir_y2 == -5:
                            possible_cor = ([5,0],[0,-5]) #-5 isn't included to avoid the AI from killing himself
                            choices = random.choice(possible_cor)
                            dir_y2 = choices[1]
                            dir_x2 = choices[0]
                            
                    
                        if dir_y2 == 5:
                            possible_cor = ([5,0],[0,5])# Same for here, -5 isn't included to avoid the AI from killing himself
                            choices = random.choice(possible_cor)
                            dir_y2 = choices[1]
                            dir_x2 = choices[0]
                            
                    
                    
                    
            
            #Joystick
            joystick_count = pygame.joystick.get_count() 
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                if P1_controls == 2: #if the player picks Joystick(1)
                    if i == 0:
                        if round(joystick.get_axis(0)) == 1:#UP
                            
                            if dir_y == 0:
                                dir_y  = speedPN1
                            if dir_x != 0:
                                dir_x = 0
                        if round(joystick.get_axis(0)) == -1:#DOWN
                            
                            if dir_y == 0:
                                dir_y = speedP1
                            if dir_x != 0:
                                dir_x = 0
                        if round(joystick.get_axis(1)) == -1: #Right 
                           
                            if dir_x == 0:
                                dir_x = speedPN1
                            if dir_y != 0:
                                dir_y = 0 
                        if round(joystick.get_axis(1)) == 1:#Left
                                
                                if dir_x == 0:
                                    dir_x = speedP1
                                if dir_y != 0:
                                    dir_y = 0
                if P1_controls == 3: #If the player picks Joystick(2)
                    if i == 1:
                        if round(joystick.get_axis(0)) == 1:#UP
                            if dir_y == 0:
                                dir_y  = speedPN1
                            if dir_x != 0:
                                dir_x = 0
                        if round(joystick.get_axis(0)) == -1:#DOWN
                            if dir_y == 0:
                                dir_y = speedP1
                            if dir_x != 0:
                                dir_x = 0
                        if round(joystick.get_axis(1)) == -1: #Right 
                            if dir_x == 0:
                                dir_x = speedPN1
                            if dir_y != 0:
                                dir_y = 0 
                        if round(joystick.get_axis(1)) == 1:
                                if dir_x == 0:
                                    dir_x = speedP1
                                if dir_y != 0:
                                    dir_y = 0
                
            
            #ScoreBoard
            message_display(str(score1),20,1.9,12,text_objects2)
            message_display(str(score2),20,2.1,12,text_objects2)
            message_display((":"),20,2,12,text_objects2)
            #LightBikes 
            lightbike(blue,x,y)
            lightbike(green,x2,y2)
            
            
            #Placing the coordinates to the list 
            list1.append([x,y])
            list2.append([x2,y2])
           
            
            for event in pygame.event.get():
                #Exit 
                if event.type ==  QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):    
                    if P1_controls == 1:          
                        if (event.key == 276): #LEFT
                            if dir_x == 0:
                                dir_x = speedPN1
                            if dir_y != 0:
                                dir_y = 0
                        if (event.key == 275): #RIGHT
                            if dir_x == 0:
                                dir_x = speedP1
                            if dir_y != 0:
                                dir_y = 0
                        if (event.key == 273): #UP
                            if dir_y == 0:
                                dir_y  = speedPN1
                            if dir_x != 0:
                                dir_x = 0
                        if (event.key == 274): #DOWN
                            if dir_y == 0:
                                dir_y = speedP1
                            if dir_x != 0:
                                dir_x = 0
            
            
                            
            #Boundaries
            if x + 2 > w or x - 2 < 0 or y + 2 > h or y - 2 < 0:
                print ("Player 2 Wins(Green)")
                return AI_GAME(score2+1,score1,P1_controls)
            if y2 + 2 > h or y2 - 2 < 0 or x2 + 2 > w or x2 - 2 < 0:
                print ("Player 1 Wins(Blue)")
                return AI_GAME(score2,score1+1,P1_controls)
            
            for i,j in zip(list1,list2):
                lightbike(blue,i[0],i[1])
                lightbike(green,j[0],j[1])
                if list1.count(j) > 0 and list2.count(i) > 0:
                    print ("Tie")
                    return AI_GAME(score2,score1,P1_controls)
                if list1.count(i) > 1:
                    return AI_GAME(score2+1,score1,P1_controls)
                if list2.count(i) > 0:
                    player2_score += 1
                    if player1_score != 0:
                        return AI_GAME(score2+1,score1,P1_controls)
                if list1.count(j) > 0:
                    player1_score += 1
                    if player2_score != 0:
                        return AI_GAME(score2,score1+1,P1_controls)
                if list2.count(j) > 1:
                    return AI_GAME(score2,score1+1,P1_controls)
                    
                    
                
               
               
            
                
            if len(list1) > 450:
                del list1[0:1]
            if len(list2) > 450:
                del list2[0:1]
                
                        
            
            pygame.display.update()
            fpsClock.tick(30)
            
            if score1 ==4:
                Blue_Wins()
            if score2 == 4:
                Green_Wins()
                
    
while True:
    #Main Loop (If you read this you have come to the end)
    intro()