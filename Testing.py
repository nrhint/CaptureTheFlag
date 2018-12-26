##Nathan Hinton
#Dec 23 2018

import pygame

(width, height) = (500, 500)#The width anf height of playing window
bg = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Capture The Flag (Test window)')
screen.fill(bg)
pygame.display.flip()


class Player():
    def __init__(self, surface, pos, color, team):
        self.pygame = pygame
        self.surface = surface
        #print(self.surface)
        self.pos = pos
        self.color = color
        self.team = team
        self.id = self.pygame.draw.rect(self.surface, self.color, (self.pos[0]+0, self.pos[0]-0, self.pos[0]+20, self.pos[0]-20))
    def update(self, positions):
        print(positions[self.team])

def collideCheck(myPos, lst):
    for player in lst:
        x = pygame.rect.Rect.colliderect(myPos.id, player.id)
        #print(x)
        if myPos.id == player.id:
            pass
        if x == 1:
            return True, player
    return False, myPos

p = Player(screen, (10, 50), red, 0)
o = Player(screen, (0, 0), blue, 1)
