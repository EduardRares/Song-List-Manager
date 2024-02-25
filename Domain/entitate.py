class Melodie:
    def __init__(self, titlu, artist, gen, zi, luna, an):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__zi = zi
        self.__luna = luna
        self.__an = an
    def getTitlu(self):
        return self.__titlu
    def getArtist(self):
        return self.__artist
    def getGen(self):
        return self.__gen
    def getZi(self):
        return self.__zi
    def getLuna(self):
        return self.__luna
    def getAn(self):
        return self.__an
    def setGen(self, gen_nou):
        self.__gen = gen_nou
    def setZi(self, zi_noua):
        self.__zi = zi_noua
    def setLuna(self, luna_noua):
        self.__luna = luna_noua
    def setAn(self, an_nou):
        self.__an = an_nou
    def __str__(self):
        return f'{self.getArtist()}, {self.getTitlu()}, {self.getZi()}.{self.getLuna()}.{self.getAn()}, {self.getGen()}'


def test_entitate():
    melodie1 = Melodie("kaskjvb", "asvb", "Jazz", 21, 10, 2114)
    assert melodie1.getTitlu() == "kaskjvb"
    assert melodie1.getArtist() == "asvb"
    assert melodie1.getGen() == "Jazz"
    assert melodie1.getZi() == 21
    assert melodie1.getLuna() == 10
    assert melodie1.getAn() == 2114
    melodie1.setGen("Rock")
    assert melodie1.getGen() == "Rock"
    melodie1.setZi(1)
    melodie1.setLuna(1)
    melodie1.setAn(1)
    assert melodie1.getZi() == 1
    assert melodie1.getLuna() == 1
    assert melodie1.getAn() == 1