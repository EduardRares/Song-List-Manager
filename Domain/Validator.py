class Validare_melodie():
    def __init__(self, gen, zi, luna, an):
        self.__gen = gen
        self.__zi = zi
        self.__luna = luna
        self.__an = an
    def validare(self):
        error = []
        lista_genuri = ["Rock", "Pop", "Jazz"]
        if self.__gen not in lista_genuri: error.append("Genul nu este Rock/Pop/Jazz")
        if self.__zi < 1 or self.__zi > 30: error.append("Ziua trebuie sa fie un numar cuprins intre 1 si 30")
        if self.__luna < 1 or self.__luna > 12: error.append("Luna trebuie sa fie un numar cuprins intre 1 si 12")
        if self.__an < 1980 or self.__an > 2024: error.append("Anul trebuie sa fie un numar cuprins intre 1980 si 2024")
        erori = ""
        for i in range(len(error)):
            erori = erori + "".join([str(error[i])]) + "\n"
        return erori

