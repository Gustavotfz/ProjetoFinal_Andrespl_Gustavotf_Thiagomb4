import pygame
from constantes import *
from assets import *
from Classes import *
from Funcoes import *

pygame.init()
pygame.mixer.init()

# ----- Roda as Funções dos Diferentes Momentos de Jogo
PreTutorial = TelaInicial()
Tutorial = TelaPreTutorial(PreTutorial)
game = TelaTutorial(Tutorial)
end = TelaGame(game)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados