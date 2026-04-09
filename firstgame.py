import pygame
import random 


pygame.init()

WIDTH = 400
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))


enemies = []


for i in range(5):
  x = random.randint(8, WIDTH-40)
  y = random.randint(-800, -40)
  enemies.append(pygame.Rect(x, y, 40, 40))

pygame.display.set_caption("Потом будет название")

player = pygame.Rect(180, 400, 50, 50)

Clock = pygame.time.Clock()

running = True

while running:
  
  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      pygame.quit()
      exit()
      
      
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    player.x -= 4
  if keys[pygame.K_RIGHT]:
    player.x += 4
 
  if player.right > WIDTH:
    player.right = WIDTH
  if player.left < 0:
     player.left = 0


      
  Clock.tick(60)
  screen.fill("black")
    

  for enemy in enemies:
    enemy.y += 4

     
    if enemy.y > HEIGHT:
        enemy.y = -50
        enemy.x = random.randint(0, WIDTH-player.width)
    pygame.draw.rect(screen, "red", enemy)

    if player.colliderect(enemy):
      running = False
  
  pygame.draw.rect(screen, "blue", player)
  
  pygame.display.update()
  
  
