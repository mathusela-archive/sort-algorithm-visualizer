import pygame
from pygame.locals import *
import random as r
import time as t

clock = pygame.time.Clock()

swapped = True
runTime = True
frameCount = 0

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
LINE_WIDTH = 1
CLOCK_SPEED = 60

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
        self.surf.fill((255-round(255*(height/WINDOW_HEIGHT)), round(255*(height/WINDOW_HEIGHT)), 0))
        self.rect = self.surf.get_rect()



stepsCount = 0
def bubbleSortStep(lineArray):
    global stepsCount
    swapped = False
    for lineCount in range(0, len(lineArray)-1-stepsCount):
        if lineArray[lineCount].height > lineArray[lineCount+1].height:
            temp = lineArray[lineCount]
            lineArray[lineCount] = lineArray[lineCount+1]
            lineArray[lineCount+1] = temp
            swapped = True
    stepsCount += 1
    return lineArray, swapped



lineArray = []
for lineCount in range(0, int(WINDOW_WIDTH/LINE_WIDTH)):
    newLine = Line(LINE_WIDTH, r.randint(1, WINDOW_HEIGHT))
    newLine.rect.bottom = WINDOW_HEIGHT
    newLine.rect.left = lineCount*LINE_WIDTH
    lineArray.append(newLine)

start = t.time()
gameloop = True
while gameloop:
    screen.fill((0, 0, 0))

    for line in lineArray:
        screen.blit(line.surf, line.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            gameloop = False
            pygame.quit()

    if swapped:
        lineArray, swapped = bubbleSortStep(lineArray)
    else:
        if runTime == True:
            end = t.time() - start
            print(f"{end} Seconds")
            print(f"{frameCount/end} Frames/second")
        runTime = False

    for lineCount in range(0, len(lineArray)):
        lineArray[lineCount].rect.left = lineCount*LINE_WIDTH

    frameCount += 1
    clock.tick(CLOCK_SPEED)
