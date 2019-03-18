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
stig = 0
teljari = 0
i = 0

####### MYNDIR ########
# Opnunargluggi - Mynd af jörðinni í litum
bakgrunnur1 = pygame.image.load('jord4.png')
# Borð - inngangsmynd
bakgrunnurIntro = pygame.image.load('bakgrunnurintro.jpg')
bakgrunnurIntro = pygame.transform.scale(bakgrunnurIntro, (800, 600))
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
rusl1 = pygame.image.load('epli2.png')
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
rusl_breyta = True
# Bakgrunnur fyrir borð 1 -
bakgrunnurb1 = pygame.image.load('pappirbak.jpg')
# Borð 2 bakgrunnur
bakgrunnurb2 = pygame.image.load('kritartafla.jpg')
bakgrunnurb2 = pygame.transform.scale(bakgrunnurb2, (800, 600))
# Borð 3 bakgrunnur - mynd af sjó
bakgrunnurb3 = pygame.image.load('haf.jpg')
bakgrunnurb3 = pygame.transform.scale(bakgrunnurb3, (800, 600))
# Borð 3 - Mynd af háfi fyrir sjóborð
hafurmynd = pygame.image.load('hafur1.png')
hafurmynd = pygame.transform.scale(hafurmynd, (200, 200))
hafur_breidd = 86
hafur_haed = 40
# Borð 3 - Myndir af plasti fyrir Sjóborð
plastflaska = pygame.image.load('Plastflaska.png')
plastflaska = pygame.transform.scale(plastflaska, (113, 170))
# Myndir af fiskum
fiskur1 = pygame.image.load('nemo.png')
fiskur1 = pygame.transform.scale(fiskur1, (203, 94))
fiskur2 = pygame.image.load('skjaldbaka.png')
fiskur2 = pygame.transform.scale(fiskur2, (209, 165))
fiskur3 = pygame.image.load('dora.png')
fiskur3 = pygame.transform.scale(fiskur3, (202, 163))
fiskur4 = pygame.image.load('hakarl.png')
fiskur4 = pygame.transform.scale(fiskur4, (156, 133))
fiskalisti = [fiskur1, fiskur2, fiskur3, fiskur4]
fiskageymsla = random.choice(fiskalisti[0:])
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
    tonlist()
    inngangur1 = True
    while inngangur1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnur1, (0,0))
        skilabod1('Gerum heiminn að betri stað',10)
        takkar("Hefja Leik",50,480,150,75,WHITE,GREY,'StartLevel1')
        takkar("Fræðsla",600,480,150,75,WHITE,GREY,'Fræðsla')
        takkar("Upplýsingar um leik",250,480,300,75,WHITE,GREY,'Upplýsingar')
        pygame.display.update()
        clock.tick(10)

#fræðsla um umhverfisvitund...
def fraedsla():
    tonlist()
    fraedsla = True
    while fraedsla:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Fræðsla',5.0)
        skilabod3c('Við eigum aðeins eina Jörð og þess vegna er mikilvægt að',3.5)
        skilabod3c('hver og einn geri sér grein fyrir að umgengni okkar skiptir máli. ',2.85)
        skilabod3c('Ef við flokkum ekki ruslið okkar, mengum og göngum illa um ',2.35)
        skilabod3c('náttúruna, þá mun Jörðin á endanum gefast upp á okkur. Þá ',2.0)
        skilabod3c('erum við í vondum málum því hvar ætlum við að fá nýja Jörð?',1.75)
        skilabod3d('Þetta er í okkar höndum og því er mikilvægt að allir leggist á eitt!',1.55)
        takkar("Til baka",320,450,150,75,WHITE,GREY,'opnunargluggi')
        pygame.display.update()
        clock.tick(10)

#Upplýsingar um leikinn og útgáfu leiks
def uppl():
    tonlist()
    upplysingar = True
    while upplysingar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Upplýsingar', 5)
        skilabod2('Útgáfa 1.1', 3.0)
        skilabod2('Höfundar: ', 2.35)
        skilabod3('Sigríður Júlía Heimisdóttir', 2.05)
        skilabod3('Sunneva Sól Ívarsdóttir', 1.85)
        skilabod3('Þórdís Rögn Jónsdóttir', 1.67)
        skilabod3('Þórdís Tryggvadóttir', 1.53)
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
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Þú ert komin/nn í borð 1', 2.6)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 2.1)
        skilabod2('Meiri texti hér ef við viljum', 1.8)
        takkar("Byrja",150,400,150,75,WHITE,GREY,'StartLevel1b')
        takkar("Hætta",550,400,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(10)

###### Borð 1 ######
def bord1():
    pygame.mixer.music.pause()
    global stig
    global teljari
    b1 = True
    global rusl_breyta
    while teljari < 4:
        while b1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            skjaMynd.blit(bakgrunnurIntro, (0,0))
            skilabod1('Í hvaða tunnu fer ruslið?',15)
            if rusl_breyta == False:
                randomrusl()
            else:
                skjaMynd.blit(ruslageymsla1,(317,100))                  # Birta mynd af random rusli
            fraestig(stig)
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
    bord1vinna()

def randomrusl():
    global rusl_breyta
    global ruslageymsla1
    ruslalisti = [rusl1,rusl2,rusl3,rusl4,rusl5,rusl6,rusl7,rusl8,rusl9,rusl10]
    ruslageymsla1 = random.choice(ruslalisti[0:])
    skjaMynd.blit(ruslageymsla1, (377,100))
    rusl_breyta = True

def blaTunna():
    global ruslageymsla1
    if ((ruslageymsla1 == rusl3) or (ruslageymsla1 == rusl6)):
        retttunna()
    else:
        vitlaustunna()
def brunTunna():
    global ruslageymsla1
    if ((ruslageymsla1 == rusl1) or (ruslageymsla1 == rusl8)):
        retttunna()
    else:
        vitlaustunna()
def graenTunna():
    global ruslageymsla1
    if ((ruslageymsla1 == rusl4) or (ruslageymsla1 == rusl5)):
        retttunna()
    else:
        vitlaustunna()
def svortTunna():
    global ruslageymsla1
    if ((ruslageymsla1 == rusl2) or (ruslageymsla1 == rusl7)):
        retttunna()
    else:
        vitlaustunna()
def raudTunna():
    global ruslageymsla1
    if ((ruslageymsla1 == rusl9) or (ruslageymsla1 == rusl10)):
        retttunna()
    else:
        vitlaustunna()

def retttunna():
    ruslahljod()
    rett = True
    global rusl_breyta
    global stig
    stig += 2
    global teljari
    teljari += 1
    while rett:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        rusl_breyta = False
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        fraestig(stig)
        skilabod1("Vel gert! Þú valdir rétta tunnu.",3)
        takkar("Halda áfram",310,300,180,75,WHITE,GREY,'StartLevel1b')
        pygame.display.update()
        clock.tick(10)

def vitlaustunna():
    ruslahljod()
    rangt = True
    global rusl_breyta
    global stig
    stig -= 1
    global teljari
    teljari += 1
    while rangt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        rusl_breyta = False
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        fraestig(stig)
        skilabod1("Æjæj þetta rusl á ekki heima hér :(",3)
        takkar("Reyna aftur",310,300,180,75,WHITE,GREY,'StartLevel1b')
        pygame.display.update()
        clock.tick(10)

def bord1vinna():
    tonlist()
    vinnab1 = True
    while vinnab1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro,(0,0))
        fraestig(stig)
        skilabod1('Til hamingju!',3)
        skilabod1('þú kláraðir borð 1',2)
        takkar("Halda áfram",310,450,190,75,WHITE,GREY,'StartLevel2')
        pygame.display.update()
        pygame.time.wait(10)

# Spurningalisti
spurning1 = "Hvernig ætlar þú í skólann í dag?"
spurning2 = "Þegar ég er búin með mjólkina þá:"
spurning3 = "Þegar fötin mín passa ekki lengur þá:"
spurning4 = "Þegar ég tannbursta mig þá:"
spurning5 = "Þegar ég klára ekki kvöldmatinn minn þá:"
spurning6 = "Þegar ég fer í búðina þá:"
spurningalisti = [spurning1, spurning2, spurning3, spurning4, spurning5, spurning6]
#Svarmöguleikalisti
valAlisti = ["Strætó", "Hendi ég fernunni í ruslið", "Fer ég með þau í Rauða krossinn",
    "Læt ég vatnið renna allann tímann", "Hendi ég honum í svörtu tunnuna",
    "Tek ég með mér taujpoka"]
valBlisti = ["Hjóli", "Skola, læt þorna og hendi í pappatunnuna",
    "Hendi ég þeim í ruslið", "Skrúfa frá rétt á meðan ég bleyti burstann",
    "Set afganginn í box og inn í ísskáp", "Kaupi þrjá plastpoka í búðinni"]
valClisti = ["Fæ far hjá ömmu", "Læt hana inn í ísskáp og mamma gengur frá",
    "Gef litla frænda/frænku þau", "Ég tannbursta mig ekki",
    "Hendi ég honum í brúnu moltutunnuna", "Kaupi maíspoka"]

# BORÐ 2 - SPURNINGAR
# Inngangur
def b2Inngangur():
    tonlist()
    inngangur3 = True
    while inngangur3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        fraestig(stig)
        skilabod1('Þú ert komin/nn í borð 2', 2.6)
        skilabod2('Nú reynir á gáfurnar, gangi þér vel! :)', 2.1)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 1.8)
        takkar("Byrja",150,450,150,75,WHITE,GREY,'StartLevel2b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(10)

###### Borð 2 ######
def bord2():
    tonlist()
    global stig
    global i
    while i < 6:
        bordtvo = True
        while bordtvo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            skjaMynd.blit(bakgrunnurb2,(0,0))
            skilabod1b("Spurningaleikur",11)
            skilabod3b("Veldu þann valmöguleika",5.75)
            skilabod3b("sem er bestur fyrir umhverfið",4.45)
            skilabod2b(spurningalisti[i],3.2)
            skilabod4(valAlisti[i],2.2)
            skilabod4(valBlisti[i],1.55)
            skilabod4(valClisti[i],1.2)
            fraestig(stig)
            takkar("A",690,250,75,75,WHITE,GREY,'a')
            takkar("B",690,350,75,75,WHITE,GREY,'b')
            takkar("C",690,450,75,75,WHITE,GREY,'c')
            pygame.display.update()
            clock.tick(10)
    b3Inngangur()

def giskA():
    global i
    if (i == 0):
        eittstig()
    elif (i == 1):
        nullstig()
    elif (i == 2):
        tvostig()
    elif (i == 3):
        nullstig()
    elif (i == 4):
        nullstig()
    else:
        tvostig()

def giskB():
    global i
    if (i == 0):
        tvostig()
    elif (i == 1):
        tvostig()
    elif (i == 2):
        nullstig()
    elif (i == 3):
        tvostig()
    elif (i == 4):
        tvostig()
    else:
        nullstig()

def giskC():
    global i
    if (i == 0):
        nullstig()
    elif (i == 1):
        eittstig()
    elif (i == 2):
        tvostig()
    elif (i == 3):
        nullstig()
    elif (i == 4):
        eittstig()
    else:
        eittstig()

def tvostig():
    rett()
    global i
    i += 1
    global stig
    gisk = True
    stig += 2
    while gisk:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Frábært!',3)
        skilabod2('Þú valdir umhverfisvænasta kostinn',2)
        fraestig(stig)
        takkar("Halda áfram",310,400,180,75,WHITE,GREY,'StartLevel2b')
        pygame.display.update()
        clock.tick(10)

def eittstig():
    rett()
    global i
    i += 1
    global stig
    gisk = True
    stig += 1
    while gisk:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Vel gert!',3)
        skilabod2('Þetta er þó ekki umhverfisvænasti kosturinn :/',2)
        fraestig(stig)
        takkar("Halda áfram",310,400,180,75,WHITE,GREY,'StartLevel2b')
        pygame.display.update()
        clock.tick(10)

def nullstig():
    vitlaust()
    global i
    i += 1
    global stig
    gisk = True
    stig = stig
    while gisk:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Æj æj',3)
        skilabod2('Þú valdir versta kostinn :(',2)
        fraestig(stig)
        takkar("Halda áfram",310,400,180,75,WHITE,GREY,'StartLevel2b')
        pygame.display.update()
        clock.tick(10)

# BORÐ 3 - SJÓBORÐ
# Inngangur
def b3Inngangur():
    tonlistsjor()
    inngangur3 = True
    while inngangur3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro, (0,0))
        skilabod1('Þú ert komin/nn í borð 3', 2.6)
        skilabod2('Ýttu á "Byrja!" til að hefja leik', 2.1)
        skilabod2('Meiri texti hér ef við viljum', 1.8)
        takkar("Byrja",150,450,150,75,WHITE,GREY,'StartLevel3b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(60)

############### Borð 3 ###################
def bord3():
    tonlistsjor()
    global stig
    #Upphafsstaður á háfi
    x = (display_breidd*0.35)
    y = (display_haed*0.73)
    x_change = 0
    #TELJARI
    counter, teljari = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('Sansation-Regular.ttf', 30)
    #Stærð og hreyfing á fiskum
    fiskur_byrjax = random.randrange(10,display_breidd-10)
    fiskur_byrjay = -600
    fiskur_hradi = random.randrange(10,14)
    fiskur_haed = 64
    fiskur_breidd = 72
    #Stærð og hreyfing á plasti
    plast_byrjax = random.randrange(10,display_breidd-10)
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
                teljari = str(counter).rjust(4) if counter > 0 else vinnurbord3(stig)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -25
                elif event.key == pygame.K_RIGHT:
                    x_change = 25
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
        fraestig(stig)
        #Þegar Háfurinn nær óvart fiski
        if (y < fiskur_byrjay + fiskur_haed):
            if ((x > fiskur_byrjax and x < fiskur_byrjax + fiskur_breidd) or (x + hafur_breidd > fiskur_byrjax and x + hafur_breidd < fiskur_byrjax + fiskur_breidd)):
                skilabod1("Æjæj þú átt að veiða plastið",5)
                #Hér eiga fræstigin að minnka...
                stig -= 1

        # Þegar háfurinn nær plasti
        if (y < plast_byrjay + plast_haed):
            if ((x > plast_byrjax and x < plast_byrjax + plast_breidd) or (x + plast_breidd > plast_byrjax and x + hafur_breidd < plast_byrjax + plast_breidd)):
                skilabod1("Flott!",5)
                # Hér eiga fræstigin að hækka...
                stig += 1

        pygame.display.update()
        clock.tick(20)

###### Vinna borð 3 #######
def vinnurbord3(stig):
    tonlistsjor()
    vinnab3 = True
    while vinnab3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro,(0,0))
        fraestig(stig)
        skilabod1('Til hamingju!',4)
        skilabod1('þú kláraðir borð 3',2.5)
        takkar("Halda áfram",310,450,190,75,WHITE,GREY,'StartLevel4')
        pygame.display.update()
        pygame.time.wait(10)

########## LOKABORÐ ############
def lokaBordInngangur():
    global stig
    inngangur4 = True
    while inngangur4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurIntro,(0,0))
        skilabod1('Til hamingju!',3.7)
        skilabod2('þú ert komin/nn á leiðarenda',2.6)
        skilabod2('Nú getur þú ...',2.1)
        skilabod2('Meiri texti hér ef við viljum',1.8)
        fraestig(stig)
        takkar("Halda áfram",150,450,190,75,WHITE,GREY,'StartLevel4b')
        takkar("Hætta",550,450,150,75,WHITE,GREY,'quit')
        pygame.display.update()
        clock.tick(10)

# Borð 4
def bord4():
    global stig
    bordfjogur = True
    while bordfjogur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        skjaMynd.blit(bakgrunnurb4, (0,0))
        fraestig(stig)
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
    pygame.mixer.music.load('toystory.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(1)

def tonlistsjor():
    pygame.mixer.music.load('undersea.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

#Hljóð sem kemur ef maður svarar rétt
def rett():
    pygame.mixer.music.load('rett.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(1)

#Hljóðið sem kemur ef maður svarar vitlaust
def vitlaust():
    pygame.mixer.music.load('rangt.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(1)

def ruslahljod():
    pygame.mixer.music.load('ruslhljod.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(1)


########  Skilaboð - texti #########
def skilabod1(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 50)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod1b(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 50)
    textSurf, textRect = textObjectsWhite(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod2(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Regular.ttf', 35)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod2b(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 35)
    textSurf, textRect = textObjectsWhite(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod3(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Light.ttf', 25)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod3b(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Regular.ttf', 25)
    textSurf, textRect = textObjectsWhite(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod3c(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Regular.ttf', 25)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod3d(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 25)
    textSurf, textRect = textObjectsBlack(texti, inngangstexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    skjaMynd.blit(textSurf, textRect)

def skilabod4(texti,lina):
    inngangstexti = pygame.font.Font('Sansation-Bold.ttf', 27)
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
            elif action == "a":
                giskA()
            elif action == "b":
                giskB()
            elif action == "c":
                giskC()
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
            b2Inngangur()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

if __name__=='__main__':
    main()
else:
    print('No just imported by another class')
