# jamp-and-run-game-v1.0.0

import pygame
import time
import random 

pygame.init()
screen = pygame.display.set_mode([1920,1800])
pygame.display.set_caption("Jump and run") 
clock = pygame.time.Clock()

screen.fill(with)
pygame.draw.rect(screen,(0,255,0),(0, 950, 1800, 50), 0) #blue player
pygame.display.update()
clock.tick(60)  
