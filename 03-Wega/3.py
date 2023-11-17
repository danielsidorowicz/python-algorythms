wiersze = []
with open('sygnaly.txt') as plik:
    for wiersz in plik:
        wiersz = wiersz.rstrip(wiersz[-1])
        wiersze.append(wiersz)
    plik.close()


i = 0
takiewyrazy = []

while i < len(wiersze):
    truearray = []
    j = 0
    while j < len(wiersze[i]) - 1:
        if abs(ord(wiersze[i][j]) - ord(wiersze[i][j+1])) <= 10:
            truearray.append('t')
        j+=1
    if len(truearray) + 1 == len(wiersze[i]):
        takiewyrazy.append(wiersze[i])
    i+=1

print(takiewyrazy)
print(len(takiewyrazy))