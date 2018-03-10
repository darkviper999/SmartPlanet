from Core import *
from Story import*


def menu():
    bg = BACKGROUND([0,0],"menu\\cover2.png")
    button_s = BACKGROUND([25,300],"menu\\button_s.png")
    button_e = BACKGROUND([25,446],"menu\\button_e.png")
    button_h = BACKGROUND([442,300],"menu\\button_h.png")
    button_c = BACKGROUND([442,446],"menu\\button_c.png")
    popup = BACKGROUND([0,0],"void.png")
    pygame.mixer.music.load("BGM\\Menu.ogg")
    cursorcount = 0
    cursor = pygame.mixer.Sound("SFX\\cursor.ogg")
    done = False
    skipStory = False
    pygame.mixer.music.play(50,11.7)
    while not done:
        bg.render()
        button_s.render()
        button_e.render()
        button_h.render()
        button_c.render()
        popup.render()
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP and popup.imagename != "void.png":
                #close howto
                popup.morph("void.png")
            elif DetectCollision(x,y,1,1,25,300,400,126):
                #click on story
                if cursorcount == 0 and popup.imagename == "void.png":
                    cursor.play()
                    cursorcount = 1
                button_s.morph("menu\\button_s2.png")
                if event.type == pygame.MOUSEBUTTONUP:
                    #storyline
                    if event.button == 3:
                        skipStory = True
                    pygame.mixer.music.stop()
                    if skipStory == False:
                        done = Intro(done)
                        done = Catch(done)
                        done = Duel(done)
                    skipStory = False
                    done = game(0,done)
                    #change music back to menu
                    pygame.mixer.music.load("BGM\\Menu.ogg")
                    pygame.mixer.music.play(50,11.7)
            elif DetectCollision(x,y,1,1,25,446,400,126):
                #click on endless
                if cursorcount == 0 and popup.imagename == "void.png":
                    cursor.play()
                    cursorcount = 1
                button_e.morph("menu\\button_e2.png")
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.mixer.music.stop()
                    done = game(1,done)
                    pygame.mixer.music.load("BGM\\Menu.ogg")
                    pygame.mixer.music.play(50,11.7)
            elif DetectCollision(x,y,1,1,442,300,334,126):
                #click on howto
                if cursorcount == 0 and popup.imagename == "void.png":
                    cursor.play()
                    cursorcount = 1
                button_h.morph("menu\\button_h2.png")
                if event.type == pygame.MOUSEBUTTONUP:
                    popup.morph("Menu\\howto.png")
            elif DetectCollision(x,y,1,1,442,446,334,126):
                #click on credit
                if cursorcount == 0 and popup.imagename == "void.png":
                    cursor.play()
                    cursorcount = 1
                if event.type == pygame.MOUSEBUTTONUP:
                    popup.morph("Menu\\credit.png")
                button_c.morph("menu\\button_c2.png")
            else:
                #blink button
                cursorcount = 0
                button_s.morph("menu\\button_s.png")
                button_e.morph("menu\\button_e.png")
                button_h.morph("menu\\button_h.png")
                button_c.morph("menu\\button_c.png")
        pygame.display.flip()
    pygame.quit()

    
def game(mode = 0,isdone = False):
    #preplay propoties
    sounds = []
    blive = 4
    live = 2
    speed = 4
    bonusscore = 0
    bulletcount = 0
    pygame.mixer.music.load("BGM\\Stage.ogg")
    pygame.mixer.music.play(5,0)
    sounds.append(pygame.mixer.Sound("SFX\\Hit.ogg"))
    appendswitch = 0
    heart = []
    heart.append(SPRITE(0,0,"SPRITE\\heart.png"))
    heart.append(SPRITE(35,0,"SPRITE\\heart.png"))
    heart.append(SPRITE(70,0,"SPRITE\\heart.png"))
    bheart = []
    bheart.append(SPRITE(765,0,"SPRITE\\blueheart.png"))
    bheart.append(SPRITE(730,0,"SPRITE\\blueheart.png"))
    bheart.append(SPRITE(695,0,"SPRITE\\blueheart.png"))
    bheart.append(SPRITE(660,0,"SPRITE\\blueheart.png"))
    bheart.append(SPRITE(625,0,"SPRITE\\blueheart.png"))
    boss = SPRITE(380,50,"SPRITE\\blackwing.png")
    player = SPRITE(380,400,"SPRITE\\whitewing.png")
    bg = BACKGROUND([0,0],"SPRITE\\city2.png")
    blast = BULLET("SPRITE\\blast.png")
    blast.blastspeed()
    isfire = False
    core = CIRCLE()
    phone = []
    boss.setspeed(2)
    for i in range(0,10):
        phone.append(BULLET())
        phone[i].randprop()
    shake = -1
    player.yspeed = 0
    #player moving
    while not isdone:
        if bulletcount%20 == 0 and bulletcount != 0 and appendswitch == 0:
            phone.append(BULLET())
            appendswitch = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isdone = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                isfire = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                speed = 2#slow movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.xspeed = -speed
                elif event.key == pygame.K_RIGHT:
                    player.xspeed = speed
                elif event.key == pygame.K_UP:
                    player.yspeed = -speed
                elif event.key == pygame.K_DOWN:
                    player.yspeed = speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    speed = 4
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.xspeed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.yspeed = 0
            if event.type == pygame.MOUSEBUTTONUP and live == -2:
                #return to menu
                return isdone
        if(core.x+player.xspeed > 0 and core.x+player.xspeed < 795):
            player.x = player.x + player.xspeed
        if(core.y+player.yspeed > 0 and core.y+player.yspeed < 590):
            player.y = player.y + player.yspeed
    #renderer
        if isfire == True:
            blast.falldown()
        else:
            blast.x = player.x+14
            blast.y = player.y+4
        core.x = player.x+19
        core.y = player.y+28
        screen.fill([255,255,255])
        screen.blit(bg.image,bg.rect)
        blast.render()
        player.render()
        boss.render()
        core.render()
        heart[0].render()
        heart[1].render()
        heart[2].render()
        if mode == 0:
            bheart[0].render()
            bheart[1].render()
            bheart[2].render()
            bheart[3].render()
            bheart[4].render()
        
        label = myfont.render('{:^30}'.format("Score: "+str((bulletcount*100)+(bonusscore*100))), 1, (255,255,255))
        #boss motion
        boss.move()
        if boss.x >= 750 or boss.x <= 0:
            boss.setspeed(boss.xspeed*shake)
        #check life
        if live == -1:
            for i in range(0,len(phone)):
                phone.pop()
            boss.morph("void.png")
            player.morph("void.png")
            core.morph("void.png")
            heart[0].morph("void.png")
            heart[1].morph("void.png")
            heart[2].morph("void.png")
            bheart[0].morph("void.png")
            bheart[1].morph("void.png")
            bheart[2].morph("void.png")
            bheart[3].morph("void.png")
            bheart[4].morph("void.png")
            blast.Transparent()
            if mode == 0:
                #lose cutscene
                Lose()
            else:
                pygame.mixer.music.load("BGM\\end.ogg")
                pygame.mixer.music.play(1,0.5)
            bg.morph("CG\\smartplanet.png")
            live = -2#show score
        elif live == -2 and mode == 1:
                screen.blit(label,[165,555])
        else:
            if mode == 0:
                #win in story mode
                if bulletcount >= 100 or blive == -1:
                    for i in range(0,len(phone)):
                        phone.pop()
                    isdone = Win()
                    blive = 4
                    return done
            for i in range(0,len(phone)):
                phone[i].falldown()
                if phone[i].is_hitted(core.x,core.y) == True:
                    heart[live].morph("SPRITE\\empty_heart.png")
                    heart[live].render()
                    live-=1
                    sounds[0].play()
                    if mode == 1:
                        bonusscore+=1
                if phone[i].y >= 600:
                    phone[i].randprop()
                    phone[i].y = 0
                    phone[i].ishit = 0
                    bulletcount+=1
                    appendswitch = 0
                phone[i].render()
        if isfire == True:
            if DetectCollision(blast.x,blast.y,20,35,boss.x,boss.y,50,50):
                if mode == 0:
                    bheart[blive].morph("SPRITE\\empty_heart.png")
                    bheart[blive].render()
                    blive-=1
                sounds[0].play()
                bonusscore+=1
                isfire = False
            elif blast.y <= 0:
                isfire = False
                
        clock.tick(60)
        ticker = pygame.time.get_ticks()
        pygame.display.flip()
    return isdone

menu()
