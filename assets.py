import pygame
ALTURA_TELA = 650
LARGURA_TELA = (16/10)*ALTURA_TELA

ALTURA_LARGURA_ICONES = ALTURA_TELA//5

ALTURA_LARGURA_VIDAS = ALTURA_TELA//15

pygame.init()
# ----- Gera tela inicial
window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.mixer.init()

# ------- Assets dos Textos

#Título da Tela Inicial
font_txt_TelaInicial = pygame.font.SysFont("cambria", 66, True)
txt_TelaInicial = font_txt_TelaInicial.render("INSPER INVASION", True, (255,0,0))

#Mensagem de "Pressione qualquer botão" da Tela Inicial
font_txt_Pressioneqlqrbotao = pygame.font.SysFont(None,46)
txt_Pressioneqlqrbotao = font_txt_Pressioneqlqrbotao.render("Pressione qualquer botão para iniciar o jogo!", True, (0,0,0))


# Fonte do score board
score_font = ('fontes/PressStart2P.ttf')
score_font = pygame.font.Font(score_font, 42)


# ------- Assets das Músicas de Fundo
#Música da Tela Inicial - Back in Black
musica_tela_inicial = pygame.mixer.Sound('audios/ACDC - Back In Black (Official Music Video).mp3')

##Música do Jogo - Missão Impossível
#musica_jogo = pygame.mixer.Sound("audios/Missao_Impossivel.mp3")


# ------- Assets Sons do Jogo
# som do tiro quando acerta
tiro_acerta_sound = pygame.mixer.Sound('audios/tiro.wav')
grito_raposinha = pygame.mixer.Sound('audios/grito_classico.wav')
pygame.mixer.music.set_volume(0.4)


# ------- Assets das Imagens
# Imagens Tela Inicial
#Imagem do Insper da Tela Inicial
img_TelaInicial = pygame.image.load("Fotos/Foto_TelaInicial.jpg")
img_TelaInicial = pygame.transform.scale(img_TelaInicial, (LARGURA_TELA, ALTURA_TELA))

#Imagem da Raposa da Tela Inicial
img_raposa_TelaInicial = pygame.image.load("Fotos/raposa_foto_tela_inicial.png")
img_raposa_TelaInicial = pygame.transform.scale(img_raposa_TelaInicial, (450, 450))


# Imagens das Telas de Morte
#Imagem da Tela de Morte por vidas
img_TeladeMorte_vidas = pygame.image.load("Fotos/Tela_de_morte_vidas.png")
img_TeladeMorte_vidas = pygame.transform.scale(img_TeladeMorte_vidas, (LARGURA_TELA, ALTURA_TELA))
#Imagem da Tela de Morte por raposa
img_TeladeMorte_raposa = pygame.image.load("Fotos/Tela_de_morte_raposa.png")
img_TeladeMorte_raposa = pygame.transform.scale(img_TeladeMorte_raposa, (LARGURA_TELA, ALTURA_TELA))


# Imagem da Tela de Tutorial
img_Tutorial = pygame.image.load("Fotos/Tela_Tutorial.png")
img_Tutorial = pygame.transform.scale(img_Tutorial, (LARGURA_TELA, ALTURA_TELA))


# Imagens Tela Bônus 
#Imagem da cesta
img_cesta = pygame.image.load("Fotos/cesta_fasebonus.png")
img_cesta = pygame.transform.scale(img_cesta, (ALTURA_LARGURA_ICONES/1.5, ALTURA_LARGURA_ICONES/3))

#Imagem icone raposa para a Tela bonus
img_raposa_fase_bonus = pygame.image.load("Fotos/icone_raposa.png")
img_raposa_fase_bonus = pygame.transform.scale(img_raposa_fase_bonus, (ALTURA_LARGURA_ICONES/2, ALTURA_LARGURA_ICONES/2))


# Imagens de fundo fases do jogo
#Imagem da Entrada do P2 da Primeira Fase do Jogo
img_fase1 = pygame.image.load("Fotos/fundo_nivel1.jpg")
img_fase1 = pygame.transform.scale(img_fase1, (LARGURA_TELA, ALTURA_TELA))

#Imagem do Segundo andar do P2 da Segunda Fase do Jogo
img_fase2 = pygame.image.load("Fotos/fundo_nivel2.jpg")
img_fase2 = pygame.transform.scale(img_fase2, (LARGURA_TELA, ALTURA_TELA))

#Imagem do FabLab da Terceira Fase do Jogo
img_fase3 = pygame.image.load("Fotos/fundo_nivel3.jpg")
img_fase3 = pygame.transform.scale(img_fase3, (LARGURA_TELA, ALTURA_TELA))

#Imagem do Terraço do P2 da Quarta/Última Fase do Jogo
img_fase4 = pygame.image.load("Fotos/fundo_nivel4.jpg")
img_fase4 = pygame.transform.scale(img_fase4, (LARGURA_TELA, ALTURA_TELA))

img_fundo_fase_bonus = pygame.image.load("Fotos/fundo_tela_bonus.jpg")
img_fundo_fase_bonus = pygame.transform.scale(img_fundo_fase_bonus, (LARGURA_TELA, ALTURA_TELA))


# Ícones do jogo
#Ícone do Polvo para o Jogo
img_polvo = pygame.image.load("Fotos/icone_polvo.png")
img_polvo = pygame.transform.scale(img_polvo, (ALTURA_LARGURA_ICONES, ALTURA_LARGURA_ICONES))

#Ícone do Canguru para o Jogo
img_canguru = pygame.image.load("Fotos/icone_canguru.png")
img_canguru = pygame.transform.scale(img_canguru, (ALTURA_LARGURA_ICONES, ALTURA_LARGURA_ICONES))

#Ícone do Rato para o Jogo
img_rato = pygame.image.load("Fotos/icone_rato.png")
img_rato = pygame.transform.scale(img_rato, (ALTURA_LARGURA_ICONES, ALTURA_LARGURA_ICONES))

#Ícone do Jacaré para o Jogo
img_jacare = pygame.image.load("Fotos/icone_jacare.png")
img_jacare = pygame.transform.scale(img_jacare, (ALTURA_LARGURA_ICONES, ALTURA_LARGURA_ICONES))

#Ícone da Raposa para o Jogo
img_raposa = pygame.image.load("Fotos/icone_raposa.png")
img_raposa = pygame.transform.scale(img_raposa, (ALTURA_LARGURA_ICONES, ALTURA_LARGURA_ICONES))


# Imagens de transição de fases (indo e saindo da fase bônus)
# Imagem indo para a fase bônus
img_transicao_indo = pygame.image.load("Fotos/fundo_transicao_indo.png")
img_transicao_indo = pygame.transform.scale(img_transicao_indo, (LARGURA_TELA, ALTURA_TELA))

# Imagem saindo para a fase bônus
img_transicao_saindo = pygame.image.load("Fotos/fundo_transicao_saindo.png")
img_transicao_saindo = pygame.transform.scale(img_transicao_saindo, (LARGURA_TELA, ALTURA_TELA))


# Outras imagens
# Coração (vidas restantes)
img_coracao= pygame.image.load("Fotos/Coração_vidas.png")
img_coracao = pygame.transform.scale(img_coracao, (ALTURA_LARGURA_VIDAS, ALTURA_LARGURA_VIDAS))


# -------- Gerando Janela do Jogo
window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))