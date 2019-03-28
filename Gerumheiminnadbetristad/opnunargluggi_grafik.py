import pygame
import time
import random

pygame.init()

######## LITIR #########
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220,220,220)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

######## SKJÁR #########
display_breidd = 800
display_haed = 600
size = (display_breidd,display_haed)
skjaMynd = pygame.display.set_mode(size)
pygame.display.set_caption('Gerum heiminn að betri stað')

####### MYNDIR ########
# Opnunargluggi - Mynd af jörðinni í litum
bakgrunnur1 = pygame.image.load('jord4.png')
# Borð 1 inngangur - Mynd af litríkum flokkunartunnum og eitthvað þannig
#bakgrunnurb1Intro = pygame.image.load('')
#Bakgrunnsmynd af fræðslu
#fraedslamynd = pygame.image.load('')
#Bakgrunnsmynd af upplýsingum um leik
#uppl = pygame.image.load('')
class Inngangur:
    def __



    def opnunarGluggi():
        inngangur1 = True
        while inngangur1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            skjaMynd.blit(bakgrunnur1, (0,0))
            skilabod1('Gerum heiminn að betri stað',14)
            takkar("Hefja Leik",50,480,150,75,WHITE,GREY,'StartLevel1')
            takkar("Fræðsla",600,480,150,75,WHITE,GREY,'Fræðsla')
            takkar("Upplýsingar um leik",250,480,300,75,WHITE,GREY,'Upplýsingar')
            pygame.display.update()
            clock.tick(10)

    #fræðsla um umhverfisvitund...
    def fraedsla():
        fraedsla = True
        while fraedsla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            skjaMynd.blit(bakgrunnurb1, (0,0))
            skilabod1('Fræðsla',15)
            skilabod3('Fræðsla hér...',7)
            skilabod3('Lína 2',5.6)
            skilabod3('Lína 3',4.6)
            skilabod3('Lína 4',3.9)
            skilabod3('Lína 5',3.35)
            takkar("Til baka",320,450,150,75,WHITE,GREY,'opnunargluggi')
            pygame.display.update()
            clock.tick(10)

    #Upplýsingar um leikinn og útgáfu leiks
    def uppl():
        upplysingar = True
        while upplysingar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            skjaMynd.blit(bakgrunnurb1, (0,0))
            skilabod1('Upplýsingar', 15)
            skilabod2('Útgáfa 1.1', 6)
            skilabod2('Höfundar: ', 3)
            skilabod3('Sigríður Júlía Heimisdóttir', 2.55)
            skilabod3('Sunneva Sól Ívarsdóttir', 2.25)
            skilabod3('Þórdís Rögn Jónsdóttir', 2.02)
            skilabod3('Þórdís Tryggvadóttir', 1.83)
            takkar("Til baka",320,450,150,75,WHITE,GREY,'opnunargluggi')
            pygame.display.update()
            clock.tick(10)
