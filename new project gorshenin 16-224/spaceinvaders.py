# Импорт Библиотек
import pygame 
import random

# Запуск окна игры
pygame.init()

# Настройки окна и прочего
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
player = pygame.Rect(370, 550, 60, 30)
bullets = []
enemies = [pygame.Rect(x*70+50, y*60+50, 50, 40) for y in range(4) for x in range(8)]
enemy_bullets = []
enemy_dir = 1
enemy_speed = 2
score = 0
font = pygame.font.Font(None,36)

# Перезапуск игры
def reset_game():
    global player, enemies, bullets, enemy_bullets
    global score, enemy_speed
    player.x = 370
    enemies = [pygame.Rect(x*70+50, y*60+50, 50, 40) for y in range(4) for x in range (8)]
    bullets = []
    enemy_bullets = []
    score = 0
    enemy_speed = 2

running = True

#Обработка событий
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.centerx-2, player.y-10, 5, 10))

# Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < 800:
        player.x += 5

# Движение пуль
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)

# Движение и пули врагов
    for enemy in enemies[:]:
        enemy.x += enemy_dir * enemy_speed
        if random.random() < 0.005:
            enemy_bullets.append(pygame.Rect(enemy.centerx-2, enemy.y+40, 5, 10))

# Выход из приложения
pygame.quit()