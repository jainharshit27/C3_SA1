import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

dino_y_change = 0

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino_y_change = -1
        # TA1: Create a condition to recognize KEYUP
            # TA1: Create a condition to recognize SPACE key
                # TA1: Change dino_y_change to 1
    
    dino_rect.y += dino_y_change
    if dino_rect.y < 100:
        dino_rect.y = 100
    # TA2: Check if dino_rect.y is more than 250
        # TA2: Set dino_rect.y back to 250
   
    cactus_rect.x = cactus_rect.x - 1
    if cactus_rect.x <= -30:
        cactus_rect.x = 1200
        
    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    pygame.display.update()
    
    
    
    
    
