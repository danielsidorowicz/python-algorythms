wiersze = []
with open('sygnaly.txt') as plik:
    for wiersz in plik:
        wiersz = wiersz.rstrip(wiersz[-1])
        wiersze.append(wiersz)
    plik.close()

i = 0
unique = {}
max = ''
max_len = 0
while i < len(wiersze):
    yip = set(wiersze[i])
    if len(yip) > max_len:
        max = yip
        max_len = len(yip)

    i+=1

print(max, max_len)
