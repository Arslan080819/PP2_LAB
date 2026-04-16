import pygame
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

ball = Ball(250,250,25,500,500)

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-20,0)
            elif event.key == pygame.K_RIGHT:
                ball.move(20,0)
            elif event.key == pygame.K_UP:
                ball.move(0,-20)
            elif event.key == pygame.K_DOWN:
                ball.move(0,20)

    pygame.draw.circle(screen,(255,0,0),(ball.x,ball.y),ball.radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
