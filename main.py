import pygame
from player import create_player, move_player
from enemy import create_enemy, move_enemies
from bullets import create_bullet, move_bullets

pygame.init()

WIDTH = 400
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Потом будет название")

player = create_player()
enemies = create_enemy(5, WIDTH)
bullets =[]
cooldown = 15
bullet_cooldown = cooldown

Clock = pygame.time.Clock()

running = True

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if bullet_cooldown > 0:
        bullet_cooldown -= 1

    if keys[pygame.K_SPACE]:
        if bullet_cooldown == 0:
            bullets.append(create_bullet(player.centerx, player.top))
            bullet_cooldown = cooldown

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemy.y = -50
                bullet.y = -100


    move_player(player, keys, WIDTH)
    move_enemies(enemies, HEIGHT, WIDTH, player.width)
    move_bullets(bullets)

    Clock.tick(60)
    screen.fill("black")


    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy)

        if player.colliderect(enemy):
            running = False

    for bullet in bullets:
        pygame.draw.rect(screen, "yellow", bullet)

    pygame.draw.rect(screen, "blue", player)

    pygame.display.update()
