import pygame
import time
import random

pygame.init()

######## LITIR #########
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220,220,220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

######## SKJÁR #########
display_breidd = 800
display_haed = 600
gameDisplay = pygame.display.set_mode((display_breidd,display_haed))
pygame.display.set_caption('Gerum heiminn að betri stað')

####### MYNDIR ########
# Opnunargluggi - Mynd af jörðinni í litum
bakgrunnur1 = pygame.image.load('Bakgrunnuropnun.png')
# Borð 1 inngangur - Mynd af litríkum flokkunartunnum og eitthvað þannig
bakgrunnurb1Intro = pygame.image.load('')
# Myndir af tunnunum 5 og random rusli
blatunna = pygame.image.load('')
graentunna = pygame.image.load('')
bruntunna = pygame.image.load('')
raudtunna = pygame.image.load('')
svorttunna =  pygame.image.load('')
# Bakgrunnur fyrir borð 1 -
bakgrunnurb1 = pygame.image.load('')
# Borð 2 inngangur - Mynd af ...
bakgrunnurb2Intro = pygame.image.load('')
# Borð 2 bakgrunnur - Mynd af ...
bakgrunnurb2 = pygame.image.load('')
# Borð 3 inngangur - Mynd af ...
bakgrunnurb3Intro = pygame.image.load('')
# Borð 3 bakgrunnur - ...
bakgrunnurb3 = pygame.image.load('')
# Bakgrunnur þegar maður vinnur Borð 3
bakgrunnurb3vinna = pygame.image.load('')
# Borð 3 - Mynd af háfi fyrir sjóborð
hafur = pygame.image.load('hafur.jpg')
hafur_breidd = 96
hafur_haed = 40
# Borð 3 - Myndir af plasti fyrir Sjóborð
plastflaska = pygame.image.load('Plastflaska.jpg')
plastpoki = pygame.image.load('Plastpoki.jpg')
fiskur = pygame.image.load('')
# Bakgrunnur fyrir inngang að lokaborði - ...
bakgrunnurb4Intro = pygame.image.load('')
#Bakgrunnur fyrir vinningsborð
bakgrunnurb4 = pygame.image.load('')


###### ANNAÐ #######
clock = pygame.time.Clock()                  # TÍMI
font = pygame.font.Font('Raleway.ttf', 30)   # LETUR

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
        skilabod1('Gerum heiminn að betri stað')
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
        skilabod2('Þú ert komin/n í borð 1', 9)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 7)
        skilabod2('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel1b')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

###### Borð 1 ######
def bord1():
    pass
    b1 = True
    while b1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurb1, (0,0))
        skilabod2('Í hvaða tunnu fer ruslið?',9)
        gameDisplay.blit(blatunna,(10,80))
        gameDisplay.blit(bruntunna,(90,80))
        gameDisplay.blit(graentunna,(170,80))
        gameDisplay.blit(svorttunna,(150,80))
        gameDisplay.blit(raudtunna,(230,80))
        takkar("",150,450,165,75,white,grey,'')
        takkar("",550,450,165,75,white,grey,'')
        pygame.display.update()
        clock.tick(10)

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
        skilabod2('Þú ert komin/n í borð 2', 9)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 7)
        skilabod2('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel2b')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

###### Borð 2 ######
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
        skilabod1('Þú ert komin/n í borð 3', 9)
        skilabod1('Ýttu á "Byrja!" til að hefja leik', 7)
        skilabod1('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,BLACK,GREY,'StartLevel3')
        takkar("Hætta",550,450,150,75,BLACK,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

####### Borð 3 #######
def bord3():
    pass
    #Upphafsstaður á háfi
    x = (display_breidd*0.45)
    y = (display_haed*0.7)
    x_change = 0
    #TELJARI
    counter, teljari = 20, '20'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('Raleway.ttf', 30)
    #Stærð og hreyfing á fiskum
    fiskur_byrjax = random.randrange(0,display_breidd)
    fiskur_byrjay = -600
    fiskur_hradi = random.randrange(10,14)
    fiskur_haed = 64
    fiskur_breidd = 72
    #Stærð og hreyfing á plasti
    plast_byrjax = random.randrange(0,display_breidd)
    plast_byrjay = -600
    plast_hradi = random.randrange(10,14)
    plast_haed = 64
    plast_breidd = 72
    #LYKKJAN
    bord3 = False
    while not bord3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                counter -=1
                teljari = str(counter).rjust(4) if counter > 0 else vinnurbord3()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -4
                elif event.key == pygame.K_RIGHT:
                    x_change = 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        # Það sem kemur á skjáinn
        gameDisplay.blit(bakgrunnurb2d,(0,0))
        gameDisplay.blit(font.render(teljari, True, (0, 0, 0)), (30, 40))
        fiskur(fiskur_byrjax, fiskur_byrjay, fiskur_breidd, fiskur_haed)
        fiskur_byrjay += fiskur_hradi
        plast(plast_byrjax, plast_byrjay, plast_breidd, plast_haed)
        plast_byrjay += plast_hradi
        hafur(x,y)
        #Hreyfingin á fiskum
        if fiskur_byrjay > display_haed:
            fiskur_byrjay = 0 - fiskur_haed
            fiskur_byrjax = random.randrange(0,display_breidd)
        #Hreyfing á plasti
        if plast_byrjay > display_haed:
            plast_byrjay = 0 - plast_haed
            plast_byrjax = random.randrange(0,display_breidd)
        #Þegar Háfurinn nær óvart fiski
        if y < fiskur_byrjay + fiskur_haed:
            if x > fiskur_byrjax and x < fiskur_byrjax + fiskur_breidd or x + hafur_breidd > fiskur_byrjax and x + hafur_breidd < fiskur_byrjax + fiskur_breidd:
                # Hér eiga fræstigin að minnka...
                pass
        # Þegar háfurinn nær plasti
        if y < plast_byrjay + plast_haed:
            if x > plast_byrjax and x < plast_byrjax + plast_breidd or x + plast_breidd > plast_byrjax and x + hafur_breidd < plast_byrjax + plast_breidd:
                # Hér eiga fræstigin að hækka...
                pass

        pygame.display.update()
        clock.tick(60)



def vinnurbord3():
    vinnab3 = True
    while vinnab3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurb3vinna, (0,0))
        skilabod2('Til hamingju!',9)
        skilabod2('þú kláraðir borð 3',5.5)
        pygame.display.update()
        #ATH er hægt að nota ehv annað????
        pygame.time.wait(5000)
        lokaBordInngangur()

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
        skilabod1('Til hamingju þú ert komin/n á leiðarenda', 9)
        skilabod1('Nú getur þú ...', 7)
        skilabod1('Meiri texti hér ef við viljum', 5)
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
def fiskur(fiskurx, fiskury,fiskurbreidd,fiskurhaed):
    gameDisplay.blit(fiskur,(fiskurx,fiskury,fiskurbreidd,fiskurhaed))

def plast(plasx,plasty,plastbreidd,plasthaed):
    gameDisplay.blit(plastflaska,(plastx,plasty,plastbreidd,plasthaed))

def hafur(x,y):
    gameDisplay.blit(hafur,(x,y))

def fraestig(stig):
    fraestigTexti = font.render("Stig: "+str(stig), True, black)
    gameDisplay.blit(fraestigTexti,[0,0])

#Tónlist í bakgrunni
def tonlist():
    pass

#Hljóð sem kemur ef maður svarar rétt
def rett():
    pass

#Hljóðið sem kemur ef maður svarar vitlaust
def vitlaust():
    pass

# Skilaboð - texti
def skilabod1(texti):
    inngangstexti = pygame.font.Font('Raleway.ttf', 70)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/2))
    gameDisplay.blit(textSurf, textRect)

def skilabod2(texti,lina):
    inngangstexti = pygame.font.Font('Raleway.ttf', 35)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    gameDisplay.blit(textSurf, textRect)

# Litir á texta
def textObjectsBlack(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def textObjectsWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textObjectsRed(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

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

