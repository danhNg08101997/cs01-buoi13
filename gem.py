import pygame, random

gem_image = pygame.image.load('./img/gem.png')
gem_image = pygame.transform.scale(gem_image,(50,50))
gem_rect = gem_image.get_rect()

def draw_gem(screen):        
    screen.blit(gem_image, gem_rect)