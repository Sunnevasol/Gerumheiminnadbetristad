class Bord1():
    def __init__(self):
        pass

    def inntakRangt (self, value):
        if value == 0:
            sentence = "æjæj þetta var ekki rétt, reyndu aftur"
        elif value == 1:
            sentence = "æjæj þetta var ekki rétt, reyndu aftur"
        elif value == 2:
            sentence = "æjæj þetta var ekki rétt, endilega spilaðu leikinn aftur til að bæta þig"
        else:
            sys.exit()
        return sentence

    def inntakRett (self, value):
        if value == 0:
            sentence = "Þetta var rétt hjá þér, vel gert!"
        elif value == 1:
            sentence = "Þetta var næstum því rétt hjá þér, vel gert!"
        elif value == 2:
            sentence = "Þetta var rétt hjá þér vel gert! :)"
        else:
            sys.exit()
        return sentence

############################
#Gamli skipanalínuleikurinn
############################

    def byrja_bord1(self):
        print('Þú ert komin/nn í borð 1 þar sem flokka þarf rusl')
        #setja fram lista af nr. á tunnum
        #Búa til lista fyrir myndirnar af ruslinu sem þarf að flokka og skilgr hvað er hvað
        #bua til random fall sem velur random 6 rusl úr listanum sem á að flokka
        #bua til if og else til að gefa stig og lata hlut hverfa ef rett agiskun

        from random import randint

        rusl_listi = ["pepsi-dós","epli", "bananahýði","plaströr","mjólkurferna","svalaferna","skyrdolla","tyggjó","eyrnapinni","kókflaska"]
        tunnur_listi = ["plasttunna","pappatunna","lífrænn úrgangur","almennt rusl", "flöskur og dósir"]
        tunnur_numer =["1","2","3","4","5"]

        teljari = 6
        heildarstig = 0

        print("höfum eftirfarandi tunnur:")
        print()
        for x in range(len(tunnur_listi)):
            print("nr ",x+1,tunnur_listi[x])
            print()



        for i in range(teljari):
            random_rusl=randint(0,len(rusl_listi)-1)
            rusl = rusl_listi[random_rusl]
            rusl_listi.remove(rusl)
            inntak = input("í hvaða tunnu fer " + rusl +"? ")
            if(rusl == "epli" or rusl == "bananahýði"):
                rett = tunnur_numer[2]
                if(inntak == rett):
                    print("rétt hjá þér!!")
                    heildarstig = heildarstig + 1
                    teljari= teljari -1

                else:
                    print("æjæj þetta var ekki rétt")
                    teljari = teljari -1
                    heildarstig = heildarstig -1
            elif(rusl=="pepsi-dós" or rusl == "kókflaska"):
                rett = tunnur_numer[4]
                if(inntak == rett):
                    print("rétt hjá þér!!")
                    heildarstig = heildarstig + 1
                    teljari= teljari -1

                else:
                    print("æjæj þetta var ekki rétt")
                    teljari = teljari -1
                    heildarstig = heildarstig -1
            elif(rusl == "plaströr" or rusl=="skyrdolla" ):
                rett = tunnur_numer[0]
                if(inntak == rett):
                    print("rétt hjá þér!!")
                    heildarstig = heildarstig + 1
                    teljari= teljari -1


                else:
                    print("æjæj þetta var ekki rétt")
                    teljari = teljari -1
                    heildarstig = heildarstig -1

            elif(rusl == "mjólkurferna" or rusl == "svalaferna" ):
                rett = tunnur_numer[1]
                if(inntak == rett):
                    print("rétt hjá þér!!")
                    heildarstig = heildarstig + 1
                    teljari= teljari -1

                else:
                    print("æjæj þetta var ekki rétt")
                    teljari = teljari -1
                    heildarstig = heildarstig - 1

            elif(rusl == "tyggjó" or rusl == "eyrnapinni" ):
                rett = tunnur_numer[3]
                if(inntak == rett):
                    print("rétt hjá þér!!")
                    heildarstig = heildarstig + 1
                    teljari= teljari -1

                else:
                    print("æjæj þetta var ekki rétt")
                    teljari = teljari -1
                    heildarstig = heildarstig - 1
        print("Þú hefur lokið borði 1, þú ert núna komin með " , heildarstig, "fræ")

    def main():
        pass

    if __name__ == '__main__':
            main()
    else:
        print('Skráin var importuð af annarri skrá')
