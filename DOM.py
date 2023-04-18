import pygame
import sys
import random
pygame.init()
#värvid
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
pink=[255,153,255]
lGreen=[153,255,153]
#ekraani seaded
pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Majake")
pind.fill(lGreen)

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]
#funktsioonid
def Maja(x,y,width,height,screen,color):
    points=[(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0)* height),(x,y- ((3/4.0) * height)), (x+width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen,color,False,points,suurus)

def Uks(x,y,laius,kõrgus,screen,color):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen,color,False,punktid,suurus)

def Aken(x,y,laius,kõrgus,screen,color):
    punktid=[(x,y-(1/2)*kõrgus),(x,y),(x,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen,color,False,punktid,suurus)
#kutsun funktsiooni välja
Maja(100,400,500,400,pind,majavarv)
Uks(100,400,500,400,pind,majavarv)
pygame.display.flip()