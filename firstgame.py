import pygame

pygame.init()

WIDTH = 400
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Потом будет название")

player = pygame.Rect(180, 400, 50, 50)

Clock = pygame.time.Clock()

while True:
  
  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      pygame.quit()
      exit()
      
      
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
    player.x -= 4
  if keys[pygame.K_RIGHT]:
    player.x += 4
    
  Clock.tick(60)
    
    
    
    
    
    
    
  screen.fill("black")
  
  pygame.draw.rect(screen, "blue", player)
  
  
  pygame.display.update()
  