import pygame
from constantes import *
from assets import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela inicial
window = pygame.display.set_mode((LARGURA_TELA_INICIAL, ALTURA_TELA_INICIAL))
pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')

# ----- Inicia estruturas de dados
game = True
tela_inicial = True
# ===== Loop principal =====
while tela_inicial:
    musica_tela_inicial.play(-1)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            tela_inicial = False
            game = False
            musica_tela_inicial.stop()
            continue
        elif event.type == pygame.KEYDOWN:
            tela_inicial = False
            musica_tela_inicial.stop()
            continue

    # ----- Gera saídas
    window.blit(img_TelaInicial, (0,0))
    window.blit(txt_TelaInicial, (84,20))
    window.blit(txt_Pressioneqlqrbotao, (40,100))
    window.blit(img_raposa_TelaInicial, (100,150))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
if game:
    #window = pygame.display.set_mode((LARGURA_TELA_JOGO, ALTURA_TELA_JOGO))
    pygame.display.set_caption(Nome_Jogo)

estagio = 0
status_musica = 0
while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
            musica_jogo.stop()
        elif event.type == pygame.KEYDOWN and (estagio == 0 or estagio == 1):
            estagio += 1
    
    window.fill((255, 255, 255))
    if estagio == 0:
        window.blit(txt_Pre_Tutorial,(0,0))
    elif estagio == 1:
        window.blit(txt_Tutorial,(0,0))
    else:
        window.blit(txt_Jogo,(0,0))
    if estagio == 2 and status_musica == 0:
        status_musica += 1
        musica_jogo.play(-1)
    
    



    # ----- Gera saídas
    #window.blit(img_fase1, (0,0))
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados