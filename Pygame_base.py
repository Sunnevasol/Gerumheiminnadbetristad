
import pygame
import time
import random
#from PIL import image

######## LITIR #########
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220,220,220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

######## SKJÁR #########
display_breidd = 800
display_haed = 600
gameDisplay = pygame.display.set_mode((display_breidd,display_haed))
pygame.display.set_caption('Gerum heiminn að betri stað')

####### MYNDIR ########
# Hér koma þær myndir sem við þurfum
# Mynd af jörðinni í litum
bakgrunnur1 = pygame.image.load('jord.png')
# Mynd af litríkum flokkunartunnum
#bakgrunnurb1Intro = pygame.image.load('....png')
# Myndir af tunnunum 5 og random rusli
#bakgrunnurb1 = pygame.image.load('....png')

#bakgrunnurb2Intro = pygame.image.load('....png')
#bakgrunnurb2 = pygame.image.load('....png')
#bakgrunnurb3Intro = pygame.image.load('....png')
#bakgrunnurb3 = pygame.image.load('....png')
#bakgrunnurb4Intro = pygame.image.load('....png')
#bakgrunnurb4 = pygame.image.load('....png')
# Mynd af háfi fyrir sjóborð
hafur = pygame.image.load('hafur.jpg')
# Mynd af plasti fyrir Sjóborð


# Loop until the user clicks the close button.
done = False

###### ANNAÐ #######
# TÍMI
clock = pygame.time.Clock()
# LETUR
font = pygame.font.Font('Raleway.ttf', 30)

###### BORÐIN ######
# INNGANGUR
def opnunarGluggi():
    inngangur1 = True
    while inngangur1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnur1, (0,0))
        messageDisplayIntro('Gerum heiminn að betri stað')
        takkar("Hefja Leik",50,450,150,75,BLACK,GREY,'StartLevel1')
        takkar("Fræðsla",250,450,150,75,BLACK,GREY,'Fræðsla')
        takkar("Upplýsingar um leik",450,450,150,75,BLACK,GREY,'Upplýsingar')
        pygame.display.update()
        clock.tick(60)

#fræðsla um umhverfisvitund...
def fraedsla():
    pass
#Upplýsingar um leikinn og útgáfu leiks
def uppl():
    pass


# BORÐ 1 - FLOKKUN
# Inngangur
def b1Inngangur():
    inngangur2 = True
    while inngangur2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurb1Intro, (0,0))
        messageDisplayIntro('Þú ert komin/n í borð 1', 9)
        messageDisplayIntro('Ýttu á "Byrja!" til að hefja leik', 7)
        messageDisplayIntro('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel1b')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

# Borð 1
def bord1():
    pass


# BORÐ 2 - SPURNINGAR
# Inngangur
def b2Inngangur():
    inngangur3 = True
    while inngangur3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurb2Intro, (0,0))
        messageDisplayIntro('Þú ert komin/n í borð 2', 9)
        messageDisplayIntro('Ýttu á "Byrja!" til að hefja leik', 7)
        messageDisplayIntro('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel2b')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

# Borð 2
def bord2():
    pass
"""
    bordtvo = True
    while bordtvo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
"""
# BORÐ 3 - SJÓBORÐ
# Inngangur
def b3Inngangur():
    inngangur3 = True
    while inngangur3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurb3Intro, (0,0))
        messageDisplayIntro('Þú ert komin/n í borð 3', 9)
        messageDisplayIntro('Ýttu á "Byrja!" til að hefja leik', 7)
        messageDisplayIntro('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel3')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

# Borð 3
def bord3():
    pass
"""
    bordthrju = True
    while bordthrju:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
"""
# LOKABORÐ
# Inngangur
def lokaBordInngangur():
    inngangur4 = True
    while inngangur4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurb4Intro, (0,0))
        messageDisplayIntro('Til hamingju þú ert komin/n á leiðarenda', 9)
        messageDisplayIntro('Nú getur þú ...', 7)
        messageDisplayIntro('Meiri texti hér ef við viljum', 5)
        takkar("Halda áfram",150,450,150,75,BLACK,GREY,'StartLevel4')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')

# Borð 4
def bord4():
    bordfjogur = True
    while bordfjogur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



####### ANNAÐ #########
#Tónlist í bakgrunni
def tonlist():
    pass

#Hljóð sem kemur ef maður svarar rétt
def rett():
    pass

#Hljóðið sem kemur ef maður svarar vitlaust
def vitlaust():
    pass

######### TAKKAR ##########
def takkar(text,x,y,breidd,haed,litur1,litur2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #gera kassa gráa ef músin fer yfir kassana
    if x + breidd > mouse[0] > x and y + haed > mouse[1] > y:
        pygame.draw.rect(gameDisplay, litur2,(x,y,breidd,haed))
        if click[0] == 1 and action !=None:
            if action == "StartLevel1":
                b1Inngangur()
            elif action == "Fræðsla":
                fraedsla()
            elif action == "Upplýsingar":
                uppl()
            elif action == "StartLevel1b":
                bord1()
            elif action == "quit":
                pygame.quit()
            elif action == "StartLevel2":
                b2Inngangur()
            elif action == "StartLevel2b":
                bord2()
            elif action == "StartLevel3":
                b3Inngangur()
            elif action == "StartLevel3b":
                bord3()
            elif action == "StartLevel4":
                lokaBordInngangur()
            elif action == "StartLevel4b":
                bord4()

    else:
        pygame.draw.rect(gameDisplay, litur1,(x,y,breidd,haed))

    takkar = pygame.font.Font('Raleway.ttf', 30)
    textSurf, textRect = textObjectsBlack(text, takkar)
    textRect.center = ((x+(breidd/2)),(y+(haed/2)))
    gameDisplay.blit(textSurf, textRect)
