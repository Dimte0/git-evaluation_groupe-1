Avant d'effectuer ce programme il vous sera demander d'installer Python.
Sur linux python est normalement déjà pré-installé.
Sur Windows 2 chemins sont possibles:
- Taper python sur le microsoft Store et installer
- Télécharger python sur internet et lancer l'exécutable

Se placer dans le bon répertoire pour effectuer les commandes 
Lancement du programmme minitrice:
./minitrice.py

Après avoir lancé le programme differentes intéractions sont possibles:
2+2 ( Effectuer des opérations)
Appuyer sur la touche Entrer (pour valider la saisie, si la ligne est vide cela déclenche la sortie du programme)


Exemple:
````bash
./minitrice.py
2+2
4
````

Gestion des erreurs:
generator.py
Si aucun argument ou plusieurs arguments en entrée:
````bash
1.$./generator.py
2. Manque ou surplus d'argument
````
 Si un entier n'est pas renseigné :
 ````bash
1.$./generator.py 2.2
2. Erreur : l'argument n'est pas un entier 
````


minitrice.py
Si executé sans argument ( touche entrée):
 ````bash
1.$./minitrice.py
2.
3. Fin des calculs :)
````

Si plusieurs opérateur détectés :
 ````bash
1.$./minitrice.py
2.2+2+1
3. Erreur de syntaxe  pour le calcul : "2+2+1"
````
