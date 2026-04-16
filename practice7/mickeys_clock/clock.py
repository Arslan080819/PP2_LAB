import pygame
import datetime

class MickeyClock:
    def __init__(self, center):
        self.center = center
        self.hand = pygame.Surface((10, 150), pygame.SRCALPHA)
        pygame.draw.rect(self.hand, (0,0,0), (0,0,10,150))

    def draw(self, screen):
        now = datetime.datetime.now()
        sec = now.second
        minute = now.minute

        sec_angle = sec * 6 - 90
        min_angle = minute * 6 - 90

        sec_hand = pygame.transform.rotate(self.hand, -sec_angle)
        min_hand = pygame.transform.rotate(self.hand, -min_angle)

        screen.blit(min_hand, min_hand.get_rect(center=self.center))
        screen.blit(sec_hand, sec_hand.get_rect(center=self.center))
