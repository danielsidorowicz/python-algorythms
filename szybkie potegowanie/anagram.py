def anagram(slowo1, slowo2, x, i, j):
    slowoarray1 = [*slowo1]
    slowoarray2 = [*slowo2]
    whop = sorted(slowoarray1)
    yip = sorted(slowoarray2)
    print(whop, yip)
    if i == len(whop):
        return print("Wyrazy są anagramami")
    elif j > len(whop):
        return print("Wyrazy nie są anagramami")
    if whop[x] == yip[x]:
        i+=1
    return anagram(slowo1, slowo2, x+1, i, j+1)

anagram("burzaaaaaa", "arbuz", 0, 0, 0)