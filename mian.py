import pygame 
import sys

pygame.init()
pygame.display.set_icon(pygame.image.load('graphics/icon.png'))
pygame.display.set_caption('')

speed = [5, 4]
size = width, height = 900, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load('graphics/orange_926.png').convert_alpha()
rect = logo.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if rect.left < 0:
        speed[0] = -speed[0]
        logo = pygame.image.load('graphics/green_926.png').convert_alpha()

    if rect.right > width:
        speed[0] = -speed[0]
        logo = pygame.image.load('graphics/pink_926.png').convert_alpha()

    if rect.top < 0:
        speed[1] = -speed[1]
        logo = pygame.image.load('graphics/blue_926.png').convert_alpha()

    if rect.bottom > height:
        speed[1] = -speed[1]
        logo = pygame.image.load('graphics/orange_926.png').convert_alpha()
    
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, rect)
    pygame.display.update()
    clock.tick(60)
