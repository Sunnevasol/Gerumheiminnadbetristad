import unittest
from unittest import mock

from bord1 import Bord1


class Testleikur (unittest.TestCase):
    def setUp(self):
        self.bord=Bord1()
        self.teljari=0

    def test_1(self):
        self.assertEqual(self.bord.inntakRangt(0), 'æjæj þetta var ekki rétt, reyndu aftur')
        self.assertEqual(self.bord.inntakRangt(2), 'æjæj þetta var ekki rétt, endilega spilaðu leikinn aftur til að bæta þig')


    def test_2(self):
        self.assertEqual(self.bord.inntakRett(0), 'Þetta var rétt hjá þér, vel gert!')
        self.assertEqual(self.bord.inntakRett(1), 'Þetta var næstum því rétt hjá þér, vel gert!')

if __name__ =='__main__':
    unittest.main()
