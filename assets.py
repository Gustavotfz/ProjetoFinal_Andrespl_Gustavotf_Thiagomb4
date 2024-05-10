from constantes import *

# ------- Assets dos Textos
#Título da Tela Inicial
font_txt_TelaInicial = pygame.font.SysFont("cambria", 56, True)
txt_TelaInicial = font_txt_TelaInicial.render("INSPER INVASION", True, (255,0,0))
#Mensagem de "Pressione qualquer botão" da Tela Inicial
font_txt_Pressioneqlqrbotao = pygame.font.SysFont(None,36)
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



# ------- Assets das Músicas de Fundo
#Música da Tela Inicial - Back in Black
musica_tela_inicial = pygame.mixer.Sound('Áudios/ACDC - Back In Black (Official Music Video).mp3')
#Música do Jogo - Missão Impossível
musica_jogo = pygame.mixer.Sound("Áudios/Missao_Impossivel.mp3")



# ------- Assets das Imagens
#Imagem do Insper da Tela Inicial
img_TelaInicial = pygame.image.load("Fotos/Foto_TelaInicial.jpg")
img_TelaInicial = pygame.transform.scale(img_TelaInicial, (ALTURA_TELA_INICIAL, LARGURA_TELA_INICIAL))
#Imagem da Raposa da Tela Inicial
img_raposa_TelaInicial = pygame.image.load("Fotos/raposa_foto_tela_inicial.png")
img_raposa_TelaInicial = pygame.transform.scale(img_raposa_TelaInicial, (300, 300))
#Imagem da Entrada do P2 da Primeira Fase do Jogo
img_fase1 = pygame.image.load("Fotos/fundo_nivel1.jpg")
img_fase1 = pygame.transform.scale(img_fase1, (ALTURA_TELA_JOGO, LARGURA_TELA_JOGO))
