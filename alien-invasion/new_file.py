import pygame , sys 

pygame.init()

# set up the window
window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("First Shapes")


# Setting up colors 

# Colors made up 
# using three tuble format 
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
mix1 = (189,58,54)

# #Colors made up using 
# # the the pygame.Color object 
# #by calling the pygame.Color() constructor function
# pygame.Color(23,250,30)
# pygame.Color(20,27,270)




# draw on the surface object
window_surface.fill(white)

# draw on the surface object 

pygame.draw.polygon(window_surface, green, ((146, 0), (291, 106), (236, 277),
(56, 277), (0, 106)), 4)
pygame.draw.line(window_surface , blue, (60, 60), (120, 60), 4)
pygame.draw.line(window_surface, blue, (120, 60), (60, 120))
pygame.draw.line(window_surface, blue, (60, 120), (120, 120), 4)
pygame.draw.circle(window_surface, blue, (300, 50), 20, 0)
pygame.draw.ellipse(window_surface, red, (300, 250, 40, 80), 1)
pygame.draw.rect(window_surface, red, (200, 150, 100, 50))

#drawing a black cross on a display surface
pygame.draw.line(window_surface,black,(0,200),(500,200),20)
pygame.draw.line(window_surface,black,(250,0),(250,400),20)

# drawing an arc and polygon display surface
pygame.draw.polygon(window_surface,blue,[(50,200),(100,50),(450,60),(450,70),(50,300)])

# drawing multiple lines 
pygame.draw.lines(window_surface,red,False,[(39,99),(100,250),(300,400)],5)


pixObj = pygame.PixelArray(window_surface)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()