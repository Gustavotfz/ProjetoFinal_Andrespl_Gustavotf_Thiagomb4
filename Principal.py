import pygame
from constantes import *

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL))
pygame.display.set_caption('Tela Inicial - NOME DO JOGO')

# ----- Criando o Fundo Tela Inicial
img_TelaInicial = pygame.image.load("Fotos/Foto_TelaInicial.jpg")
img_TelaInicial = pygame.transform.scale(img_TelaInicial, (ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL))

# ----- Inicia Assets
font_txt_TelaInicial = pygame.font.SysFont(None, 48)
txt_TelaInicial = font_txt_TelaInicial.render("TÍTULO", True, (255,0,0))

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.blit(img_TelaInicial, (0,0))
    window.blit(txt_TelaInicial, (50,50))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados