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

# Запуск игрового цикла
running = True

# Обработка событий
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # поставил выбор на мышку или пробел чтоб стрелять
            if event.button == 1:
                bullets.append(pygame.Rect(player.centerx-2, player.y-10, 5, 10))
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx-2, player.y-10, 5, 10))

# Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_d] and player.right < 800:
        player.x += 5

# Движение пуль игрока
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)

# Движение и стрельба врагов
    for enemy in enemies[:]:
        enemy.x += enemy_dir * enemy_speed
        if random.random() < 0.005:
            enemy_bullets.append(pygame.Rect(enemy.centerx-2, enemy.y+40, 5, 10))

# Смена направления врагов
    if enemies and (min(e.x for e in enemies) <= 0 or max(e.right for e in enemies) >= 800):
        enemy_dir *= -1
        for enemy in enemies:
            enemy.y += 30
            
# Движение и столкновение вражеских пуль
    for bullet in enemy_bullets[:]:
        bullet.y +=5
        if bullet.top > 600:
            enemy_bullets.remove(bullet)
        if bullet.colliderect(player):
            reset_game()

# Столкновение пуль игрока с врагами
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

# Проверка касания врагов с игроком
    if any(enemy.bottom >= player.top for enemy in enemies):
        reset_game()
    
# Создание новой волны врагов
    if not enemies:
        enemies = [pygame.Rect(x*70+50, y*60+50, 50, 40) for y in range(4) for x in range(8)]
        enemy_speed = 2

# Отрисовка всех объектов
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 255), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    for bullet in enemy_bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    
# Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Выход из игры
pygame.quit()