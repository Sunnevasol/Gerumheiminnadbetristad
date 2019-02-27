class Bord2():
    def __init__(self):
        pass

    def byrja_bord2(self):
        print('Þú ert komin/nn í borð 2 þar sem þú átt að svara nokkrum spurningum')
        #Setja fram lista af spurningum?
        #Random fall sem kallar á listann af sp og velur tvær sp
        #if og else fyrir stigagjöf ef rétt ágiskun
            #Mínus stig (fræ) ef röng ágiskun
    from random import randint
    spurn1 = "Hvernig ætlar þú í skólann í dag?"
    spurn2 = "Þegar ég fer í búðina þá: "
    spurn3 = "Þegar ég er búin með mjólkina þá: "
    spurn4 = "Hvað gerir þú við fötin þín þegar þau passa ekki lengur? "
    spurn5 = "Þegar ég tannbursta mig þá: "
    spurn6 = "Þegar ég klára ekki kvöldmatinn minn þá: "
    spurn_listi=[spurn1,spurn2,spurn3,spurn4,spurn5,spurn6]
    teljari = 3
    Heildarstig = 0 #ná í stig frá borði 1 kann ekki
    for i in range(teljari):
        random_spurn = randint(0,len(spurn_listi)-1)
        spurn = spurn_listi[random_spurn]
        spurn_listi.remove(spurn)
        if(spurn == spurn1):
            teljari = teljari -1
            print()
            print(spurn)
            print("  a. Strætó")
            print("  b. Hjóli")
            print("  c. Fá far hjá ömmu")
            inntak = input("Svar: ")
            if(inntak == "a"):
                Heildarstig = Heildarstig + 1
                print("Gott val þú fékkst 1 fræ, en það er þó enn betra að fara með hjóli þar sem það mengar minnst")
                print("Þú færð 1 fræ")

            elif(inntak == "b"):
                Heildarstig = Heildarstig + 2
                print("Já hárrétt hjá þér, hjól er besti valkosturinn!")
                print("Þú færð 2 fræ")


            else:
                 print("Ahh þetta var versti valkosturinn, best er að fara á hjóli")
                 print("Þú færð 0 fræ")

        elif(spurn == spurn2):
            teljari = teljari -1
            print()
            print(spurn)
            print("  a. Tek ég með mér taujpoka" )
            print("  b. Kaupi 3 plastpoka í búðinni")
            print("  c. Kaupa maíspoka")
            inntak = input("Svar: ")
            if(inntak == "a"):
                Heildarstig = Heildarstig + 2
                print("Vel gert! Þetta var besti valkosturinn")
                print("Þú færð 2 fræ")

            elif(inntak == "b"):
                print("Æjæj þetta var ekki rétt, það er mjög óumhverfisvænt að kaupa svona mikið af plastpokum, best er að taka með taujpoka í búðina")
                print("Þú færð 0 fræ")

            else:
                Heildarstig = Heildarstig + 1
                print("Gott Val, það er þó enn umhverfisvænna að taka með taujpoka í búðina")
                print("Þú færð 1 fræ")

        elif(spurn == spurn3):
            teljari = teljari -1
            print()
            print(spurn)
            print("  a. Hendi ég fernunni í ruslið" )
            print("  b. Skola hana, læt þorna og hendi henni svo í pappatunnuna")
            print("  c. Læt hana aftur inn í ísskáp og mamma gengur frá henni")
            inntak = input("Svar: ")
            if(inntak == "a"):
                print("Æjæj þetta var rangt svar, mundu að við þurfum að flokka!")
                print("Þú færð 0 fræ")

            elif(inntak == "b"):
                Heildarstig = Heildarstig + 2
                print("Vel gert! Hárrétt hjá þér")
                print("Þú færð 2 fræ")

            else:
                Heildarstig = Heildarstig + 1
                print("Gott Val, það er þó enn betra að ganga frá henni og flokka sjálfur")
                print("Þú færð 1 fræ")

        elif(spurn == spurn4):
            teljari = teljari -1
            print()
            print(spurn)
            print("  a. Fer með þau í rauðakrossinn" )
            print("  b. Hendi þeim í ruslið")
            print("  c. Gef litla frænda/frænku þau")
            inntak = input("Svar: ")
            if(inntak == "a"):
                print("Vel gert! hárrétt hjá þér")
                print("Þú færð 2 fræ")

            elif(inntak == "b"):
                print("Æjæj þetta var ekki rétt, best er að gefa þau svo hægt sé að endurnýta fötin")
                print("Þú færð 0 fræ")

            else:
                Heildarstig = Heildarstig + 2
                print("Vel gert! hárrétt hjá þér")
                print("Þú færð 2 fræ")

        elif(spurn == spurn5):
            teljari = teljari - 1
            print()
            print(spurn)
            print("  a. Læt ég vatnið renna allan tímann" )
            print("  b. Skrúfa frá rétt á meðan ég bleyti burstann")
            print("  c. Ég tannbursta mig ekki")
            inntak = input("Svar: ")
            if(inntak == "a"):
                print("Æjæj þetta var vitlaust hjá þér, við viljum ekki eyða vatni að óþörfu")
                print("Þú færð 0 fræ")

            elif(inntak == "b"):
                Heildarstig = Heildarstig + 2
                print("Vel gert! hárrétt hjá þér")
                print("Þú færð 2 fræ")

            else:
                print("Æjæj ertu búin að gleyma Karíus og Baktus, mundu að tannbursta þig næst")
                print("Þú færð 0 fræ")
        else:
            teljari = teljari - 1
            print()
            print(spurn)
            print("  a. Hendi ég honum í svörtu tunnuna" )
            print("  b. Set afganginn í box og inni ísskáp")
            print("  c. Hendi ég honum í brúnu moltu tunnuna")
            inntak = input("Svar: ")
            if(inntak == "a"):
                print("Æjæj þetta var rangt, við setjum matarleifar í brúnu moltutunnuna")
                print("Þú færð 0 fræ")

            elif(inntak == "b"):
                Heildarstig = Heildarstig + 2
                print("Frábært svar, gott að leifa ekki matnum")
                print("Þú færð 2 fræ")

            else:
                Heildarstig = Heildarstig + 1
                print("Gott svar! Það er samt betra að henda ekki mat")
                print("Þú færð 1 fræ")

    print("Þú hefur lokið borði 2, þú ert núna komin með " , Heildarstig, "fræ")



def main():
    pass

if __name__ == '__main__':
    main()
else:
    print('Skráin var importuð af annarri skrá')
