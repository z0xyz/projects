# import sys
import pygame
import sys


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))

while True :
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYUP :
            pygame.quit()
            sys.exit()

    pygame.display.update()


