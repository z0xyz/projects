import pygame
import sys
# from pygame import *

pygame.init()
# First surface object >> Display surface 
display_surface = pygame.display.set_mode((400,300))
pygame.display.set_caption("Frist game")


# The main game loop
while True:

    # The main Event handling 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



        # The main game-state update
        pygame.display.update()



my_color = pygame.Color(255,0,0)
print(my_color)

some_rect = pygame.Rect(10 , 20 , 300 , 300)
print(some_rect)
print(some_rect.left)

