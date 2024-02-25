from Domain.entitate import *
class RepoInMemory():
    def __init__(self):
        """
        Se initializeaza clasa
        """
        self.__lista = []
    def store(self, melodie):
        """
        Stocheaza o melodie in colectia de date
        :param melodie: Melodie
        :return:
        """
        self.__lista.append(melodie)
    def getAll(self):
        """
        :return: lista de melodii
        """
        return self.__lista
    def search(self, artist, titlu):
        """
        Cauta o melodie cu combinatia artist-titlu
        :param artist: string
        :param titlu: string
        :return: True daca melodia a fost gasita in colectie de date, False in caz contar
        """
        ok = 0
        for i in self.__lista:
            if artist == i.getArtist() and titlu == i.getTitlu():
                ok = 1
        if ok == 0: return False
    def modificare(self, artist, titlu, gen, zi, luna, an):
        """
        Modifica genul si data unei melodii identificate dupa combinatia artist-titlu
        :param artist: str
        :param titlu: str
        :param gen: str
        :param zi: int
        :param luna: int
        :param an: int
        :return:
        """
        for i in self.__lista:
            if artist == i.getArtist() and titlu == i.getTitlu():
                i.setGen(gen)
                i.setZi(zi)
                i.setLuna(luna)
                i.setAn(an)
        return True

class RepoInFile(RepoInMemory):
    def __init__(self, filename : str):
        """
        Se initializeaza clasa
        :param filename: str
        """
        RepoInMemory.__init__(self)
        self.filename = filename
        self.read()
    def read(self):
        """
        Se citesc linile din fisierul dat
        :return:
        """
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                lista = line.split(",")
                lista = [element.strip() for element in lista]
                titlu = str(lista[1])
                artist = str(lista[0])
                gen = str(lista[3])
                lista1 = lista[2].split(".")
                zi = int(lista1[0])
                luna = int(lista1[1])
                an = int(lista1[2])
                melodie = Melodie(titlu, artist, gen, zi, luna, an)
                self.store(melodie)
    def store(self, melodie : Melodie):
        """
        Se stocheaza fiecare linie citita in colectia de date
        :param melodie:
        :return:
        """
        RepoInMemory.store(self, melodie)
        self.write()
    def write(self):
        """
        Scrie fiecare melodie din colectia de date in fisierul dat
        :return:
        """
        lista = RepoInMemory.getAll(self)
        with open(self.filename, 'w', encoding="utf-8") as f:
            for i in lista:
                data = ".".join([str(i.getZi()), str(i.getLuna()), str(i.getAn())])
                linie = ", ".join([str(i.getArtist()), str(i.getTitlu()), str(data), str(i.getGen()), "\n"])
                f.write(linie)

def test_repo():
    repo = RepoInFile("Testrepo.txt")
    lista = repo.getAll()
    assert lista[0].getArtist() == "YE"
    assert repo.search("YE", "Mistakes") == 0
    repo.modificare("Ye", "Company", "Pop", 3, 3, 2009)
    repo.write()
    lista = repo.getAll()
    assert lista[0].getGen() == "Rock"
    assert lista[0].getZi() == 3
    assert lista[0].getLuna() == 3
    assert lista[0].getAn() == 2009
