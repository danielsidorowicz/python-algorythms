wiersze = []
with open('sygnaly.txt') as plik:
    for wiersz in plik:
        wiersze.append(wiersz)
    plik.close()

i=39
litery = ''
while(i < len(wiersze)):
    litery = str(litery) + str(wiersze[i][9])
    i+=40



print(litery)
