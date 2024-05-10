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

# ----- Inicia Assets
font_txt_TelaInicial = pygame.font.SysFont("cambria", 56, True)
txt_TelaInicial = font_txt_TelaInicial.render("INSPER INVASION", True, (255,0,0))
font_txt_Pressioneqlqrbotao = pygame.font.SysFont(None,36)
txt_Pressioneqlqrbotao = font_txt_Pressioneqlqrbotao.render("Pressione qualquer botão para iniciar o jogo!", True, (0,0,0))


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
            musica_de_fundo.stop()
        elif event.type == pygame.KEYDOWN:
            tela_inicial = False
            musica_de_fundo.stop()

    # ----- Gera saídas
    window.blit(img_TelaInicial, (0,0))
    window.blit(txt_TelaInicial, (84,20))
    window.blit(txt_Pressioneqlqrbotao, (40,100))   

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

window = pygame.display.set_mode((LARGURA_TELA_JOGO, ALTURA_TELA_JOGO))
pygame.display.set_caption(Nome_Jogo)

while game:

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        

    # ----- Gera saídas
    window.blit(img_TelaInicial, (0,0))
    

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados