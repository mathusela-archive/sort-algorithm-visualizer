import pygame
from pygame.locals import *
import random as r

clock = pygame.time.Clock()

swapped = True

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
LINE_WIDTH = 5
CLOCK_SPEED = 10

if WINDOW_WIDTH % LINE_WIDTH != 0:
    raise Exception("WINDOW WIDTH NOT DIVISIBLE BY LINE WIDTH")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



class Line(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Line, self).__init__()
        self.height = height
        self.surf = pygame.Surface((width, height))
        #self.surf.fill((255, 255, 255))
        global WINDOW_HEIGHT
        self.colour = (255 - round(255 * (height / WINDOW_HEIGHT)), round(255 * (height / WINDOW_HEIGHT)), 0)
        self.surf.fill((255-round(255*(height/WINDOW_HEIGHT)), round(255*(height/WINDOW_HEIGHT)), 0))
        self.rect = self.surf.get_rect()



def bubbleSortStep(lineArray, lineCount, swapped):
    lineColour = lineArray[lineCount].colour
    #lineArray[lineCount].surf.fill((255, 255, 255))
    if lineArray[lineCount].height > lineArray[lineCount+1].height:
        temp = lineArray[lineCount]
        lineArray[lineCount] = lineArray[lineCount+1]
        lineArray[lineCount+1] = temp
        swapped = True
    return lineArray, swapped, lineColour, lineArray[lineCount]



lineArray = []
for lineCount in range(0, int(WINDOW_WIDTH/LINE_WIDTH)):
    newLine = Line(LINE_WIDTH, r.randint(1, WINDOW_HEIGHT))
    newLine.rect.bottom = WINDOW_HEIGHT
    newLine.rect.left = lineCount*LINE_WIDTH
    lineArray.append(newLine)

stepsCount = 0
gameloop = True
while gameloop:

    if swapped:
        swapped = False
        for lineCount in range(0, len(lineArray) - 1 - stepsCount):
            lineArray, swapped, lineColour, changedLine = bubbleSortStep(lineArray, lineCount, swapped)
            for lineCount2 in range(0, len(lineArray)):
                lineArray[lineCount2].rect.left = lineCount2 * LINE_WIDTH
            screen.fill((0, 0, 0))
            for line in lineArray:
                screen.blit(line.surf, line.rect)
            pygame.display.flip()
            #print(changedLine, lineColour)
            #changedLine.surf.fill((0,0,0))
        stepsCount += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            gameloop = False
            pygame.quit()

    clock.tick(CLOCK_SPEED)
