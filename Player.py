##Nathan Hinton
#Dec 24 2018
#Player class for capture the flag

import pygame
print("Pygame imported in Player")

class Player:
    def __init__(self, surface, pos, color, team):
        self.pygame = pygame
        self.surface = surface
        self.currPos = pos
        self.color = color
        self.team = team
        self.id = self.pygame.draw.rect(self.surface, self.color, (50, 100))
    def update(self, positions):
        print(positions[self.team])
        
        
