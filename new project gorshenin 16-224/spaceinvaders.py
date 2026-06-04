# Импорт Библиотек
import pygame
import random
import time

# Запуск окна игры
pygame.init()

# Настройки окна и прочего
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Космическое Вторжение")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 74)

# Фон
background = pygame.image.load("space.jpg")  
background = pygame.transform.scale(background, (800, 600))  

# Параметры игрока
player = pygame.Rect(370, 550, 60, 30)
bullets = []
enemies = []
enemy_bullets = []
enemy_dir = 1
enemy_speed = 2
score = 0

# Укрытия
shelters = [
    pygame.Rect(100, 450, 80, 50),   
    pygame.Rect(360, 450, 80, 50),   
    pygame.Rect(620, 450, 80, 50)    
]
shelters_health = [10, 7, 10]   

# Состояние игры
game_state = 'menu'

# Кнопки меню
menu_buttons = {
    "start": pygame.Rect(300, 250, 200, 50),
    "quit": pygame.Rect(300, 350, 200, 50)
}

# Точка начала отсчета(esc)
game_start_time = 0

# Функция, добавляющая меню
def draw_menu():
    # Рисуем фон
    screen.blit(background, (0, 0))
    
    # Заголовок
    title = title_font.render("Космическое Вторжение", True, (255, 255, 255))
    title_rect = title.get_rect(center=(400, 150))
    screen.blit(title, title_rect)
    
    # Кнопки
    pygame.draw.rect(screen, (0, 255, 0), menu_buttons["start"])
    pygame.draw.rect(screen, (255, 0, 0), menu_buttons["quit"])
    
    # Текст на кнопках
    start_text = font.render("Начать", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=menu_buttons["start"].center)
    screen.blit(start_text, start_rect)
    
    quit_text = font.render("Выход", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=menu_buttons["quit"].center)
    screen.blit(quit_text, quit_rect)

# Функция ресета игры
def reset_game():
    global player, enemies, bullets, enemy_bullets, score, enemy_speed, enemy_dir, game_start_time, shelters, shelters_health
    player.x = 370
    enemies = [pygame.Rect(x*70+50, y*60+50, 50, 40) for y in range(4) for x in range(8)]
    bullets = []
    enemy_bullets = []
    score = 0
    enemy_speed = 2
    enemy_dir = 1
    game_start_time = time.time()
    shelters = [
        pygame.Rect(100, 450, 80, 50),
        pygame.Rect(360, 450, 80, 50),
        pygame.Rect(620, 450, 80, 50)
    ]
    shelters_health = [10, 7, 10]

# Запуск игрового цикла
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == 'menu':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if menu_buttons["start"].collidepoint(mouse_pos):
                    game_state = 'playing'
                    reset_game()
                elif menu_buttons["quit"].collidepoint(mouse_pos):
                    running = False
        
        elif game_state == 'playing':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(pygame.Rect(player.centerx-2, player.y-10, 5, 10))
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.centerx-2, player.y-10, 5, 10))
                if event.key == pygame.K_ESCAPE:
                    game_state = 'menu'

    if game_state == 'menu':
        draw_menu()
    
    elif game_state == 'playing':
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
                
        # Движение вражеских пуль и проверка столкновения с укрытиями
        for bullet in enemy_bullets[:]:
            bullet.y += 5
            if bullet.top > 600:
                enemy_bullets.remove(bullet)
                continue
            
            # Проверка попадания в укрытия
            hit_shelter = False
            for i, shelter in enumerate(shelters[:]):
                if shelter.colliderect(bullet):
                    shelters_health[i] -= 1
                    if shelters_health[i] <= 0:
                        shelters.pop(i)
                        shelters_health.pop(i)
                    enemy_bullets.remove(bullet)
                    hit_shelter = True
                    break
            
            if hit_shelter:
                continue
                
            # Проверка попадания в игрока
            if bullet.colliderect(player):
                reset_game()
                continue

        # Столкновение пуль игрока с врагами
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    score += 10
                    break

        # Пули игрока могут попадать в укрытия 
        for bullet in bullets[:]:
            for i, shelter in enumerate(shelters[:]):
                if shelter.colliderect(bullet):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break

        # Проверка касания врагов с игроком
        if any(enemy.bottom >= player.top for enemy in enemies):
            reset_game()
        
        # Создание новой волны врагов
        if not enemies:
            enemies = [pygame.Rect(x*70+50, y*60+50, 50, 40) for y in range(4) for x in range(8)]
            enemy_speed = 2

        # Отрисовка всех объектов
        screen.blit(background, (0, 0))  # Рисуем фон
        
        
        for i in range(len(shelters)):  
            if i < len(shelters) and i < len(shelters_health):  
                shelter = shelters[i]
                health = shelters_health[i]
                health_percent = health / 10  
                health_percent = max(0, min(1, health_percent))
                red = int(255 * (1 - health_percent))
                green = int(255 * health_percent)
                color = (red, green, 0)
                pygame.draw.rect(screen, color, shelter)
                pygame.draw.rect(screen, (255, 255, 255), shelter, 2)  
                health_text = font.render(str(health), True, (255, 255, 255))
                screen.blit(health_text, (shelter.x + 30, shelter.y - 20))
        
        pygame.draw.rect(screen, (0, 255, 255), player)
        
        for bullet in bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)
        
        for enemy in enemies:
            pygame.draw.rect(screen, (255, 0, 0), enemy)
        
        for bullet in enemy_bullets:
            pygame.draw.rect(screen, (255, 255, 255), bullet)
        
        screen.blit(font.render(f"Счёт: {score}", True, (255, 255, 255)), (10, 10))
        
        # Показываем esc только первые 5 секунд
        if time.time() - game_start_time < 5:
            screen.blit(font.render("Нажмите ESC для выхода", True, (255, 255, 255)), (10, 40))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Конец программы
pygame.quit()