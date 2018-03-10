from Core import *

def gameon(gamemode = 0):
    # important prep
    live = 3
    speed = 4
    bulletcount = 0
    done = False
    clock = pygame.time.Clock()
    #pygame.mixer.music.load("china.ogg")
    #pygame.mixer.music.play(50,1)
    ticker = 0
    heart = []
    heart.append(SPRITE(0,567,"heart1.png"))
    heart.append(SPRITE(35,567,"heart1.png"))
    heart.append(SPRITE(70,567,"heart1.png"))
    core = SPRITE(400,550,"CORE")
    boss = SPRITE(400,50,"blackwing.png")
    player = SPRITE(400,550,"whitewing.png")
    bg = BACKGROUND([0,0],"city.gif")
    phone = []
    for i in range(0,10):
        phone.append(BULLET())
        phone[i].randprop()
    shake1 = -1
    shake2 = -1
    
    #player moving
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                speed = 2#slow movement
            if event.type == pygame.QUIT:
                done = True
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
        player.x = player.x + player.xspeed
        player.y = player.y + player.yspeed
    #renderer
        core.x = player.x+24
        core.y = player.y+28
        screen.fill([255,255,255])
        screen.blit(bg.image,bg.rect)
        player.render()
        boss.render()
        core.render()
        heart[0].render()
        heart[1].render()
        heart[2].render()
        for i in range(0,10+(bulletcount//20)):
            phone[i].falldown()
            if phone[i].y >= 600:
                phone[i].randprop()
                phone[i].y = 0
                bulletcount+=1
            phone[i].render()
        phone[0].falldown()
        phone[0].render()
        pygame.display.flip()
        clock.tick(60)
        ticker = pygame.time.get_ticks()
        print(bulletcount)
        if(ticker % 100 == 0):
            boss.shake(5*shake1)
            shake1 *= shake2
        if bulletcount%20 == 0:
            phone.append(BULLET())
        if gamemode == 0 and bulletcount >= 1000:
            break
    pygame.quit()
    
gameon()
