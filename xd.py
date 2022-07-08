import json
import random

while True:
    grupy = (1, 2, 3, 4)

    def pokazmecze(meczedef):
        print("Koszyk:", meczedef[i]["koszyk"])
        print("-", meczedef[i]["1"])
        print("-", meczedef[i]["2"])
        print("-", meczedef[i]["3"])
        print("-", meczedef[i]["4"])
        print()

    print("Losowanie grup Pucharu JD")
    print()

    with open("xd.json") as plik:
        mecze = json.load(plik)

        for i in range(0, len(mecze)):
            pokazmecze(mecze)

        print("----------------------------------------------")
        print()

        zuzytegrupy = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

        for x in range(0, len(grupy)):

            file = open(str(x) + ".txt", "a+")

            file.write("Grupa " + str(x + 1))

            for i in range(0, len(grupy)):

                grupa = random.choice(zuzytegrupy[i])

                file.write("\n")
                file.write("- " + mecze[int(i)][str(grupa)])
            
                zuzytegrupy[i].remove(grupa)

            file.close()

    for i in range(0, 4):
        
        los = input("Naciśnij Enter aby wylosować grupę")

        file = open(str(i) + ".txt", "r")

        for i in range(0, 5):
            linia = file.readline()
            print(linia.strip())
    
    for i in range(0, 4):
        open(str(i) + ".txt", "w").close

    print("1. Wyjdź | 2. Przeprowadź losowanie jeszcze raz")

    while True:
        wybor = input("Wprowadź wartość: ")

        if wybor == "1" or wybor == "2":
            break
        else:
            continue

    if wybor == "1":
        break

    
