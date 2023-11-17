import time
start_time = time.time()

baza = 2
potega = 1000
wynik = baza**potega

print(f'{baza} do potegi {potega} = {wynik}')

print("--- %s seconds ---" % (time.time() - start_time))