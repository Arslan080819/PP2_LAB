import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((400,200))

playlist = ["music/track1.wav", "music/track2.wav"]
player = MusicPlayer(playlist)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.previous()
            elif event.key == pygame.K_q:
                running = False

pygame.quit()
