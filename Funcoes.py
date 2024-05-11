import pygame
from constantes import *
from assets import *
from Classes import *

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

        # ----- Gera saídas
        window.blit(img_TelaInicial, (0,0))
        window.blit(txt_TelaInicial, (270,20))
        window.blit(txt_Pressioneqlqrbotao, (180,120))
        window.blit(img_raposa_TelaInicial, (150,200))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return game_status

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


def IconesSpriteGroup (n):
    all_icones = pygame.sprite.Group()
    for i in range(n):
        n_icone = random.randint(0,len(boss_n1)-1)
        icone = Icones(Bosses[boss_n1[n_icone]])
        all_icones.add(icone)
    return all_icones


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


def TelaGame (game):
    end = game
    # Criando um grupo de icones
    all_icones = IconesSpriteGroup(5)

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
                                score = AddPontucao(icone,score)
                            else:
                                pygame.time.delay(1000)
                                game = False
        
        for icone in all_icones:
            if icone.rect.bottom >= ALTURA_TELA:
                icone.kill()
        if len(all_icones) == 0:
            pygame.display.update()
            all_icones = IconesSpriteGroup(5)
            pygame.time.delay(1000)

        all_icones.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(img_fase1, (0, 0)) #Preenche com a Imagem de Fundo
        # Desenhando Ícones
        all_icones.draw(window)

        score_txt = score_font.render(str(score), True, (255,0,0))
        window.blit(score_txt, (10, 10))

        if game:
            pygame.display.update()  # Mostra o novo frame para o jogador

    return end


def TelaFinal(end):
    pygame.display.set_caption(f'Fim de Jogo - {Nome_Jogo}')
    while end:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                end = False
        window.fill((255, 255, 255))
        window.blit(txt_Final,(0,0))
        pygame.display.update()  # Mostra o novo frame para o jogador

def TelaFinal_morteraposa ():
    game_status = True
    pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')
    # ----- Inicia estruturas de dados
    tela_final = True
    # ===== Loop principal =====
    while tela_final:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                tela_final = False
                game_status = False
                continue

        # ----- Gera saídas
        window.blit(img_TelaInicial, (0,0))
        window.blit(txt_TelaInicial, (270,20))
        window.blit(txt_Pressioneqlqrbotao, (180,120))
        window.blit(img_raposa_TelaInicial, (150,200))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return game_status