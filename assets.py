import pygame
ALTURA_TELA = 650
LARGURA_TELA = (16/10)*ALTURA_TELA

ALTURA_LARGURA_ICONES = ALTURA_TELA//5

pygame.init()

# ------- Assets dos Textos

#Título da Tela Inicial
font_txt_TelaInicial = pygame.font.SysFont("cambria", 66, True)
txt_TelaInicial = font_txt_TelaInicial.render("INSPER INVASION", True, (255,0,0))
#Mensagem de "Pressione qualquer botão" da Tela Inicial
font_txt_Pressioneqlqrbotao = pygame.font.SysFont(None,46)
txt_Pressioneqlqrbotao = font_txt_Pressioneqlqrbotao.render("Pressione qualquer botão para iniciar o jogo!", True, (0,0,0))
#Título da Página de Tutorial
font_txt_Tutorial = pygame.font.SysFont("cambria", 56, True)
txt_Tutorial = font_txt_Tutorial.render("Clique para pular o Tutorial", True, (255,0,0))
#Título da Página de Pré-Tutorial
font_txt_Pre_Tutorial = pygame.font.SysFont("cambria", 56, True)
txt_Pre_Tutorial = font_txt_Pre_Tutorial.render("Clique para Iniciar o Tutorial", True, (255,0,0))
#Título da Página do Jogo
font_txt_Jogo = pygame.font.SysFont("cambria", 56, True)
txt_Jogo = font_txt_Jogo.render("Jogo", True, (255,0,0))
#Título da Página de Derrota
font_txt_Final = pygame.font.SysFont("cambria", 56, True)
txt_Final = font_txt_Final.render("Jogo", True, (255,0,0))

# Textos das Telas Finais
#Título da Tela Final (matou a raposa)
font_txt_tela_morte_raposa = pygame.font.SysFont("cambria", 66, True)
font_txt_tela_morte_raposa = font_txt_tela_morte_raposa.render("Você matou a raposa bebê!", True, (255,250,205))
#GAME OVER
font_txt_game_over = pygame.font.SysFont("cambria", 76, True)
font_txt_game_over = font_txt_game_over.render("GAME OVER", True, (255,0,0))
#Título da Tela Final (perdeu as vidas)
font_txt_tela_final_vidas = pygame.font.SysFont("cambria", 56, True)
font_txt_tela_final_vidas = font_txt_tela_final_vidas.render("Os mascotes invadiram a faculdade!", True, (255,250,205))


# Fonte do score board
score_font = pygame.font.SysFont(None, 60)



# ------- Assets das Músicas de Fundo
#Música da Tela Inicial - Back in Black
musica_tela_inicial = pygame.mixer.Sound('Áudios/ACDC - Back In Black (Official Music Video).mp3')
#Música do Jogo - Missão Impossível
musica_jogo = pygame.mixer.Sound("Áudios/Missao_Impossivel.mp3")



# ------- Assets das Imagens
# Imagens Tela Inicial
#Imagem do Insper da Tela Inicial
img_TelaInicial = pygame.image.load("Fotos/Foto_TelaInicial.jpg")
img_TelaInicial = pygame.transform.scale(img_TelaInicial, (LARGURA_TELA, ALTURA_TELA))

#Imagem da Raposa da Tela Inicial
img_raposa_TelaInicial = pygame.image.load("Fotos/raposa_foto_tela_inicial.png")
img_raposa_TelaInicial = pygame.transform.scale(img_raposa_TelaInicial, (450, 450))


# Imagens Tela Final 1
#Imagem do crocodilo da Tela Final 1
img_crocodilo_TelaFinal = pygame.image.load("Fotos/telafinal_crocodilo.png")
img_crocodilo_TelaFinal = pygame.transform.scale(img_crocodilo_TelaFinal, (450, 450))

#Imagem do rato da Tela Final 1
img_rato_TelaFinal = pygame.image.load("Fotos/telafinal_rato.png")
img_rato_TelaFinal = pygame.transform.scale(img_rato_TelaFinal, (400, 400))

#Imagem do canguru da Tela Final 1
img_canguru_TelaFinal = pygame.image.load("Fotos/telafinal_canguru.png")
img_canguru_TelaFinal = pygame.transform.scale(img_canguru_TelaFinal, (450, 450))


# Imagens Tela Final 2
#Imagem da Raposa da Tela Final 2
img_raposa_chorando_TelaFinal = pygame.image.load("Fotos/raposa_chorando_telafinal.png")
img_raposa_chorando_TelaFinal = pygame.transform.scale(img_raposa_chorando_TelaFinal, (450, 450))

#Imagem 2 da Raposa da Tela Final 2
img_raposa_chorando_TelaFinal2 = pygame.image.load("Fotos/raposa_chorando_telafinal2.png")
img_raposa_chorando_TelaFinal2 = pygame.transform.scale(img_raposa_chorando_TelaFinal2, (540, 756))


# Imagens de fundo fases do jogo
#Imagem da Entrada do P2 da Primeira Fase do Jogo
img_fase1 = pygame.image.load("Fotos/fundo_nivel1.jpg")
img_fase1 = pygame.transform.scale(img_fase1, (LARGURA_TELA, ALTURA_TELA))

#Imagem do Segundo andar do P2 da Segunda Fase do Jogo
img_fase2 = pygame.image.load("Fotos/fundo_nivel2.jpg")
img_fase2 = pygame.transform.scale(img_fase1, (LARGURA_TELA, ALTURA_TELA))

#Imagem do FabLab da Terceira Fase do Jogo
img_fase3 = pygame.image.load("Fotos/fundo_nivel3.jpg")
img_fase3 = pygame.transform.scale(img_fase1, (LARGURA_TELA, ALTURA_TELA))

#Imagem do Terraço do P2 da Quarta/Última Fase do Jogo
img_fase4 = pygame.image.load("Fotos/fundo_nivel4.jpg")
img_fase4 = pygame.transform.scale(img_fase1, (LARGURA_TELA, ALTURA_TELA))


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



# -------- Gerando Janela do Jogo
window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))