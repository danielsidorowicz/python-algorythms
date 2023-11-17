words = ["jabłko", "banan", "arbuz", "ananas", "gruszka"]

sortedWords = sorted(words)

print(sortedWords)


# words.sort()
# print(words)


sortedWordsDesc = sorted(words, reverse=True)
print(sortedWordsDesc)


def alfbubsort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

alfbubsort(words)
print(words)
