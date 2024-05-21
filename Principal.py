import pygame
from Funcoes import *

# ----- Roda as Funções dos Diferentes Momentos de Jogo

Tutorial = TelaInicial()
game = TelaTutorial(Tutorial)
end = TelaGame(game)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados