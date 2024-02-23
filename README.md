
**Installation**

Afin de pouvoir vous lancer dans l'exécution des différents programmes, il vous sera demandé d'installer une version de Python3.
Sur linux python est normalement déjà pré-installé.
Sur Windows 2 chemins sont possibles:
- Rechercher python sur le microsoft Store et installer
- Télécharger python sur internet et lancer l'exécutable


Se placer dans le bon répertoire pour effectuer les commandes .

Lancement du programmme minitrice:

./minitrice.py

Après avoir lancé le programme différentes intéractions sont possibles:
- Inscrire des opérations à la suite de l'éxécution (Un résultat sera par la suite envoyé) : ( 2+2 ; 5*7)
Appuyer sur la touche ENTER pour valider la saisie (si la ligne est vide, cela entraîne l'arrêt du programme).

**Exécution**: 

Ici, on vous présente des exemples d'exécution des programmes disponibles.

Avec le programme "minitrice.py", vous pouvez effectuer des opérations comme présenté ci-dessus.


````bash
./minitrice.py
2+2
4
5*7
35

Fin des Calculs :)
````


Vous pouvez également effectuer un pipe sur l'entrée standard du programme "minitrice.py".

````bash
echo 5+5 | ./minitrice.py
10
````


Le programme "generator.py", génère des opérations aléatoires qui varient selon l'argument inscrit en paramètre (Voir la Section "Generator" pour la gestion des différentes erreurs).

````bash
./generator.py 5 | ./minitrice.py
1139
-352
34650
341
993
````

Vous pouvez bien évidemment le coupler avec "minitrice.py".


````bash
./generator.py 5 | ./minitrice.py
1139
-352
34650
341
993
````


Si executé sans argument ( touche ENTER):

 ````bash
1.$./minitrice.py
2.
3. Fin des calculs :)
````

Si plusieurs opérateurs détectés :

 ````bash
1.$./minitrice.py
2.2+2+1
3. Erreur de syntaxe  pour le calcul : "2+2+1"
````


**Générator** : 

***Gestion des erreurs***

Ici, nous allons faire la description des différentes erreurs que vous pouvez rencontrer sur le programme "generator.py".

Si aucun argument ou plusieurs arguments en entrée:

````bash
1.$./generator.py
2. Manque ou surplus d'argument
````

 Si l'argument ne peut pas être converti comme un entier :
 ````bash
1.$./generator.py 2.2
2. Erreur : l'argument n'est pas un entier 
````

**Publication** : 

Le lien de la vidéo GOURCE : https://youtu.be/6sBaMwAqrnU

**Liens utiles** : 

-aucune ressource externe n'a été utilisée

