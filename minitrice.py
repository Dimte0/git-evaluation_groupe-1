

def Operation(Operateur, Calcul):
    ope1, ope2 = Calcul.split(Operateur)
    ope1, ope2 = int(ope1), int(ope2) #exception si le string ne peut être converti
    
    print(eval(Calcul))

#Programme principale
if __name__ == "__main__":

    #init
    while(1):

        #Input Request
        try:
            ope_Calcul = input()
        #Cas : Fin de lecture d'un fichier
        except:
            break #Rompt "while"
        
        #Cas : Press "ENTER" dans l'invite
        if(ope_Calcul == ""):
            print("Fin des Calculs :)")
            break #Rompt "while"

        operatorFound= False

        list_Operation = ["+","-"]
        #Vérification de présence d'
        for i in list_Operation:
            if(i in ope_Calcul):
                operatorFound= True
                try:
                    Operation(i, ope_Calcul)
                except:
                    print("Erreur de syntaxe pour le calcul: \""+ ope_Calcul +"\"")
                    SystemExit(-1)
                    
        if(operatorFound is False):
            print("Erreur Syntaxique dans l'opération envoyée")
            SystemExit(-1)
    
