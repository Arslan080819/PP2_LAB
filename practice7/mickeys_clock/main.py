import pygame
from clock import MickeyClock

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
mickey = MickeyClock((250, 250))

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.draw(screen)
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
