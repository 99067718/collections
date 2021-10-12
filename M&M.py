import random
Zak = []
Zak_V2 = {}

colors = ["oranje", "blauw", "groen", "bruin"]


def sorteren(soortCheck):
    soort = soortCheck(type)
    if soort == "list":
        return Zak.sort()

    elif soort == "dict":
        return sorted(soortCheck)

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
Alphabetic = sorted(Zak)
print((listToStringWithoutBrackets(Alphabetic)))

dictionlisted = diction(amount())

print(dictionlisted)
Sorted_Items = sorted(dictionlisted, key=lambda x: dictionlisted[x], reverse=True)
print(Sorted_Items)

