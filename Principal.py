import pygame
from Funcoes import *
from constantes import *

# ----- Roda as Funções dos Diferentes Momentos de Jogo
 
pygame.init()


Tutorial = TelaInicial()
game = TelaTutorial(Tutorial)
end = TelaGame(game)


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados