from assets import img_jacare,img_canguru,img_polvo,img_rato,img_raposa

ALTURA_TELA = 500
LARGURA_TELA = 800
FPS = 75

#ALTURA_TELA_INICIAL= 600
#LARGURA_TELA_INICIAL = 450

# DEFININDO AS CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

Nome_Jogo = "INSPER INVASION"


Bosses = {0:img_polvo, 1:img_canguru, 2:img_rato, 3:img_jacare, 4:img_raposa}

boss_n1 = [0,0,0,0,0,0,0,4,4,4]
boss_n2 = [0,0,0,1,1,1,1,4,4,4]
boss_n3 = [0,1,1,1,2,2,2,4,4,4]
boss_final = [3,3,3,3,3,3,3,4,4,4]

lista_icones_viloes = [img_polvo,img_canguru,img_rato,img_jacare]

Tempo_Ar = 2 #Segundos