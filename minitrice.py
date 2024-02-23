

def Operation(Operateur, Calcul):
    ope1, ope2 = Calcul.split(Operateur)
    ope1, ope2 = int(ope1), int(ope2)  # Exception si le string ne peut être converti
    if Operateur == "/" and ope2 == 0:  # Cas division par 0
        print("Division par 0")
        raise SystemExit(1)  #On sort du programme avec le code erreur 1
    else:
        print(eval(Calcul))

def compter_operateurs(Calcul):
    # Compte le nombre total d'opérateurs dans l'expression
    return sum(Calcul.count(op) for op in ["+","-","/"])

#Programme principale
if __name__ == "__main__":
    while True:
        try:
            ope_Calcul = input()
            
            #Cas : Press "ENTER" dans l'invite
            if ope_Calcul == "":
                print("Fin des Calculs :)")
                break
            
            # Si le nombre d'opérteur excède 1 on affiche une erreur de syntaxe
            if compter_operateurs(ope_Calcul) > 1:
                print("Erreur de syntaxe pour le calcul: \"" + ope_Calcul + "\"")
                raise SystemExit(1)

            operatorFound= False

            list_Operation = ["+","-","/"]
            #Vérification de présence d'opérateur
            for i in list_Operation:
                if(i in ope_Calcul):
                    operatorFound = True
                    try:
                        Operation(i, ope_Calcul)
                    except:
                        print("Erreur de syntaxe pour le calcul: \""+ ope_Calcul +"\"")
                        SystemExit(-1)

            if(operatorFound is False):
                print("Erreur de syntaxe pour le calcul: \""+ ope_Calcul +"\"")
                SystemExit(-1)
              
        except EOFError:
            print("Fin des Calculs :)")
            break

        
