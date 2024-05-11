import pygame
from constantes import *
from assets import *
from Classes import *
from Funcoes import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela inicial
window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')

# ----- Roda as Funções dos Diferentes Momentos de Jogo
PreTutorial = TelaInicial()
Tutorial = TelaPreTutorial(PreTutorial)
game = TelaTutorial(Tutorial)
end = TelaGame(game)
TelaFinal_morteraposa(end)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados