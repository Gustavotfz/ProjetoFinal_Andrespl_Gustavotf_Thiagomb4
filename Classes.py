import pygame
import random
from constantes import *
from assets import *

class Icones(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA_TELA - ALTURA_LARGURA_ICONES)
        self.rect.y = ALTURA_TELA - ALTURA_LARGURA_ICONES - 1
        self.maxHigh = random.randint(0, ALTURA_LARGURA_ICONES)
        self.speedy = (2*(self.maxHigh - ALTURA_LARGURA_ICONES) - 1)/(FPS*Tempo_Ar)
        print("Velocidade Vy", self.speedy)
        self.Yorientation = 0
        if self.rect.x <= 400:
            self.speedx = random.randint(int((401-self.rect.x)/(FPS*Tempo_Ar)), int((800-ALTURA_LARGURA_ICONES-self.rect.x)/(FPS*Tempo_Ar)))
        else:
            self.speedx = -(random.randint(0, int((400 - ALTURA_LARGURA_ICONES)/(FPS*Tempo_Ar))))
    
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        if self.rect.y == self.maxHigh:
            self.Yorientation = 1
        if self.Yorientation == 0:
            self.rect.y += -self.speedy
        else:
            self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
            