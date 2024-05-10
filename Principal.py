import pygame
from constantes import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela inicial
window = pygame.display.set_mode((ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL))
pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')

# ----- Criando o Fundo Tela Inicial
img_TelaInicial = pygame.image.load("Fotos/Foto_TelaInicial.jpg")
img_TelaInicial = pygame.transform.scale(img_TelaInicial, (ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL))
img_fase1 = pygame.image.load("Fotos/fundo_nivel1.jpg")
img_fase1 = pygame.transform.scale(img_fase1, (ALTURA_TELA_JOGO, LARGURA_TELA_JOGO))

# ----- Inicia Assets
font_txt_TelaInicial = pygame.font.SysFont("cambria", 56, True)
txt_TelaInicial = font_txt_TelaInicial.render("INSPER INVASION", True, (255,0,0))
font_txt_Pressioneqlqrbotao = pygame.font.SysFont(None,36)
txt_Pressioneqlqrbotao = font_txt_Pressioneqlqrbotao.render("Pressione qualquer botão para iniciar o jogo!", True, (0,0,0))
font_txt_Tutorial = pygame.font.SysFont("cambria", 56, True)
txt_Tutorial = font_txt_Tutorial.render("Clique para pular o Tutorial", True, (255,0,0))
font_txt_Pre_Tutorial = pygame.font.SysFont("cambria", 56, True)
txt_Pre_Tutorial = font_txt_Pre_Tutorial.render("Clique para Iniciar o Tutorial", True, (255,0,0))
font_txt_Jogo = pygame.font.SysFont("cambria", 56, True)
txt_Jogo = font_txt_Jogo.render("Jogo", True, (255,0,0))

musica_de_fundo = pygame.mixer.Sound('Áudios/ACDC - Back In Black (Official Music Video).mp3')

# ----- Inicia estruturas de dados
game = True
tela_inicial = True
# ===== Loop principal =====
while tela_inicial:
    musica_de_fundo.play(-1)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            tela_inicial = False
            game = False
            musica_de_fundo.stop()
            continue
        elif event.type == pygame.KEYDOWN:
            tela_inicial = False
            musica_de_fundo.stop()
            continue

    # ----- Gera saídas
    window.blit(img_TelaInicial, (0,0))
    window.blit(txt_TelaInicial, (84,20))
    window.blit(txt_Pressioneqlqrbotao, (40,100))   

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
if game:
    window = pygame.display.set_mode((LARGURA_TELA_JOGO, ALTURA_TELA_JOGO))
    pygame.display.set_caption(Nome_Jogo)

estagio = 0
while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN and (estagio == 0 or estagio == 1):
            estagio += 1
    
    window.fill((255, 255, 255))
    if estagio == 0:
        window.blit(txt_Pre_Tutorial,(0,0))
    elif estagio == 1:
        window.blit(txt_Tutorial,(0,0))
    else:
        window.blit(txt_Jogo,(0,0))

    # ----- Gera saídas
    #window.blit(img_fase1, (0,0))
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados