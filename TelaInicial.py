import pygame
from constantes import ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL

window_TelaInicial = pygame.display.set_mode((LARGURA_TELA_INICIAL, ALTURA_TELA_INICIAL))
while True:
    pygame.display.set_caption('Tela inicial')