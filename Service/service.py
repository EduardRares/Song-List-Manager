from Domain.entitate import *
from Repo.repository import *
from Domain.Validator import *
import random
class Service:
    def __init__(self, repo):
        """
        se initializeaza clasa Service
        :param repo: class
        """
        self.__repo = repo
    def generare(self, n, titlu, artist):
        """
        Se genereaza n entitati noi, daca n depaseste numarul de combinari de entitati noi posbile, atunci se vor genera doar numarul de entitati posibile
        :param n: int
        :return: numarul de entitati noi generate
        """
        lista_artist = artist.split(",")
        lista_artist = [element.strip() for element in lista_artist]
        lista_titlu = titlu.split(",")
        lista_titlu = [element.strip() for element in lista_titlu]
        lista_gen = ["Rock", "Pop", "Jazz"]
        count = 0
        for i in range(n):
            x = random.randint(0, len(lista_artist) - 1)
            nume_artist = lista_artist[x]
            x = random.randint(0, len(lista_titlu) - 1)
            titlu_artist = lista_titlu[x]
            x = random.randint(1, 3)
            gen = lista_gen[x - 1]
            zi = random.randint(1, 30)
            luna = random.randint(1, 12)
            an = random.randint(1980, 2024)
            melodie = Melodie(titlu_artist, nume_artist, gen, zi, luna, an)
            if self.__repo.search(nume_artist, titlu_artist) == 0:
                self.__repo.store(melodie)
                count += 1
            elif count < len(lista_titlu) * len(lista_artist):
                i -= 1

        return count
    def merge_sort(self, lista, start, end):
        """
        Sortare crescatoare lista de melodii dupa data
        :param lista: list
        :param start: int
        :param end: int
        :return:
        """
        if start < end:
            mid = (end + start) // 2
            self.merge_sort(lista, start, mid)
            self.merge_sort(lista, mid + 1, end)
            j = mid + 1
            i = start
            lista1 = []
            while i <= mid and j <= end:
                if lista[i].getAn() < lista[j].getAn():
                    lista1.append(lista[i])
                    i += 1
                elif lista[i].getAn() == lista[j].getAn() and lista[i].getLuna() < lista[j].getLuna():
                    lista1.append(lista[i])
                    i += 1
                elif lista[i].getAn() == lista[j].getAn() and lista[i].getLuna() == lista[j].getLuna() and lista[i].getZi() < lista[j].getZi():
                    lista1.append(lista[i])
                    i += 1
                else:
                    lista1.append(lista[j])
                    j += 1
            for k in range(i, mid + 1):
                lista1.append(lista[k])
            for k in range(j, end + 1):
                lista1.append(lista[k])
            for i in range(len(lista1)):
                lista[i + start] = lista1[i]

    def export(self, fisier):
        """
        Se exporteaza toate colectia de date ordonata dupa criteriul impus
        :param fisier: str
        :return:
        """
        lista = self.__repo.getAll()
        self.merge_sort(lista, 0, len(lista) - 1)
        with open(fisier, 'w', encoding="utf-8") as g:
            for i in lista:
                data = ".".join([str(i.getZi()), str(i.getLuna()), str(i.getAn())])
                linie = ", ".join([str(i.getArtist()), str(i.getTitlu()), str(data), str(i.getGen()), "\n"])
                g.write(linie)
        return True
    def display(self):
        """
        Se afiseaza colectia de date
        :return:
        """
        lista = self.__repo.getAll()
        for i in lista:
            print(i)
    def edit(self, artist, titlu, gen, data):
        """
        Se modifica genul si data melodiei dorite
        :param artist: str
        :param titlu: str
        :param gen: str
        :param data: str
        :return: Un mesaj corespunzator
        :error: Utilizatorul primeste un mesaj de eroare in cazul in care data nu respecta formatul dd.MM.yyyy sau nu este o data valida sau genul nu exista sau combinatia artisti - titlu nu exista
        """
        try:
            lista = data.split(".")
            if len(lista) != 3: raise ValueError
            zi = int(lista[0])
            luna = int(lista[1])
            an = int(lista[2])
        except ValueError:
            return("Data nu este valida")
        obj = Validare_melodie(gen, zi, luna, an)
        erori = obj.validare()
        if len(erori) > 0: return erori
        else:
            ok = self.__repo.search(artist, titlu)
            if ok == 0: return "Nu exista combinatia artist-titlu data!"
            else:
                self.__repo.modificare(artist, titlu, gen, zi, luna, an)
                self.__repo.write()
                return "Modificarea a avut loc cu succes!"

def test_generare():
    contr = Service(RepoInFile("Testgenerare.txt"))
    n = 10000
    assert contr.generare(n) == 100
def test_edit():
    contr = Service(RepoInFile("Testedit.txt"))
    assert contr.edit("Smiley", "Acasa", "Pop", "abcs") == "Data nu este valida"
    assert contr.edit("Smiley", "Acasa", "Poppp", "21.15.2004") == "Genul nu este Rock/Pop/Jazz\nLuna trebuie sa fie un numar cuprins intre 1 si 12\n"
    assert contr.edit("Smiley", "Thriller", "Rock", "10.10.2004") == "Nu exista combinatia artist-titlu data!"
    assert contr.edit("YE", "Company", "Rock", "3.3.2009") == "Modificarea a avut loc cu succes!"

def test_export():
    contr = Service(RepoInFile("Testedit.txt"))
    contr.export("abc.txt")
    songs = []
    with open("abc.txt", 'r') as f:
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
            songs.append(melodie)
    print("1\n1\n1\n")
    print(songs)
    assert songs[0].getArtist() == "Don Toliver"
    assert songs[0].getTitlu() == "Montero"
    assert songs[0].getGen() == "Pop"
    assert songs[0].getZi() == 13
    assert songs[0].getLuna() == 10
    assert songs[0].getAn() == 1980

