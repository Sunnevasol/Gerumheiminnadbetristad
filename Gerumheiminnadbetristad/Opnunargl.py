from bord1 import Bord1
from bord2 import Bord2
from bord3 import Bord3

class Byrja:
    def __init__(self, byrja=1 , haetta=2):
        self.byrja = byrja
        self.haetta = haetta

    def byrja_leik(self):
        print ('Þú ert í upphafsborði')
    #Viltu hefja leikinn? ef ja-> kalla a bord 1 klasa og fall
        bord1_start = Bord1()
        bord1_start.byrja_bord1()
    #Viltu hefja leikinn? ef ja/1-> kalla a bord 2 klasa og fall
        bord2_start = Bord2()
        bord2_start.byrja_bord2()
    #Viltu hefja leikinn ef ja/1-> kalla a bord 3 klasa og fall
        bord3_start = Bord3()
        bord3_start.byrja_bord3()

def main():
    start=Byrja()
    start.byrja_leik()

if __name__ == '__main__':
    main()
