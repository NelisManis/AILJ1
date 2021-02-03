import random
import math

# Opdracht 1 while loop
def op1a(n):
    var1 = 0
    while n > 0:
        var1 += 1
        n -= 1
        print('*' * var1)
    while var1 > 0:
        var1 -= 1
        print('*' * var1)

# opdracht 1 for loop
def op1b(n):
    var1 = 0
    for x in range(0, n):
        var1 += 1
        n -= 1
        print('*' * var1)
    for x in range(0, var1):
        var1 -= 1
        print('*' * var1)
    return

#  TODO: Werkt niet als tweede string langer is... Misschien nu wel...
# opdracht 2
def op2():
    var1 = 0
    input1 = input('Geef de eerste string:\n')
    input2 = input('Geef de tweede string:\n')
    if len(input1) < len(input2):
        langsteinput = input2
    else:
        langsteinput = input1
    for x in langsteinput:
        try:
            if x == input2[var1]:
                var1 += 1
            else:
                print('Het verschil zit op index', var1)
                return
        except IndexError:
            print('Het verschil zit op index', var1)
            return
    print('Er is geen verschil...')

# opdracht 3 count
def op3a(lst):
    var1 = 0
    for x in lst:
        if isinstance(x, int) == True:
            var1 += 1
        else:
            continue
    print(var1)

# opdracht 3 verschil
def op3b(lst):
    verschillst = []
    var1 = 0
    var2 = 1
    for x in range(0, len(lst) - 1):
        if lst[var1] - lst[var2] > 0:
            verschillst.append(lst[var1] - lst[var2])
        else:
            verschillst.append(-1 * (lst[var1] - lst[var2]))
        var1 += 1
        var2 += 1
    verschillst.sort()
    print(verschillst[-1])

# opdracht 3 1'en en 0'en
def op3c(lst):
    var0 = 0
    var1 = 0
    for x in lst:
        if x == 1:
            var1 += 1
        elif x == 0:
            var0 += 1
        else:
            return False

    if var0 < var1 and var0 <= 12:
        return True
    else:
        return False

# opdracht 4 bieb
def op4a(str):
    nieuwestr = ''.join(reversed(str))
    if nieuwestr == str:
        return True
    else:
        return False

# opdracht 4 zelf
def op4b(str):
    nieuwestr = ''
    for x in str:
        nieuwestr = x + nieuwestr
    if nieuwestr == str:
        return True
    else:
        return False

# opdracht 5
def op5(unsortedlst):
    sortedlst = []
    for var1 in unsortedlst:
        if len(sortedlst) == 0:
            sortedlst.append(var1)
        else:
            inserted = False
            for var2 in sortedlst:
                if var1 < var2:
                    continue
                elif var1 > var2 or var1 == var2:
                    m = sortedlst.index(var2)
                    sortedlst.insert(sortedlst.index(var2), var1)
                    inserted = True
                    break
                else:
                    sortedlst.append(var1)
                    inserted = True
                    break
            if inserted == False:
                sortedlst.append(var1)
    print(sortedlst)

# opdracht 6 lijst
def op6a(lst):
    print(sum(lst) / len(lst))

# opdracht 6 lijst van lijsten
def op6b(lsts):
    sumlst = []
    for lst in lsts:
        sumlst.append(sum(lst) / len(lst))
    print(sumlst)

# opdracht 7
def op7():
    min = int(input('Kies een minimum: '))
    max = int(input('Kies een maximum: '))
    while True:
        if max < min:
            max = int(input('Dit getal is kleiner dan je minimum. Kies een groter getal: '))
            if max > min:
                break
        else:
            break
    randomnummer = random.randint(min, max)
    teller = 0
    while True:
        teller += 1
        raden = int(input('Kies een getal: '))
        if raden == randomnummer:
            print('Gefeliciteerd, je hebt het in', teller, 'keer goed geraden!')
            break
        elif raden < randomnummer:
            print('Je moet groter denken.')
        elif raden > randomnummer:
            print('Veel te groot maat.')

# opdracht 8
def op8(oudbestand):
    print('Dit is het oude bestand:')
    print(oudbestand)
    tussenbestand = oudbestand.split('\n')
    nieuwbestand = ''
    for regel in tussenbestand:
        regel = regel.strip('\t')
        regel = regel.strip(' ')
        if regel == '':
            continue
        else:
            nieuwbestand= nieuwbestand + regel + '\n'
    print('\nDit is het nieuwe bestand:')
    print(nieuwbestand.strip(''))

# opdracht 9
# Ik kon het niet als int laten printen, want dan waren de 0'en aan het begin of einde weg...
def op9(ch, n):
    print(ch)
    ch = str(ch)
    if n > 0:
        for x in range(0, n):
            ch = ch + ch[0]
            ch = ch[1:]
    elif n < 0:
        for x in range(0, (n * -1)):
            ch = ch[-1] + ch
            ch = ch[:-1]

    print(ch)

# Opdracht 10
def op10(n, v0=0, v1=1):
    return op10(n-1, v1, v0+v1) if n > 1 else (v0, v1) [n]

# Opdracht 11
# 65-90
# 97-122
def op11(inputstr, rotatie):
    output = ''
    if rotatie > 0:
        for x in range(0, len(inputstr)):
            x = ord(inputstr[x])
            if x >= 48 and x <= 57:
                # cijfers
                nieuwerotatie = rotatie
                while nieuwerotatie > 10:
                    nieuwerotatie -= 10
                if x + nieuwerotatie > 57:
                    x = x + nieuwerotatie - 26
                else:
                    x = x + nieuwerotatie
            elif x >= 65 and x <= 90:
                # Hoofdletters
                nieuwerotatie = rotatie
                while nieuwerotatie > 26:
                    nieuwerotatie -= 26
                if x + nieuwerotatie > 90:
                    x = x + nieuwerotatie - 26
                else:
                    x = x + nieuwerotatie
            elif x >= 97 and x <= 122:
                # Kleine letters
                nieuwerotatie = rotatie
                while nieuwerotatie > 26:
                    nieuwerotatie -= 26
                if x + nieuwerotatie > 122:
                    x = x + nieuwerotatie - 26
                else:
                    x = x + nieuwerotatie
            else:
                pass
            x = chr(x)
            output = output + x
    elif rotatie < 0:
        for x in range(0, len(inputstr)):
            x = ord(inputstr[x])
            if x >= 48 and x <= 57:
                # cijfers
                nieuwerotatie = rotatie
                while nieuwerotatie < -10:
                    nieuwerotatie += 10
                if x + nieuwerotatie < 48:
                    x = x + nieuwerotatie + 26
                else:
                    x = x + nieuwerotatie
            elif x >= 65 and x <= 90:
                # Hoofdletters
                nieuwerotatie = rotatie
                while nieuwerotatie < -26:
                    nieuwerotatie += 26
                if x + nieuwerotatie < 65:
                    x = x + nieuwerotatie + 26
                else:
                    x = x + nieuwerotatie
            elif x >= 97 and x <= 122:
                # Kleine letters
                nieuwerotatie = rotatie
                while nieuwerotatie < -26:
                    nieuwerotatie += 26
                if x + nieuwerotatie < 97:
                    x = x + nieuwerotatie + 26
                else:
                    x = x + nieuwerotatie
            else:
                # Overige tekens
                pass
            x = chr(x)
            output = output + x
    else:
        output = input
    print(output)

# opdracht 12
def op12():
    for x in range(0, 100):
        if x % 3 == 0 and x != 0 and x % 5 != 0:
            print('fizz')
        elif x % 5 == 0 and x != 0:
            if x % 3 == 0:
                print('fizzbuzz')
            else:
                print('buzz')
        else:
            print(x)


# print('opdracht 1a')
# op1a(int(input('Geef een getal op: ')))
# print('\nopdracht 1b')
# op1b(int(input('Geef een getal op: ')))
# print('\nopdracht 2')
# op2()
# print('\nopdracht 3a')
# op3a([2, 4, 3, 6, 5, 9, 7.9, 2.7, 9, 8.4])
# print('\nopdracht 3b')
# op3b([2, 4, 3, 6, 5, 9, 7, 2, 9, 8, -10, 29, 6, 103, 7, 3, 5])
# print('\nopdracht 3c')
# print(op3c([1,0,1,1,0,1,0,0,1,0,1,1,0,1]))
# print(op3c([1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0]))
# print(op3c([1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# print('\nopdracht 4a')
# print(op4a('Haii'))
# print(op4a('lepel'))
# print('\nopdracht 4b')
# print(op4b('Haiii'))
# print(op4b('Lepel lepeL'))
# print(op4b('lepel'))
# print(op4b('Lepel'))
# print('\nOpdracht 5')
# op5([5,7,4,9,2,8,15,84,76,35,16,4])
# print('\nOpdracht 6a')
# op6a([1,4,5,2,58,45,1,6,7])
# print('\nOpdracht 6b')
# op6b([[1,4,5,2,58,45,1,6,7], [5,8,4,7,3,6,1,5,8,9,5,4,5,7], [5,4,5,4,5,8,52,48,84,6,89,62]])
# print('\nOpdracht 7')
# op7()
# print('\nOpdracht 8')
# op8('Hallo\nDit is een bestand\n\nHoe gaat het?\nDit is opdracht 8\n\tHier staat een tab voor\nHier staat een\ttab tussen\n Hier staat een spatie voor\n')
# print('\nOpdracht 9')
# op9(100101101, 4)
# op9(1001101101011010, -3)
# op9(10010101100101010, 0)
# print('\nOpdracht 10')
# print(op10(int(input('Geef een getal op: '))))
# print('\nOpdracht 11')
# op11(input('Geef een string:\n'), int(input('Geef een rotatie:\n')))
# print('\nOpdracht 12')
op12()
