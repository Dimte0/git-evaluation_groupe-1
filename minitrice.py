

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
    return sum(Calcul.count(op) for op in ["+", "/"])

#Programme principale
if __name__ == "__main__":
    while True:
        try:
            ope_Calcul = input()

            #Cas : Press "ENTER" dans l'invite
            if ope_Calcul == "":
                print("Fin des Calculs :)")
                raise SystemExit(0) 
            
            # Si le nombre d'opérteur excède 1 on affiche une erreur de syntaxe
            if compter_operateurs(ope_Calcul) > 1:
                print("Erreur de syntaxe pour le calcul: \"" + ope_Calcul + "\"")
                raise SystemExit(1)

            #Vérification de présence d'opérateur
            op_trouve = False
            for i in ["+", "/"]:
                if i in ope_Calcul: 
                    Operation(i, ope_Calcul)
                    op_trouve = True
                    break

            #Si il n'y a pas d'opérateur on affiche un message d'erreur
            if not op_trouve:
                print("Erreur de syntaxe pour le calcul: \""+ ope_Calcul +"\"")
                raise SystemExit(1)
            
        except EOFError:
            break
