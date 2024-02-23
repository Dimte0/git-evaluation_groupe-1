Avant d'effectuer se programme il vous sera demander d'installer Python.
Sur linux python est normalement déjà pré-installer.
Sur Windows 2 chemins sont possible:
- Taper python sur le microsoft Store est installer
- Télécharger python sur internet est lancé exécutable

Se placer dans le bon répertoire pour effectuer les commandes 
Lancement du programmme minitrice:
./minitrice.py

Après avoir lancer le programme vous pouvez faire differente intéraction:
2+2 ( Effectuer des opérations)
Appuyer sur la touche Entrer (pour valider la saisie, si la ligne est vide sorti du programme)


Exemple:
````bash
./minitrice.py
2+2
4
````

Gestion des erreurs:
generator.py
Si aucun argument ou plusieurs argument est entrer:
````bash
1.$./generator.py
2. Manque ou surplus d'argument
````
 Si un entier n'est pas renseigner :
 ````bash
1.$./generator.py 2.2
2. Erreur : l'argument n'est pas un entier 
````


minitrice.py
Si executé vide ( touche entrée):
 ````bash
1.$./minitrice.py
2.
3. Fin des calculs :)
````

Si plusieurs opérateur d'étecté :
 ````bash
1.$./minitrice.py
2.2+2+1
3. Erreur de syntaxe  pour le calcul : "2+2+1"
````
