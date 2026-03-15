import pygame

pygame.init()
window = pygame.display.set_mode(size = (600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() # end pygame