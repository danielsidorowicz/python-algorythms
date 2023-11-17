import math

liczba = str(input("Podaj liczbe: "))
system = int(input("Podaj system liczbowy podanej liczby: "))
system_wanted = int(input("Podaj system liczbowy ktory chcemy osiagnac: "))

liczba_list = list(liczba)


j = len(liczba_list) - 1
k = 0
wynik = 0
lista = []

liczba = int(liczba)

# if system == 10:
#     while liczba != 0:
#         reszta = int(liczba) % system_wanted
#         lista.append(reszta)
#         liczba = math.floor(liczba / system_wanted)
#     lista.reverse()
# else:
#     for i in liczba_list:
#         wynik = wynik + (int(liczba_list[k]) * system**j)
#         j-=1
#         k+=1
#     print(wynik)


def DecToOther(liczba, system_wanted):
    while liczba != 0:
        reszta = int(liczba) % system_wanted
        lista.append(reszta)
        liczba = math.floor(liczba / system_wanted)
    lista.reverse()
    print(lista)

def OtherToDec(liczba_list, k, j):
    for i in liczba_list:
        wynik = wynik + (int(liczba_list[k]) * system**j)
        j-=1
        k+=1
    print(wynik)

if system == 10:
    DecToOther(liczba, system_wanted)
else:
    OtherToDec(liczba_list, k, j)
