import pygame, copy

# global variable: biến ngoài hàm có thể được sử dụng trong hàm
hero_img = pygame.image.load('./img/player.png')
hero_img = pygame.transform.scale(hero_img, (200,100))
hero_rect = hero_img.get_rect()
hero_rect.x = 0
hero_rect.y = 0

# Đạn của hero
bullet_image = pygame.image.load('./img/bullet.png')
lst_bullet:list[pygame.Rect] = []

def draw_hero(screen):
    # local variable: khai báo trong hàm thì sẽ không sử dụng được ngoài hàm
    screen.blit(hero_img, hero_rect)
    
def attack():
    bullet_rect = copy.deepcopy(bullet_image.get_rect())
    bullet_rect.x = hero_rect.x + hero_rect.width
    bullet_rect.y = hero_rect.y + hero_rect.height / 2
    # bỏ đạn vào list đạn
    lst_bullet.append(bullet_rect)