from Service.service import *

class Console:
    def __init__(self, contr):
        self.__contr = contr
    def meniu(self):
        print("1. Modificare melodii \n2. Genereaza melodii \n3. Exporta melodiile \n0. Iesire")
    def generare(self):
        n = input("Introduceti un numar intre 1 si 10: ")
        try:
            n = int(n)
            lista_titlu = input("Introduceti lista de titluri separate prin virgula: ")
            lista_art = input("Introduceti lista de artisti separati prin virgula: ")
            x = self.__contr.generare(n, lista_titlu, lista_art)
            print(f"S-au generat {x} entitati cu succes!")
        except ValueError:
            print("Introduceti un numar natural")

    def exportare(self):
        nume = input("Introduceti numele fisierului: ")
        nume = nume + ".txt"
        self.__contr.export(nume)
        print("Melodiile s-au exportat cu succes!")
    def afisare(self):
        self.__contr.display()

    def modificare(self):
        artist = input("Introduceti numele artistului: ")
        titlu = input("Introduceti numele melodiei: ")
        gen = input("Introduceti genul piesei: ")
        data = input("Introduceti data cu formatul dd.MM.yyyy: ")
        print(self.__contr.edit(artist, titlu, gen, data))
        return True


    def start(self):
        self.meniu()
        option = input("Introduceti un numar intre 0 si 3: ")
        try:
            option = int(option)
            if option < 0 or option > 4:
                raise ValueError()
            match option:
                case 0:
                    pass
                case 1:
                    self.modificare()
                    self.start()
                case 2:
                    self.generare()
                    self.start()
                case 3:
                    self.exportare()
                    self.start()
                case 4:
                    self.afisare()
                    self.start()
        except ValueError:
            print("Introduceti un numar cuprins intre 0 si 3!")