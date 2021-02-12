import random
import itertools
import csv


def controleren(gok, geheimecode):
    goedfout = [0, 0]
    gokkopie = gok[:]
    geheimecodekopie = geheimecode[:]
    for value in range(0, len(gok)):
        if gok[value] == geheimecode[value]:
            goedfout[0] += 1
            gokkopie.pop(value)
            gokkopie.insert(value, 'None')
            geheimecodekopie.pop(value)
            geheimecodekopie.insert(value, 'enoN')

    for value in range(0, len(gokkopie)):
        if gokkopie[value] in geheimecodekopie:
            goedfout[1] += 1
            geheimecodekopie.remove(gokkopie[value])

    return goedfout

def eruittyfen(mogelijkheden, gok, goedfout):
    result = []
    for mogelijkheid in mogelijkheden:
        if goedfout == controleren(gok, mogelijkheid):
            result.append(mogelijkheid)

    return result



kleurlist = ['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink']
allecominaties = list(itertools.product(['White', 'Silver', 'Blue', 'Green', 'Yellow', 'Orange', 'Red', 'Pink'], repeat=4))
allecominatieslijst = [list(option) for option in allecominaties]


geheimecode = ['Silver', 'Red', 'Green', 'Red']

eerstegok = []
for x in range(0, 3):
    if x == 0:
        kleur12 = random.choice(kleurlist)
        eerstegok.append(kleur12)
        eerstegok.append(kleur12)
    else:
        kleur34 = random.choice(kleurlist)
        while kleur34 in eerstegok:
            kleur34 = random.choice(kleurlist)
        eerstegok.append(kleur34)


print(geheimecode)
print(eerstegok)
goedfout = controleren(eerstegok, geheimecode)
mogelijkheden = eruittyfen(allecominatieslijst, eerstegok, controleren(eerstegok, geheimecode))
print(mogelijkheden)

while goedfout != [4, 0]:
    randomchoice = random.choice(mogelijkheden)
    mogelijkheden = eruittyfen(mogelijkheden, randomchoice, controleren(randomchoice, geheimecode))
    goedfout = controleren(randomchoice, geheimecode)
    print(goedfout)
    print(len(mogelijkheden))

print(mogelijkheden)

