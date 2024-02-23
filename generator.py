import sys
import random

if __name__ == "__main__":
    if len(sys.argv) == 2:

        try:
            #vérifie la convertion du string en int
            nb = int(sys.argv[1])

            listOperator = ["+","-"]
            sizeListOpe = len(listOperator)
            # Boucle la création
            for i in range (0,nb):
                print( str(random.randint(1,1000)) + listOperator[random.randint(0, sizeListOpe-1)] + str(random.randint(1,1000)))

        except:
            print("Erreur : l'argument n'est pas entier")
            SystemExit(-1)
    else:
        print("Manque ou surplus d'arguments")
        SystemExit(-1)
