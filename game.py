import pygame
import sys
import random
import hero
import gem

pygame.init()
#Khởi tạo cửa sổ game và tên game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Hero techx")

#Tạo font chữ 
f_game = pygame.font.Font('fonts/font_game.otf',32)
# background
bg_game = pygame.image.load('./img/bg_game.jpg')
bg_game = pygame.transform.scale(bg_game, (SCREEN_WIDTH, SCREEN_HEIGHT))

time_gem_start = 0
#Vòng lặp game
running = True
while running:
    #Cài đặt game
    #events: hành động bấm từng phím hoặc click từng nháy
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        # Tất cả các event nên code trong file chính của game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.attack()
                print(hero.lst_bullet)
    # Setup sự kiện đè phím
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        hero.hero_rect.y += 1
    elif key[pygame.K_UP]:
        hero.hero_rect.y -= 1
    elif key[pygame.K_LEFT]:
        hero.hero_rect.x -= 1
    elif key[pygame.K_RIGHT]:
        hero.hero_rect.x += 1
    
    # background
    screen.blit(bg_game, (0,0))
    # draw hero
    hero.draw_hero(screen)
    # Xử lý va chạm
    for bullect_rect in hero.lst_bullet:
        if bullect_rect.colliderect(gem.gem_rect):
            gem.gem_rect.x = random.randint(0, screen.get_width()- gem.gem_rect.width)
            gem.gem_rect.y = random.randint(0, screen.get_height() - gem.gem_rect.height)
            print('va cham')
        # Xử lý tăng điểm
        
        
        
        
        
    # draw gem
    time_current_gem = pygame.time.get_ticks()
    if time_current_gem - time_gem_start >= 10000:
        gem.gem_rect.x = random.randint(0, screen.get_width() - gem.gem_rect.width)
        gem.gem_rect.y = random.randint(0, screen.get_height() - gem.gem_rect.height)
        time_gem_start = time_current_gem
    gem.draw_gem(screen)
    #Cập nhật game
    pygame.display.flip()
    
pygame.quit()
sys.exit()