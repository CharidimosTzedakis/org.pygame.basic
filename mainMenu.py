############***GAME MENU SCREEN that gives the player the basic options*###############
############**********************JEDAKIS CHARIDIMOS********************###############
############**********************GNU PUBLIC LICENSE********************###############

#--FILENAMES---#
menuIteratorImageFileName='cat.png'  #Iterator---> little icon used to iterate through the menu options 
backgroundFileName='orangeBackground.png'
menuFontFileName = 'BlackBoysOnMopeds.ttf'

import pygame
from pygame.locals import *
from sys import exit

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("The Greatest Game!")

#------>Loading Images<-------
menuIteratorImage = pygame.image.load(menuIteratorImageFileName).convert_alpha()
backgroundImage = pygame.image.load(backgroundFileName).convert()

#------>Loading Sounds<-------
menuMusic = pygame.mixer.Sound("menuTune1.ogg")
channel = menuMusic.play(2)

#------>Main menu initialization<------
spaceBetweenText=50
optionsList = ["New Game","Load Game","Options","Exit Game"]
#positions of the iterator for each option in optionList
iteratorPositions = [(50,81), (50,81+spaceBetweenText), (50,81+2*spaceBetweenText), (50,81+3*spaceBetweenText)]
previousIteratorPosition = iteratorPositions[0]
currentIteratorPosition = iteratorPositions[0]

font = pygame.font.Font(menuFontFileName, 40)

#font = pygame.font.Font(None, 40)
screen.blit(backgroundImage,(0,0))
            
for i in range(0,len(optionsList) ):
    text = font.render(optionsList[i], 1, (255, 255, 255) )
    screen.blit(text, (100,100+i*spaceBetweenText) )

screen.blit(menuIteratorImage, iteratorPositions[0] )
pygame.display.update() 
    

#------>Clock<-------
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()  

#--->here you can set a fixed Frame rate<---                                         
    timePassed = clock.tick()
    
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            if ( previousIteratorPosition!= iteratorPositions[-1] ):
                screen.blit(backgroundImage,(0,0))
                for i in range(0,len(optionsList) ):
                    text = font.render(optionsList[i], 1, (255, 255, 255) )
                    screen.blit(text, (100,100+i*spaceBetweenText) )
                currentIteratorPosition = (50 , previousIteratorPosition[1]+spaceBetweenText )
                screen.blit(menuIteratorImage, currentIteratorPosition)
                previousIteratorPosition = currentIteratorPosition
                
                pygame.display.update()         
                pygame.time.delay(200)

        elif event.key == K_UP:
            if ( previousIteratorPosition!= iteratorPositions[0] ):
                screen.blit(backgroundImage,(0,0))
                for i in range(0,len(optionsList) ):
                    text = font.render(optionsList[i], 1, (255, 255, 255) )
                    screen.blit(text, (100,100+i*spaceBetweenText) )
                currentIteratorPosition = (50 , previousIteratorPosition[1]-spaceBetweenText )
                screen.blit(menuIteratorImage,currentIteratorPosition )
                previousIteratorPosition = currentIteratorPosition
                pygame.display.update()
                pygame.time.delay(200)