import pygame
from constantes import *
from assets import *
from Classes import *
#from moviepy.editor import VideoFileClip

#tiro_acerta_sound.play(1)

# tiro_acerta_sound.stop
pygame.mixer.init()


#==============================================================================================================

def TelaInicial():

    estado = True

    pygame.display.set_caption(f'Tela Inicial - {Nome_Jogo}')
    
    # ----- Inicia estruturas de dados
    tela_inicial = True
    
    # Tocar a música uma vez antes do loop de eventos
    musica_tela_inicial.play(-1)

    # ===== Loop principal =====
    while tela_inicial:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                tela_inicial = False
                musica_tela_inicial.stop()
                continue
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                tela_inicial = False
                musica_tela_inicial.stop()
                continue

        # ----- Gera saídas
        window.blit(img_TelaInicial, (0, 0))
        window.blit(img_raposa_TelaInicial, (150, 200))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return estado


#==============================================================================================================


def TelaTutorial(Tutorial):
    estado = Tutorial
    pygame.display.set_caption(f'Tutorial - {Nome_Jogo}')
    while Tutorial:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                Tutorial = False
                
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                Tutorial = False
        window.blit(img_Tutorial,(0,0))
        pygame.display.update()  # Mostra o novo frame para o jogador
    return estado

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
    transicao = False
    if score >= 100 and fase == 1:
        transicao = True
        fase = 2
    elif score >= 250 and fase == 2:
        transicao = True
        fase = 3
    elif score >= 400 and fase == 3:
        transicao = True
        fase = 4
    fase_transicao = [fase,transicao]
    return fase_transicao

#==============================================================================================================

def TelaGame (game):
    end = game
    fase = 1
    # Criando um grupo de icones
    all_icones = IconesSpriteGroup(5,fase)

    mouse_sprite = MouseSprite()
    mouse_group = pygame.sprite.Group()
    mouse_group.add(mouse_sprite)


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
                        #if icone.rect.collidepoint(event.pos):

                        if pygame.sprite.collide_mask(icone, mouse_sprite):
                            if (icone.image in lista_icones_viloes):
                                icone.kill()
                                tiro_acerta_sound.play()
                                score = AddPontucao(icone,score)
                            else:
                                # som de morte raposa
                                grito_raposinha.play()
                                pygame.time.delay(1000)
                                TelaMorte(end,"raposa",score)
                                game = False

        for icone in all_icones:
            if (icone.rect.bottom >= ALTURA_TELA):
                if icone.image != img_raposa:
                    vidas -= 1
                icone.kill()
        
        if vidas == 0:
            TelaMorte(end,"vidas",score)
            game = False
                

        estado_fase = DefineFase(score,fase)
        fase = estado_fase[0]
        transicao = estado_fase[1]

        if transicao == True:
            PrimeiraTransicaoTelas()
            score = FaseBonus(score)
            SegundaTransicaoTelas()

        if len(all_icones) == 0:
            pygame.display.update()
            all_icones = IconesSpriteGroup(5,fase)
            #pygame.display.update()
            #pygame.time.delay(1000)

        all_icones.update()
        mouse_group.update()


        DefineTela(fase)

        # Desenhando Ícones
        all_icones.draw(window)
        mouse_group.draw(window)


        score_txt = score_font.render(f'SCORE:{score}', True, (0, 0, 0))
        window.blit(score_txt, (350, 20))
        
        Coracoes(vidas)


        if game:
            pygame.display.update()  # Mostra o novo frame para o jogador

    return end

#==============================================================================================================

def TelaMorte(end, tipo,score):
    pygame.display.set_caption(f'Fim de Jogo - {Nome_Jogo}')
    while end:
        # ----- Trata eventos
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                end = False
            elif event.type == pygame.KEYDOWN:
                end = False

        pontos = final_score_font.render(f'FINAL SCORE: {score}', True, (255, 165, 0))

        if tipo == "raposa":
            window.blit(img_TeladeMorte_raposa, (0, 0))
            window.blit(pontos, (550, 400))

        elif tipo == "vidas":
            window.blit(img_TeladeMorte_vidas, (0, 0))
            window.blit(pontos, (350, 420))

        pygame.display.update()  # Mostra o novo frame para o jogador


#===============================================================================================


def FaseBonusxxx(score):

    pygame.display.set_caption(f'Fase Bônus - {Nome_Jogo}')

    player_x = LARGURA_TELA // 2
    player_y = ALTURA_TELA - 100
    player_speed = 10

    raposas = []
    falling_speed = 5

    game_duration = 20000
    pygame.time.set_timer(pygame.USEREVENT, game_duration)

    running = True

    while running:
        clock.tick(FPS/1.3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                running = False

        # Movimentação do jogador
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if tecla[pygame.K_RIGHT] and player_x < LARGURA_TELA - 50:
            player_x += player_speed

        # Adiciona novos objetos que caem
        if random.randint(1, 20) == 1:
            raposas.append([random.randint(0, LARGURA_TELA - 50), 0])

        # Atualiza a posição dos objetos que caem
        for raposa in raposas:
            raposa[1] += falling_speed
            # Verifica colisão com o jogador
            if player_x < raposa[0] < player_x + 50 and player_y < raposa[1] < player_y + 50:
                score += 2
                raposas.remove(raposa)
            # Remove objetos que saem da tela
            elif raposa[1] > ALTURA_TELA:
                raposas.remove(raposa)

        # Desenha na tela
        window.blit(img_fundo_fase_bonus, (0,0))
        window.blit(img_cesta, (player_x, player_y))
        for obj in raposas:
            window.blit(img_raposa_fase_bonus, obj)

        score_txt = score_font.render(f'SCORE:{score}', True, (0, 0, 0))
        window.blit(score_txt, (350, 20))

        pygame.display.update()
    
    return score

#=============================================================

player_mask = pygame.mask.from_surface(img_cesta)
raposa_mask = pygame.mask.from_surface(img_raposa_fase_bonus)

def FaseBonus(score):

    pygame.display.set_caption(f'Fase Bônus - {Nome_Jogo}')

    player_x = LARGURA_TELA // 2
    player_y = ALTURA_TELA - 100
    player_speed = 10

    raposas = []
    falling_speed = 5

    game_duration = 15000
    pygame.time.set_timer(pygame.USEREVENT, game_duration)

    running = True

    while running:
        clock.tick(FPS/1.4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                running = False

        # Movimentação do jogador
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if tecla[pygame.K_RIGHT] and player_x < LARGURA_TELA - 50:
            player_x += player_speed

        # Adiciona novos objetos que caem
        if random.randint(1, 20) == 1:
            raposas.append([random.randint(0, LARGURA_TELA - 50), 0])

        # Atualiza a posição dos objetos que caem
        for raposa in raposas:
            raposa[1] += falling_speed
            if player_mask.overlap(raposa_mask, (player_x - raposa[0], player_y - raposa[1])):
                score += 2
                raposas.remove(raposa)


        # Desenha na tela
        window.blit(img_fundo_fase_bonus, (0,0))
        window.blit(img_cesta, (player_x, player_y))
        for obj in raposas:
            window.blit(img_raposa_fase_bonus, obj)

        score_txt = score_font.render(f'SCORE:{score}', True, (0, 0, 0))
        window.blit(score_txt, (350, 20))

        pygame.display.update()
    
    return score


#=============================================================================


def Coracoes(vidas):
    if vidas == 5:
        window.blit(img_coracao, (15, 15))
        window.blit(img_coracao, (50, 15))
        window.blit(img_coracao, (85, 15))
        window.blit(img_coracao, (120, 15))
        window.blit(img_coracao, (155, 15))
    elif vidas == 4:
        window.blit(img_coracao, (15, 15))
        window.blit(img_coracao, (50, 15))
        window.blit(img_coracao, (85, 15))
        window.blit(img_coracao, (120, 15))
    elif vidas == 3:
        window.blit(img_coracao, (15, 15))
        window.blit(img_coracao, (50, 15))
        window.blit(img_coracao, (85, 15))
    elif vidas == 2:
        window.blit(img_coracao, (15, 15))
        window.blit(img_coracao, (50, 15))
    elif vidas == 1:
        window.blit(img_coracao, (15, 15))

def PrimeiraTransicaoTelas():
    pygame.display.set_caption(f'Transição - {Nome_Jogo}')

    transition_duration = 3000
    
    pygame.time.set_timer(pygame.USEREVENT, transition_duration)

    transitioning = True

    while transitioning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                transitioning = False
            elif event.type == pygame.USEREVENT:
                transitioning = False      
        
        window.blit(img_transicao_indo, (0, 0))

        pygame.display.update()  # Mostra o novo frame para o jogador

def SegundaTransicaoTelas():
    pygame.display.set_caption(f'Transição - {Nome_Jogo}')

    transition_duration = 3000
    
    pygame.time.set_timer(pygame.USEREVENT, transition_duration)

    transitioning = True

    while transitioning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                transitioning = False
            elif event.type == pygame.USEREVENT:
                transitioning = False      
        
        window.blit(img_transicao_saindo, (0, 0))

        pygame.display.update()  # Mostra o novo frame para o jogador