from Core import*
done = False
na = "STORY\\nar.png"
ww = "STORY\\ww.png"
wws = "Story\\wws.png"
bw = "STORY\\bw.png"
bws = "STORY\\bws.png"
box = DIALOGUE("STORY\\nar.png")
text = open("STORY\\intro.txt","r")
def Intro(done = False):
    voicer = 0
    now = 1
    bgm = pygame.mixer.music.load("BGM\\peace.ogg")
    pygame.mixer.music.play(5,0)
    #get dialogue
    clear = len(word)
    for i in range(0,clear):
        word.pop()
    clear = len(order)
    for i in range(0,clear):
        order.pop()
    myfile = open("STORY\\intro.txt","r")
    for line in myfile:
        word.append(line)
    myfile = open("STORY\\intro_order.txt","r")
    for line in myfile:
        order.append(line)
    CGI = BACKGROUND([0,0],"CG\\wizroom1.png")
    CGI.render()
    box.boxrender()
    pygame.display.flip()
    #story loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP and now < len(word)-1 and voicer < len(order)-1:
                if "bgc" in order[voicer]:
                    CGI.morph("CG\\"+order[voicer][:-5]+".png")
                    voicer+=1
                if "bgm" in order[voicer]:
                    pygame.mixer.music.load("BGM\\"+order[voicer][:-5]+".ogg")
                    pygame.mixer.music.play(5,0)
                    voicer+=1
                box.morph("STORY\\"+order[voicer][:-1]+".png")
                CGI.render()
                box.boxrender()
                now = box.massrender(now,ww)
                voicer+=1
                if voicer == len(order)-1:
                    return done
        pygame.display.flip()
    return done

def Catch(done = False):
    voicer = 0
    now = 1
    smoothchap = 0
    #dialogue reset
    clear = len(word)
    for i in range(0,clear):
        word.pop()
    clear = len(order)
    for i in range(0,clear):
        order.pop()
    #get dialogue
    myfile = open("STORY\\catch.txt","r")
    for line in myfile:
        word.append(line)
    myfile = open("STORY\\catch_order.txt","r")
    for line in myfile:
        order.append(line)
    BG1 = BACKGROUND([0,0],"SPRITE\\city2.png")
    BG2 = BACKGROUND([0,-600],"SPRITE\\city2.png")
    bgm = pygame.mixer.music.load("BGM\\catch.ogg")
    player = SPRITE(380,400,"SPRITE\\whitewing.png")
    box.morph("STORY\\ww.png")
    box.boxrender()
    pygame.mixer.music.play(5,0)
    pygame.display.flip()
    #storyloop
    while not done:
        #animated screen
        BG1.falldown()
        BG2.falldown()
        BG1.render()
        BG2.render()
        player.render()
        if BG1.rect.top >= 600:
            BG1.rect.top = -600
        if BG2.rect.top >= 600:
            BG2.rect.top = -600
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP and now < len(word)-1 and voicer < len(order)-1:
                if "bgm" in order[voicer]:
                    pygame.mixer.music.load("BGM\\"+order[voicer][:-5]+".ogg")
                    pygame.mixer.music.play(5,0)
                    voicer+=1
                box.morph("STORY\\"+order[voicer][:-1]+".png")
                box.boxrender()
                now = box.massrender(now,ww)
                voicer+=1
                if voicer == len(order)-2:
                    smoothchap = 1
        if smoothchap == 1 and (BG1.rect.top == 0 or BG2.rect.top == 0):
            return done
        box.boxrender()
        box.massrender(now,ww)       
        clock.tick(60)
        pygame.display.flip()
    return done

def Duel(done = False):
    voicer = 0
    now = 1
    #dialogue reset
    clear = len(word)
    for i in range(0,clear):
        word.pop()
    clear = len(order)
    for i in range(0,clear):
        order.pop()
    #get dialogue
    myfile = open("STORY\\duel.txt","r")
    for line in myfile:
        word.append(line)
    myfile = open("STORY\\duel_order.txt","r")
    for line in myfile:
        order.append(line)
    BG1 = BACKGROUND([0,0],"SPRITE\\city2.png")
    player = SPRITE(380,400,"SPRITE\\whitewing.png")
    boss = SPRITE(380,50,"SPRITE\\blackwing.png")
    BG1.render()
    box.boxrender()
    player.render()
    boss.render()
    pygame.display.flip()
    box.morph(wws)
    box.boxrender()
    now = box.massrender(now,wws)
    #story loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP and now < len(word)-1 and voicer < len(order)-1:
                if "bgc" in order[voicer]:
                    CGI.morph("CG\\"+order[voicer][:-5]+".png")
                    voicer+=1
                if "bgm" in order[voicer]:
                    pygame.mixer.music.load("BGM\\"+order[voicer][:-5]+".ogg")
                    pygame.mixer.music.play(5,0)
                    voicer+=1
                box.morph("STORY\\"+order[voicer][:-1]+".png")
                box.boxrender()
                now = box.massrender(now,ww)
                voicer+=1
                if voicer == len(order)-1:
                    return done
        pygame.display.flip()
    return done

def Win(done = False):
    voicer = 0
    now = 1
    #dialogue reset
    clear = len(word)
    for i in range(0,clear):
        word.pop()
    clear = len(order)
    for i in range(0,clear):
        order.pop()
    #get dialogue
    myfile = open("STORY\\win.txt","r")
    for line in myfile:
        word.append(line)
    myfile = open("STORY\\win_order.txt","r")
    for line in myfile:
        order.append(line)
    BG1 = BACKGROUND([0,0],"CG\\win1.png")
    BG1.render()
    box.morph(wws)
    box.boxrender()
    pygame.display.flip()
    now = box.massrender(now,wws)
    #story loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP and now < len(word)-1 and voicer < len(order)-1:
                if "bgc" in order[voicer]:
                    BG1.morph("CG\\"+order[voicer][:-5]+".png")
                    BG1.render()
                    voicer+=1
                if "bgm" in order[voicer]:
                    pygame.mixer.music.load("BGM\\"+order[voicer][:-5]+".ogg")
                    pygame.mixer.music.play(5,0.8)
                    voicer+=1
                if voicer == len(order)-2:
                        return done
                box.morph("STORY\\"+order[voicer][:-1]+".png")
                box.boxrender()
                now = box.massrender(now,ww)
                voicer+=1
        pygame.display.flip()
    return done

def Lose(done = False):
    voicer = 0
    now = 1
    #dialogue reset
    clear = len(word)
    for i in range(0,clear):
        word.pop()
    clear = len(order)
    for i in range(0,clear):
        order.pop()
    #get dialogue
    myfile = open("STORY\\lose.txt","r")
    for line in myfile:
        word.append(line)
    myfile = open("STORY\\lose_order.txt","r")
    for line in myfile:
        order.append(line)
    BG1 = BACKGROUND([0,0],"CG\\win1.png")
    bgm = pygame.mixer.music.load("BGM\\end.ogg")
    pygame.mixer.music.play(5,0)
    BG1.render()
    box.morph(wws)
    box.boxrender()
    pygame.display.flip()
    now = box.massrender(now,ww)
    #story loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP and now < len(word)-1 and voicer < len(order)-1:
                if "bgc" in order[voicer]:
                    BG1.morph("CG\\"+order[voicer][:-5]+".png")
                    BG1.render()
                    voicer+=1
                if "bgm" in order[voicer]:
                    pygame.mixer.music.load("BGM\\"+order[voicer][:-5]+".ogg")
                    pygame.mixer.music.play(5,0.8)
                    voicer+=1
                if voicer == len(order)-2:
                        return done
                box.morph("STORY\\"+order[voicer][:-1]+".png")
                box.boxrender()
                now = box.massrender(now,ww)
                voicer+=1
        pygame.display.flip()
    return done
