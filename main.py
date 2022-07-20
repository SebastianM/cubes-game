import pygame, sys, time, random
pygame.init()

win = pygame.display.set_mode((500,500))

yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
purple = (121, 25, 122)

run = True

speed = 1

cubeX = 250
cubeY = 250
cubeSize = 25

while run:
  pygame.time.delay(5)
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  keys = pygame.key.get_pressed()
  win.fill(white)
  if(keys[pygame.K_RIGHT]):
    cubeX+=speed

  if(keys[pygame.K_LEFT]):
    cubeX-=speed
    
  if(keys[pygame.K_UP]):
    cubeY-=speed
    
  if(keys[pygame.K_DOWN]):
    cubeY+=speed
    
  player = pygame.Rect(cubeX, cubeY, cubeSize, cubeSize)

  food = pygame.Rect(400,250,10,10)


  if player.colliderect(food):
    print("eating!")
  
  pygame.draw.rect(win, purple, food)
  
  pygame.draw.rect(win, red, player)
  pygame.display.update()
  
  
