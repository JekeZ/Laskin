import math
def funktio():
    eka = int(input("Anna ensimmäinen luku: "))
    toka = int(input("Anna toinen luku: "))
    while True:
        print ("(1)+ \n(2)- \n(3)* \n(4)/\n(5)sin(luku1/luku2) \n(6)cos(luku1/luku2) \n(7) Vaihda luvut \n(8) Lopeta \nValitut luvut: ", eka, toka)
        valinta = int(input("Tee valinta (1-8): "))
        if(valinta == 1):
                    print("Tulos on: ", eka + toka)
                    continue

        elif(valinta == 2):
                    print("Tulos on: ", eka - toka)
                    continue

        elif(valinta == 3):
                    print("Tulos on: ", eka * toka)
                    continue

        elif(valinta == 4):
                    print ("Tulos on: ", eka / toka)
                    continue
        elif(valinta == 5):
                    print("Tulos on : ",  math.sin(eka / toka))
                    continue
        elif(valinta == 6):
                    print ("Tulos on: ", math.cos(eka / toka))
                    continue
        elif(valinta == 7):
                    uusivalinta = int(input("Anna uusi ensimmäinen luku: "))
                    uusivalinta2 = int(input("Anna uusi toinen luku: "))
        elif(valinta == 8):
                    return
        while True:
                    print ("(1)+ \n(2)- \n(3)* \n(4)/\n(5)sin(luku1/luku2) \n(6)cos(luku1/luku2) \n(7) Vaihda luvut \n(8) Lopeta \nValitut luvut: ", uusivalinta, uusivalinta2)
                    valinta = int(input("Tee valinta (1-8): "))

                    if(valinta == 1):
                        print("Tulos on: ", uusivalinta + uusivalinta2)
                        continue

                    elif(valinta == 2):
                        print("Tulos on: ", uusivalinta - uusivalinta2)
                        continue

                    elif(valinta == 3):
                        print("Tulos on: ", uusivalinta * uusivalinta2)
                        continue

                    elif(valinta == 4):
                        print ("Tulos on: ", uusivalinta / uusivalinta2)
                        continue

                    elif(valinta == 5):
                        print("Tulos on : ",  math.sin(uusivalinta / uusivalinta2))
                        continue

                    elif(valinta == 6):
                        print ("Tulos on: ", math.cos(uusivalinta / uusivalinta2))
                        continue
                    elif(valinta == 7):
                        continue

                    elif(valinta == 8):
                        return
funktio()