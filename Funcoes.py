import pygame
from constantes import *
from assets import *
from Classes import *
#from moviepy.editor import VideoFileClip

#tiro_acerta_sound.play(1)

# tiro_acerta_sound.stop
pygame.mixer.init()
#==============================================================================================================

def TelaInicial ():
    game_status = True
    pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')
    # ----- Inicia estruturas de dados
    tela_inicial = True
    # ===== Loop principal =====
    while tela_inicial:
        musica_tela_inicial.play(-1)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                tela_inicial = False
                game_status = False
                musica_tela_inicial.stop()
                continue
            elif event.type == pygame.KEYDOWN:
                tela_inicial = False
                musica_tela_inicial.stop()
                continue
            else:
                musica_tela_inicial.stop()
                continue

        # ----- Gera saídas
        window.blit(img_TelaInicial, (0,0))
        window.blit(txt_TelaInicial, (270,20))
        window.blit(txt_Pressioneqlqrbotao, (180,120))
        window.blit(img_raposa_TelaInicial, (150,200))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return game_status

#==============================================================================================================

def TelaPreTutorial(PreTutorial):
    Tutorial = PreTutorial
    pygame.display.set_caption(f'Pré-Tutorial - {Nome_Jogo}')
    while PreTutorial:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                PreTutorial = False
                Tutorial = False
                musica_jogo.stop()
            elif event.type == pygame.KEYDOWN:
                PreTutorial = False
        window.fill((255, 255, 255))
        window.blit(txt_Pre_Tutorial,(0,0))
        pygame.display.update()  # Mostra o novo frame para o jogador
    return Tutorial

#==============================================================================================================

def TelaTutorial(Tutorial):
    game = Tutorial
    pygame.display.set_caption(f'Tutorial - {Nome_Jogo}')
    while Tutorial:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                Tutorial = False
                game = False
                musica_jogo.stop()
            elif event.type == pygame.KEYDOWN:
                Tutorial = False
        window.fill((255, 255, 255))
        window.blit(txt_Tutorial,(0,0))
        pygame.display.update()  # Mostra o novo frame para o jogador
    return game

#==============================================================================================================

def IconesSpriteGroup (n,fase):
    all_icones = pygame.sprite.Group()
    for i in range(n):
        if fase == 1:
            n_icone = random.randint(0,len(boss_n1)-1)
            icone = Icones(Bosses[boss_n1[n_icone]])
        elif fase == 2:
            n_icone = random.randint(0,len(boss_n2)-1)
            icone = Icones(Bosses[boss_n2[n_icone]])
        elif fase == 3:
            n_icone = random.randint(0,len(boss_n3)-1)
            icone = Icones(Bosses[boss_n3[n_icone]])
        elif fase == 4:
            n_icone = random.randint(0,len(boss_final)-1)
            icone = Icones(Bosses[boss_final[n_icone]])
        all_icones.add(icone)
    return all_icones

#==============================================================================================================

def AddPontucao (icone, score):
    if icone.image == img_polvo:
        score += 5
    elif icone.image == img_canguru:
        score += 10
    elif icone.image == img_rato:
        score += 15
    elif icone.image == img_jacare:
        score += 20
    return score

#==============================================================================================================

def DefineTela (fase):
    if fase == 1:
        window.blit(img_fase1, (0, 0)) #Preenche com a Imagem de Fundo
    elif fase == 2:
        window.blit(img_fase2, (0, 0)) #Preenche com a Imagem de Fundo
    elif fase == 3:
        window.blit(img_fase3, (0, 0)) #Preenche com a Imagem de Fundo
    elif fase == 4:
        window.blit(img_fase4, (0, 0)) #Preenche com a Imagem de Fundo

#==============================================================================================================
  
def DefineFase (score,fase):
    if score >= 100 and fase == 1:
        fase = 2
    elif score >= 250 and fase == 2:
        fase = 3
    elif score >= 400 and fase == 3:
        fase = 4
    return fase   

#==============================================================================================================

def TelaGame (game):
    end = game
    fase = 1
    # Criando um grupo de icones
    all_icones = IconesSpriteGroup(5,fase)

    vidas = 5
    score = 0
    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
    # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                end = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    for icone in all_icones:   
                        if icone.rect.collidepoint(event.pos):
                            if (icone.image in lista_icones_viloes):
                                icone.kill()
                                tiro_acerta_sound.play()
                                score = AddPontucao(icone,score)
                            else:
                                # som de morte raposa
                                pygame.time.delay(1000)
                                TelaFinal(end,"raposa")
                                game = False
                                

        for icone in all_icones:
            if (icone.rect.bottom >= ALTURA_TELA):
                if icone.image != img_raposa:
                    vidas -= 1
                icone.kill()
        
        if vidas == 0:
            TelaFinal(end,"vidas")
            game = False

        fase = DefineFase(score,fase)
        if len(all_icones) == 0:
            pygame.display.update()
            all_icones = IconesSpriteGroup(5,fase)
            #pygame.display.update()
            #pygame.time.delay(1000)

        all_icones.update()

        DefineTela(fase)

        # Desenhando Ícones
        all_icones.draw(window)

        score_txt = score_font.render(str(score), True, (255,0,0))
        window.blit(score_txt, (10, 10))

        vidas_txt = vidas_font.render(str(vidas), True, (255,0,0))
        window.blit(vidas_txt, (100, 10))

        if game:
            pygame.display.update()  # Mostra o novo frame para o jogador

    return end

#==============================================================================================================

def TelaFinal(end, tipo):
    pygame.display.set_caption(f'Fim de Jogo - {Nome_Jogo}')
    while end:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                end = False

        if tipo == "raposa":
            window.blit(img_TeladeMorte_raposa, (0, 0))

        elif tipo == "vidas":
            window.blit(img_TeladeMorte_vidas, (0, 0))

        pygame.display.update()  # Mostra o novo frame para o jogador

def PlacarFinal(end,score):
    pygame.display.set_caption(f'Pontuação final - {Nome_Jogo}')
    while end:
        x = 1

def FaseBonus(end, all_icones):
    cesta = Cesta(img_cesta)
    

    while end:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                end = False

            if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    cesta.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    cesta.speedx += 8
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    cesta.speedx += 8
                if event.key == pygame.K_RIGHT:
                    cesta.speedx -= 8
        cesta.update()

        for icone in all_icones:
            hits = pygame.sprite.spritecollide(cesta, all_icones, True)
            if len(hits) > 0:
                icone.kill()
                points = 30
                score = AddPontucao(points,score)


        pygame.display.update()  # Mostra o novo frame para o jogador

"""
def TelaRanking (status_ranking, score):
    window.fill(WHITE)
    window.blit(font_txt_game_over, (315,10))
    window.blit(font_txt_tela_ranking, (315,10))
    while status_ranking:
        for event in pygame.event.get():
            if event 
        with open('Ranking.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for indice_linha in range(len(linhas)):
                pontuacao_nome = linhas[indice_linha].split(':')
                pontuacao = pontuacao_nome[0]
                nome = pontuacao_nome[1]
                if pontuacao < score:
                    window.fill(WHITE)
                    window.blit(font_txt_game_over, (315,10))
                    window.blit(font_txt_game_over, (315,10))
                    """