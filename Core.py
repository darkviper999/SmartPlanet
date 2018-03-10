import pygame
import sys,os
import random
clock = pygame.time.Clock()
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Smart Planet")
pygame.display.set_icon(pygame.image.load("Menu\\icon.png"))
random.seed()
pygame.mixer.init()
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
myfont = pygame.font.SysFont("monospace",20,True)
word = []
order = []


def DetectCollision(x1,y1,w1,h1,x2,y2,w2,h2):
        #Check sprite overlap
        if (x2+w2 >= x1 >= x2 and y2+h2 >= y1 >= y2):
            return True
        elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1 >= y2):
            return True
        elif (x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2):
            return True
        elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2):
            return True
        else:
            return False

class DIALOGUE:
        def __init__(self,fname):
                self.image = pygame.image.load(fname)
                self.rect = self.image.get_rect()
                self.rect.left,self.rect.top = 0,450
                self.fname = fname
        def boxrender(self):
                screen.blit(self.image,self.rect)
        def massrender(self,now,fname = "STORY\\ww.png",shifty = 10):
                #recursion to display multiple line words
                toprint = word[now][:-1]
                label = myfont.render(toprint, 1, (255,255,255))
                if word[now] != '\n':
                        screen.blit(label,(self.rect.left+180,self.rect.top+shifty))
                if now+1 < len(word):
                        if word[now+1] != '\n':
                                now = self.massrender(now+1,fname,shifty+20)
                                if(now == len(word)-1):
                                        return now
                        else:
                                return now+1
                return now
        def morph(self,fname):
                self.image = pygame.image.load(fname)
                self.fname = fname
                
class BACKGROUND:
        def __init__(self,location,fname):
                self.imagename = fname
                self.image = pygame.image.load(fname)
                self.rect = self.image.get_rect()
                self.rect.left,self.rect.top = location
                self.yspeed = 15
        def morph(self,name):
                self.image = pygame.image.load(name)
                self.imagename = name
        def render(self):
                screen.blit(self.image,self.rect)
        def falldown(self):
                self.rect.top += self.yspeed
class CIRCLE():
        def __init__(self):
                self.x = 400
                self.y = 550
                self.image = pygame.Surface((10,10))
                self.image = pygame.image.load("SPRITE\\core.png")
        def render(self):
                screen.blit(self.image,(self.x,self.y))
        def morph(self,name):
                self.image = pygame.image.load(name)
                self.imagename = name
class SPRITE():
        def __init__(self,x,y,name):
                self.x = x
                self.y = y
                self.width = 50
                self.height = 50
                self.xspeed = 0
                self.yspeed = 0
                self.image = pygame.image.load(name)
        def morph(self,name):
                self.image = pygame.image.load(name)
        def render(self):
                screen.blit(self.image,(self.x,self.y))
        def move(self):
                self.x += self.xspeed
        def setspeed(self,speed):
                self.xspeed = speed
class BULLET():
    def __init__(self,image = "SPRITE\\smartphone.png"):
        self.x = random.randrange(10,790)
        self.y = 0
        self.yspeed = random.randrange(1,8)
        self.ishit = 0
        self.image = pygame.image.load(image)
    def blastspeed(self):
        self.yspeed = -8
    def randprop(self):
        self.x = random.randrange(10,790)
        self.yspeed = random.randrange(1,10)
    def falldown(self):
        self.y += self.yspeed
    def render(self):
        screen.blit(self.image,(self.x,self.y))
    def is_hitted(self,wx,wy):
        if DetectCollision(wx,wy,10,10,self.x,self.y,20,35) and self.ishit == 0:
                self.ishit = 1
                return True
    def Transparent(self):
        self.image = pygame.image.load("void.png")
                
