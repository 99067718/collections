import random


colors = ["oranje", "blauw", "groen", "bruin"]
Zak = []


def toevoegen(kleuren:list, aantal: int):
    for i in range(aantal):
        Zak.append(random.sample(kleuren,1))
    return Zak

toevoegen(colors,10)
print(Zak)
