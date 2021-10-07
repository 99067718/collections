import random
Zak = []
Zak_V2 = {}

colors = ["oranje", "blauw", "groen", "bruin"]

def amount():
    return int(input("Hoeveel M&M's wil je in je zakje?: "))

def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','').replace(",",'')

def toevoegen(aantal: int):
    for i in range(aantal):
        new = random.choice(colors)
        Zak.append(new)
    return Zak

def diction(aantal: int):
    for i in range(aantal):
        new = random.choice(colors)
        if new in Zak_V2:
            Zak_V2[new] += 1
        else:
            Zak_V2[new] = 1
    return Zak_V2
        

toevoegen(amount())

print(listToStringWithoutBrackets(Zak))

print(diction(amount()))

