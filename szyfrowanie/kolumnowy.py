message = "Konstatnynopol"
columns = 17
count = 0
objet = {}
iks = 0

for i in range(columns):
    objet[i] = []

while count < len(message) - 1:
    for i in range(columns):
        if count != len(message) -1:
            objet[i] += str(message[count])
        if count < len(message) - 1:
            count+=1

text = ''
for i in range(len(objet)):
    for j in range(len(objet[i])):
        text += objet[i][j]

print(text)
