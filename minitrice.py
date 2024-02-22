

#Programme principale
if __name__ == "__main__":

    #init
    while(1):

        try:
            ope_Calcul = input()
        except:
            break
        
        if(ope_Calcul == ""):
            print("Fin des Calculs :)")
            break

        list_Operation = ["+"]
        #Vérification de présence d'opérateur
        if('+' in ope_Calcul):

            try:
                ope1, ope2 = ope_Calcul.split('+')
                ope1, ope2 = int(ope1), int(ope2) #exception si le string ne peut être converti
                print(ope1 + ope2)

            except:
                print("Erreur de syntaxe pour le calcul: \""+ ope_Calcul +"\"")
                SystemExit(-1)
        else:
            print("Erreur Syntaxique dans l'opération envoyée")
            SystemExit(-1)
    