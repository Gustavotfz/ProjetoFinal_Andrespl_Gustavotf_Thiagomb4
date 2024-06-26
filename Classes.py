import pygame
import random
from constantes import *
from assets import *

class Icones(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA_TELA - ALTURA_LARGURA_ICONES)
        self.rect.y = ALTURA_TELA - ALTURA_LARGURA_ICONES - 1
        self.maxHigh = random.randint(int((0.75)*ALTURA_LARGURA_ICONES), int((1.25)*ALTURA_LARGURA_ICONES))
        self.speedy = (2*(ALTURA_TELA - self.maxHigh) - 1)/(FPS*Tempo_Ar)
        self.Yorientation = 0
        if self.rect.x <= (LARGURA_TELA/2):
            self.speedx = random.randint(int((((LARGURA_TELA/2)+1)-self.rect.x)/(FPS*Tempo_Ar)), int((LARGURA_TELA-ALTURA_LARGURA_ICONES-self.rect.x)/(FPS*Tempo_Ar)))
        else:
            self.speedx = -(random.randint(0, int(((LARGURA_TELA/2) - ALTURA_LARGURA_ICONES)/(FPS*Tempo_Ar))))
    
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        if self.rect.y <= self.maxHigh:
            self.Yorientation = 1
        if self.Yorientation == 0:
            self.rect.y -= self.speedy
        else:
            self.rect.y += self.speedy



class MouseSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1, 1))  # Criar uma imagem vazia de 1x1 pixel
        self.rect = self.image.get_rect()

    def update(self):
        # Atualize a posição da sprite para a posição atual do mouse
        self.rect.center = pygame.mouse.get_pos()