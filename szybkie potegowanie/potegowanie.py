import time
start_time = time.time()


def szybko(baza, potega):


    if potega == 0:
       return 1
    elif potega % 2 == 0:
        polpotegi = szybko(baza, potega//2)
        return polpotegi * polpotegi
    else:
        return baza * szybko(baza, potega-1)

baza = 2
potega = 1000

wynik = szybko(baza, potega)
print(f'{baza} do potegi {potega} = {wynik}')

print("--- %s seconds ---" % (time.time() - start_time))