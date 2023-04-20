import pygame
pygame.init()

surface =pygame.display.set_mode((500,500))
color = (255, 0, 0)
surface.fill(color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

surface =pygame.display.set_mode((500,500))
color = (255, 0, 0)
surface.fill(color)
pygame.display.flip()
