
**Installation**

Afin de pouvoir vous lancez dans l'exécution des différents programmes, il vous sera demander d'installer une version de Python3.
Sur linux python est normalement déjà pré-installer.
Sur Windows 2 chemins sont possible:
- Taper python sur le microsoft Store est installer
- Télécharger python sur internet est lancé exécutable


Se placer dans le bon répertoire pour effectuer les commandes 
Lancement du programmme minitrice:

./minitrice.py

Après avoir lancer le programme vous pouvez faire differente intéraction:
    - Inscrit des opérations à la suite de l'execution (Un résultat sera par la suite envoyé) : ( 2+2 ; 5*7)
Appuyer sur la touche ENTER pour valider la saisie (si la ligne est vide sorti du programme)

**Exécution**: Un exemple d'utilisation de votre programme, avec la sortie attendu, comme ce qui fait dans ce document,

Ici, on vous présente des exemples d'éxecution des programmes disponibles.

Avec le programme "minitrice.py", vous pouvez effectuez des opérations comme présenter ci-dessus

````bash
./minitrice.py
2+2
4
5*7
35

Fin des Calculs :)
````

Vous pouvez également effectue un pipe sur l'entrée standard du programme "minitrice.py"

````bash
echo 5+5 | ./minitrice.py
10
````

Le programme "generator.py", génère des opérations aléatoire qui varie selon l'argument inscrit en paramètre (Voir la Section "Generator" pour la gestion des différentes erreurs)

````bash
./generator.py 5 | ./minitrice.py
1139
-352
34650
341
993
````

Vous pouvez bien évidemment l'accouplez avec "minitrice.py"

````bash
./generator.py 5 | ./minitrice.py
1139
-352
34650
341
993
````

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

**Générator** : Description de la gestion de ou des erreurs que vous avez mis en place sur le programme generator. La ou les procédures pour reproduire le ou les erreurs doivent être renseignées,

***Gestion des erreurs***

Ici, nous allons faire la description des différentes erreurs que vous pouvez rencontrez sur le programme "generator.py"

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

insérer liens utiles 

