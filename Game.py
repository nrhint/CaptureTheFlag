##Nathan Hinton
#Dec 23 2018
#This is for learning ho to make AI.  I will program acapture the flag game.

#This is the Game class.  This will be the master class.

#Import pygame:
import pygame
from time import sleep
from math import cos, sin
print("Pygame imported in Game")
print("Sleep imported in Game")
red = (255, 0, 0)
blue = (0, 0, 255)

#Changer vars here:
playerMaxSpeed = 4
(width, height) = (500, 500)#The width anf height of playing window
bg = (75, 150, 225)
midline = height/2

#Not here...
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Capture The Flag')
screen.fill(bg)
pygame.draw.rect(screen, (255, 155, 55), (0, 249, (width), 2))#Center line
pygame.display.flip()


class Game:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        #self.screen = screen
        self.players = []
        #Create players:
        for x in range(0, 2):#number of players on each team
            self.players.append(Player((100*x, 0), red, 0))
            self.players.append(Player((100*x, 480), blue, 1))
        self.updateScreen()
    def updateScreen(self):
        running = True
##    while running:
##    #for x in range(0, 1):
        #Put code here:
##        self.playerPoses = []
##        for player in self.players:
##            self.playerPoses.append(player.id)
        for player in self.players:
            player.move()
            self.val = collideCheck(player, self.players)
            if self.val[0] == True:
                #print("COLLISION")
                for x in range(0, len(self.players)):
                    #print(self.val)
                    print(x)
                    if self.players[x] == self.val[1]:
                        offender = x
                        #print(x)
                        self.die = checkDeath(player, self.players[x])
                        #print(self.die)
                        if self.die[0] == True:
                            #print(self.die)
                            self.die[1].die()
                            self.players.remove(self.die[1])
                        else:
                            pass
            
        pygame.draw.rect(screen, (255, 155, 55), (0, midline-1, (width), 2))#Center line
        pygame.display.flip()
        ##############Event code for closing the window##############
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pygame.quit()
                running = False
        #running = False
        #sleep(0.01)
        #print('Updated')
        #print()
        #print()

class Player():
    def __init__(self, pos, color, team):
        self.speed = 0
        self.pygame = pygame
        self.color = color
        self.team = team
        self.id = self.pygame.draw.rect(screen, self.color, (pos[0], pos[1], 20, 20))
        self.heading = 0
    def move(self):
        if self.speed > playerMaxSpeed:
            self.speed = playerMaxSpeed
        self.nextPos = self.id.move(cos(self.heading)*self.speed, sin(self.heading)*self.speed)
        pygame.draw.rect(screen, bg, self.id)
        self.id = self.pygame.draw.rect(screen, self.color, (self.nextPos[0], self.nextPos[1], 20, 20))
    def update(self, heading, speed):##This is what the AI gets to change.
        self.heading = heading
        self.speed = speed
    def info(self):
        return self.heading, self.speed, (self.id.x, self.id.y)
    def die(self):
        self.pygame.draw.rect(screen, bg, self.id)

class flag:
    def __init__(self, color, pos):
        pass
    

def collideCheck(myPos, lst):
    for player in lst:
        x = pygame.rect.Rect.colliderect(myPos.id, player.id)
        #print(x)
        if myPos.id == player.id:
            pass
        elif x == 1:
            return True, player
            #print("!!!COLLISION!!!")
            #print()
    return False, myPos

def checkDeath(player1, player2):
    if player1.team == player2.team:
        #print("Same team")
        return False, False
    else:
        #print("Not same team")
        #Create boundries:
        #print(player1.team == 0)
        if player1.team == 0:
            #print(player1.id.y>midline)
            #print(player1.id.y)
            if player1.id.y>midline:#Player 1 below midline
                #print("Player1 dies")
                return True, player1
            #print(player2.team == 0)
        if player2.team == 0:
            if player2.id.x<midline:#Player 2 above midline
                #print("Player2 dies")
                return True, player2
    #print("Death checked.")

print("Creating class object g for Game class...")
##g = Game(pygame, screen)
##p = g.players[0]
##p.heading = 45
##p.speed = 2
###z = Player((250, 250), blue, 0)
