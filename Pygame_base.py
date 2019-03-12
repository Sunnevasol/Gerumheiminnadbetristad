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

level = 0

####### MYNDIR ########
# Opnunargluggi - Mynd af jörðinni í litum
bakgrunnur1 = pygame.image.load('jord4.png')
# Borð 1 inngangur - Mynd af litríkum flokkunartunnum og eitthvað þannig
#bakgrunnurb1Intro = pygame.image.load('')
#Bakgrunnsmynd af fræðslu
#fraedslamynd = pygame.image.load('')
#Bakgrunnsmynd af upplýsingum um leik
#uppl = pygame.image.load('')
# Myndir af tunnunum 5 og random rusli
blatunna = pygame.image.load('blatunna.png')
blatunna = pygame.transform.scale(blatunna, (390, 270))
graentunna = pygame.image.load('graentunna.png')
graentunna = pygame.transform.scale(graentunna, (390, 270))
bruntunna = pygame.image.load('bruntunna.png')
bruntunna = pygame.transform.scale(bruntunna, (390, 270))
raudtunna = pygame.image.load('raudtunna.png')
raudtunna = pygame.transform.scale(raudtunna, (390, 270))
svorttunna =  pygame.image.load('svorttunna.png')
svorttunna = pygame.transform.scale(svorttunna, (390, 270))
rusl1 = pygame.image.load('epli.jpg')
rusl1 = pygame.transform.scale(rusl1, (200, 180))
rusl2 = pygame.image.load('tyggjo.png')
rusl2 = pygame.transform.scale(rusl2, (180, 180))
rusl3 = pygame.image.load('svali2.png')
rusl3 = pygame.transform.scale(rusl3, (230, 210))
rusl4 = pygame.image.load('skyr.jpg')
rusl4 = pygame.transform.scale(rusl4, (220, 190))
rusl5 = pygame.image.load('prinspolo.jpg')
rusl5 = pygame.transform.scale(rusl5, (300, 100))
rusl6 = pygame.image.load('ferna.jpg')
rusl6 = pygame.transform.scale(rusl6, (90, 210))
rusl7 = pygame.image.load('eyrnapinni.jpg')
rusl7 = pygame.transform.scale(rusl7, (200, 140))
rusl8 = pygame.image.load('banani.png')
rusl8 = pygame.transform.scale(rusl8, (290, 260))
rusl9 = pygame.image.load('Plastpoki.png')
rusl9 = pygame.transform.scale(rusl9, (150, 200))
rusl10 = pygame.image.load('dos.jpg')
rusl10 = pygame.transform.scale(rusl10, (190, 200))
ruslalisti = [rusl1,rusl2,rusl3,rusl4,rusl5,rusl6,rusl7,rusl8,rusl9,rusl10]
ruslageymsla1 = random.choice(ruslalisti[0:])
# Bakgrunnur fyrir borð 1 -
bakgrunnurb1 = pygame.image.load('pappirbak.jpg')
# Borð 2 inngangur - Mynd af ...
#bakgrunnurb2Intro = pygame.image.load('')
# Borð 2 bakgrunnur
bakgrunnurb2 = pygame.image.load('bakgrunnurbord2.jpg')
bakgrunnurb2 = pygame.transform.scale(bakgrunnurb2, (800, 600))
# Borð 3 inngangur - Mynd af ...
#bakgrunnurb3Intro = pygame.image.load('')
# Borð 3 bakgrunnur - mynd af sjó
bakgrunnurb3 = pygame.image.load('haf.jpg')
bakgrunnurb3 = pygame.transform.scale(bakgrunnurb3, (800, 600))
# Bakgrunnur þegar maður vinnur Borð 3
#bakgrunnurb3vinna = pygame.image.load('')
# Borð 3 - Mynd af háfi fyrir sjóborð
hafurmynd = pygame.image.load('hafur1.png')
hafur_breidd = 96
hafur_haed = 40
# Borð 3 - Myndir af plasti fyrir Sjóborð
plastflaska = pygame.image.load('Plastflaska.png')
plastflaska = pygame.transform.scale(plastflaska, (113, 170))
# Myndir af fiskum
fiskur1 = pygame.image.load('nemo.png')
fiskur1 = pygame.transform.scale(fiskur1, (353, 204))
fiskur2 = pygame.image.load('skjaldbaka.png')
fiskur2 = pygame.transform.scale(fiskur2, (259, 215))
fiskur3 = pygame.image.load('dora.png')
fiskur3 = pygame.transform.scale(fiskur3, (232, 193))
fiskur4 = pygame.image.load('hakarl.png')
fiskur4 = pygame.transform.scale(fiskur4, (156, 133))
fiskalisti = [fiskur1, fiskur2, fiskur3, fiskur4]
fiskageymsla = random.choice(fiskalisti[0:])
# Bakgrunnur fyrir inngang að lokaborði - ...
#bakgrunnurb4Intro = pygame.image.load('')
#Bakgrunnur fyrir vinningsborð
bakgrunnurb4 = pygame.image.load('lokabordbakgrunnur.jpg')
bakgrunnurb4 = pygame.transform.scale(bakgrunnurb4, (800, 600))
solblommynd = pygame.image.load('Sólblóm.png')
solblommynd = pygame.transform.scale(solblommynd, (100, 150))
eplatremynd = pygame.image.load('Eplatré.png')
eplatremynd = pygame.transform.scale(eplatremynd, (100, 150))

###### ANNAÐ #######
clock = pygame.time.Clock()                            # TÍMI
font = pygame.font.Font('Sansation-Regular.ttf', 30)   # LETUR

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

# BORÐ 1 - FLOKKUN
# Inngangur
def b1Inngangur():
    inngangur2 = True
    while inngangur2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb1, (0,0))
        skilabod1('Þú ert komin/n í borð 1', 15)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 5)
        skilabod2('Meiri texti hér ef við viljum', 7)
        takkar("Byrja",150,450,150,75,WHITE,GREY,'StartLevel1b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(10)

###### Borð 1 ######
def bord1():
    stig = 0
    b1 = True
    while b1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb1, (0,0))
        skilabod1('Í hvaða tunnu fer ruslið?',15)
        skjaMynd.blit(ruslageymsla1, (300,77))                      # Birta mynd af random rusli
        skjaMynd.blit(blatunna,(-90,250))
        skjaMynd.blit(bruntunna,(60,250))
        skjaMynd.blit(graentunna,(210,250))
        skjaMynd.blit(svorttunna,(360,250))
        skjaMynd.blit(raudtunna,(510,250))
        takkar("Bláu",50,500,100,75,WHITE,GREY,'blaTunna')
        takkar("Brúnu",200,500,100,75,WHITE,GREY,'brunTunna')
        takkar("Grænu",350,500,100,75,WHITE,GREY,'graenTunna')
        takkar("Svörtu",500,500,100,75,WHITE,GREY,'svortTunna')
        takkar("Rauðu",650,500,100,75,WHITE,GREY,'raudTunna')
        pygame.display.update()
        clock.tick(10)

def blaTunna():
    if ((ruslageymsla1 == rusl3) or (ruslageymsla1 == rusl6)):
        retttunna()
    else:
        vitlaustunna()
def brunTunna():
    if ((ruslageymsla1 == rusl1) or (ruslageymsla1 == rusl8)):
        retttunna()
    else:
        vitlaustunna()
def graenTunna():
    if ((ruslageymsla1 == rusl4) or (ruslageymsla1 == rusl5)):
        retttunna()
    else:
        vitlaustunna()
def svortTunna():
    if ((ruslageymsla1 == rusl2) or (ruslageymsla1 == rusl7)):
        retttunna()
    else:
        vitlaustunna()
def raudTunna():
    if ((ruslageymsla1 == rusl9) or (ruslageymsla1 == rusl10)):
        retttunna()
    else:
        vitlaustunna()

def retttunna():
    rett = True
    while rett:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb1, (0,0))
        # Hækka fræteljarann um 2
        skilabod1("Vel gert! Þú valdir rétta tunnu.",7)
        takkar("Halda áfram",350,500,180,75,WHITE,GREY,'StartLevel1b')
        pygame.display.update()
        clock.tick(10)

def vitlaustunna():
    rangt = True
    while rangt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb1, (0,0))
        # Lækka fræteljarann um 1
        skilabod1("Æjæj þetta rusl á ekki heima hér :(",7)
        takkar("Reyna aftur",350,500,180,75,WHITE,GREY,'StartLevel1b')
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
        skjaMynd.blit(bakgrunnurb1, (0,0))
        skilabod1('Þú ert komin/n í borð 2', 15)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 7)
        skilabod2('Meiri texti hér ef við viljum', 5)
        takkar("Byrja",150,450,150,75,WHITE,GREY,'StartLevel2b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(10)

###### Borð 2 ######
def bord2():
    bordtvo = True
    while bordtvo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb2, (0,0))
        skilabod1("Spurningaleikur",15)
        skilabod4("Veldu þann valmöguleika sem þér þykir réttastur",6)
        skilabod4("Hér kemur spurningin",4)
        skilabod4("'Svarmöguleiki A'",2.2)
        skilabod4("'Svarmöguleiki B'",1.55)
        skilabod4("'Svarmöguleiki C'",1.2)
        takkar("A",650,250,75,75,WHITE,GREY,'')
        takkar("B",650,350,75,75,WHITE,GREY,'')
        takkar("C",650,450,75,75,WHITE,GREY,'')
        pygame.display.update()
        clock.tick(10)

# BORÐ 3 - SJÓBORÐ
# Inngangur
def b3Inngangur():
    inngangur3 = True
    while inngangur3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnur1, (0,0))
        skilabod1('Þú ert komin/n í borð 3', 9)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 5)
        skilabod2('Meiri texti hér ef við viljum', 3)
        takkar("Byrja",150,450,150,75,WHITE,GREY,'StartLevel3b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

############### Borð 3 ###################
def bord3():
    tonlistsjor()
    #Upphafsstaður á háfi
    x = (display_breidd*0.35)
    y = (display_haed*0.6)
    x_change = 0
    #TELJARI
    counter, teljari = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('Sansation-Regular.ttf', 30)
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
    plast_haed = 60
    plast_breidd = 60
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
                    x_change = -13
                elif event.key == pygame.K_RIGHT:
                    x_change = 13
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        # Það sem kemur á skjáinn
        skjaMynd.blit(bakgrunnurb3,(0,0))
        skjaMynd.blit(font.render(teljari, True, (0, 0, 0)), (30, 40))
        fiskur(fiskur_byrjax, fiskur_byrjay, fiskur_breidd, fiskur_haed)        # Birta mynd af fiski
        fiskur_byrjay += fiskur_hradi
        plast(plast_byrjax, plast_byrjay)                                       # Birta mynd af plasti
        plast_byrjay += plast_hradi
        hafurfall(x,y)                                                          # Birta mynd af háfi
        #Hreyfingin á fiskum
        if (fiskur_byrjay > display_haed):
            fiskur_byrjay = 0 - fiskur_haed
            fiskur_byrjax = random.randrange(0,display_breidd)
        #Hreyfing á plasti
        if (plast_byrjay > display_haed):
            plast_byrjay = 0 - plast_haed
            plast_byrjax = random.randrange(0,display_breidd)
        #Þegar Háfurinn nær óvart fiski
        if (y < fiskur_byrjay + fiskur_haed):
            if ((x > fiskur_byrjax and x < fiskur_byrjax + fiskur_breidd) or (x + hafur_breidd > fiskur_byrjax and x + hafur_breidd < fiskur_byrjax + fiskur_breidd)):
                skilabod1("Æjæj þú átt að veiða plastið",5)
                #Hér eiga fræstigin að minnka...

        # Þegar háfurinn nær plasti
        if (y < plast_byrjay + plast_haed):
            if ((x > plast_byrjax and x < plast_byrjax + plast_breidd) or (x + plast_breidd > plast_byrjax and x + hafur_breidd < plast_byrjax + plast_breidd)):
                skilabod1("Flott!",5)
                # Hér eiga fræstigin að hækka...

        pygame.display.update()
        clock.tick(20)

###### Vinna borð 3 #######
def vinnurbord3():
    vinnab3 = True
    while vinnab3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnur1, (0,0))
        skilabod2('Til hamingju!',9)
        skilabod2('þú kláraðir borð 3',5.5)
        pygame.display.update()
        pygame.time.wait(50)
        #lokaBordInngangur()
"""
########## LOKABORÐ ############
def lokaBordInngangur():
    inngangur4 = True
    while inngangur4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb4, (0,0))
        skilabod1('Til hamingju þú ert komin/n á leiðarenda', 9)
        skilabod2('Nú getur þú ...', 7)
        skilabod2('Meiri texti hér ef við viljum', 5)
        takkar("Halda áfram",150,450,150,75,WHITE,GREY,'StartLevel4')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
"""
# Borð 4
def bord4():
    bordfjogur = True
    while bordfjogur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb4, (0,0))
        skilabod1('Texti hér...', 15)
        skilabod3('Texti hér líka', 7)
        takkar("Eplatré",150,200,120,52,WHITE,GREY,'eplatre')
        takkar("Sólblóm",550,200,120,52,WHITE,GREY,'solblom')
        pygame.display.update()
        clock.tick(30)

def eplaTre():
    x = random.randrange(-200,500)
    y = random.randrange(350,500)
    skjaMynd.blit(eplatremynd,(x,y))

def solBlom():
    x = random.randrange(-200,500)
    y = random.randrange(350,500)
    skjaMynd.blit(solblommynd,(x,y))

####### ANNAÐ #########
def fiskur(fiskurx, fiskury,fiskurbreidd,fiskurhaed):
    skjaMynd.blit(fiskageymsla,(fiskurx,fiskury,fiskurbreidd,fiskurhaed))

def plast(plastx,plasty):
    skjaMynd.blit(plastflaska,(plastx,plasty))

def hafurfall(x,y):
    skjaMynd.blit(hafurmynd,(x,y))

def fraestig(stig):
    fraestigTexti = font.render("Stig: " + str(stig), True, BLACK)
    skjaMynd.blit(fraestigTexti,[0,0])

###### Tónlist ########
def tonlist():
    pygame.mixer.music.load('')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

def tonlistsjor():
    pygame.mixer.music.load('undersea.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

#Hljóð sem kemur ef maður svarar rétt
def rett():
    pygame.mixer.music.load('')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

#Hljóðið sem kemur ef maður svarar vitlaust
def vitlaust():
    pygame.mixer.music.load('')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

########  Skilaboð - texti #########
def skilabod1(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 50)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod2(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Regular.ttf', 35)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod3(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Light.ttf', 25)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod4(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 30)
    textSurf, textRect = textObjectsWhite(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)
# Litir á texta
def textObjectsBlack(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def textObjectsWhite(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def textObjectsRed(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

######### TAKKAR ##########
def takkar(text,x,y,breidd,haed,litur1,litur2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #gera kassa gráa ef músin fer yfir kassana
    if x + breidd > mouse[0] > x and y + haed > mouse[1] > y:
        pygame.draw.rect(skjaMynd, litur2,(x,y,breidd,haed))
        if click[0] == 1 and action !=None:
            if action == "StartLevel1":
                b1Inngangur()
            elif action == "Upplýsingar":
                uppl()
            elif action == "Fræðsla":
                fraedsla()
            elif action == "opnunargluggi":
                opnunarGluggi()
            elif action == "quit":
                pygame.quit()
            elif action == "blaTunna":
                blaTunna()
            elif action == "brunTunna":
                brunTunna()
            elif action == "graenTunna":
                graenTunna()
            elif action == "svortTunna":
                svortTunna()
            elif action == "raudTunna":
                raudTunna()
            elif action == "StartLevel1b":
                bord1()
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
            elif action == "eplatre":
                eplaTre()
            elif action == "solblom":
                solBlom()

    else:
        pygame.draw.rect(skjaMynd, litur1,(x,y,breidd,haed))

    takkar = pygame.font.Font('Sansation-Bold.ttf', 29)
    textSurf, textRect = textObjectsBlack(text, takkar)
    textRect.center = ((x+(breidd/2)),(y+(haed/2)))
    skjaMynd.blit(textSurf, textRect)

def main():
    done = False
    state_tune = 1
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if level == 0:
            if state_tune != 0:
                state_tune = 0
            bord4()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

if __name__=='__main__':
    main()
else:
    print('No just imported by another class')
