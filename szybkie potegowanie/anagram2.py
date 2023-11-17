slowo1 = input("Podaj 1 słowo: ")
slowo2 = input("Podaj 2 słowo: ")

slowoarray1 = [*slowo1]
slowoarray2 = [*slowo2]

whop = sorted(slowoarray1)
yip = sorted(slowoarray2)

if whop == yip:
    print("wyrazy są anagramami")
else:
    print("wyrazy nie są anagramami")

