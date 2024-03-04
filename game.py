import pygame
import sys
import random

pygame.init()
#Khởi tạo cửa sổ game và tên game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Hero techx")

#Tạo font chữ 
f_game = pygame.font.Font('fonts/font_game.otf',32)

#Vòng lặp game
running = True
while running:
    #Cài đặt game
    #events: hành động bấm từng phím hoặc click từng nháy
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    #Cập nhật game
    pygame.display.flip()
    
pygame.quit()
sys.exit()