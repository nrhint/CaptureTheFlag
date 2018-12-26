##Nathan Hinton
##AI for ctf

from Game import *
import pygame
from time import sleep
from math import cos, sin
red = (255, 0, 0)
blue = (0, 0, 255)
team = 0

#Changer vars here:
playerSpeed = 2
(width, height) = (500, 500)#The width anf height of playing window
bg = (225, 150, 75)

#Not here...
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Capture The Flag')
screen.fill(bg)
pygame.draw.rect(screen, (255, 155, 55), (0, 249, (width), 2))#Center line
pygame.display.flip()
#######################################################
g = Game(pygame, screen)
players = g.players

#z = Player((250, 250), blue, 0)
team0 = []
for p in g.players:
    if p.team == 0:
        team0.append(p)
team1 = []
for p in g.players:
    if p.team == 1:
        team1.append(p)

################ BEGIN STATE MACHINE DANIEL #################
print("Seting up machines")
class stateError(Exception):
    def __init__(self, i, place):
        print("State machine error!  Machine name %s!" %i)
        print("Place: %s" %place)

##State machine info.  
##Requirements: __init__, update
##update is the function that is called once every loop.

class Daniel:
    def __init__(self, team, enm):
        self.team = team
        self.enm = enm
        self.state = 'attack'
    def update(self):
        for player in self.team:
            #Change states here:
            ##Eval states:
            if self.state == 'attack':
                player.update(90, 20)
            elif self.state == 'defend':
                pass
            else:
                raise stateError('Daniel', 'State error')

#Main loop:
daniel = Daniel(team0, team1)
while True:
    daniel.update()
    g.updateScreen()
    sleep(0.015)
    #print('tick')
