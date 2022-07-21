import pygame, sys, time, random
pygame.init()

win = pygame.display.set_mode((500,500))

green = (0,255,0)
white = (255,255,255)
red = (255,0,0)
purple = (121, 25, 122)

run = True
food_status = True
food2_status = True
speed = 1
food = pygame.Rect(400,250,10,10)
food2 = pygame.Rect(50,400,10,10)

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

  
  if player.colliderect(food):
    cubeSize+=5
    food_status = False
    red = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
  if food_status == False:
    food = pygame.Rect(random.randint(0,500),random.randint(0,500),10,10)
    food_status = True

  if player.colliderect(food2):
    cubeSize-=5
    food2_status = False
  

  if food2_status == False:
    food2 = pygame.Rect(random.randint(0,500),random.randint(0,500),10,10)
    food2_status = True



    
  pygame.draw.rect(win, purple, food)
  pygame.draw.rect(win, green, food2)
  pygame.draw.rect(win, red, player)
  pygame.display.update()