<div align="center">
  <h1>Recherche-dichotomique-recursive</h1>
  <!-- <img src="https://github.com/allenai/OLMo/assets/8812459/774ac485-a535-4768-8f7c-db7be20f5cc3" width="300"/> -->
  <img src="https://github.com/Murasakaaa/Recherche-dichotomique-recursive/assets/119632356/17da6306-27fa-4f70-9460-9be5a1bba00f?raw=true" alt="image of tkinter interface" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</div>

Programme de recherche dichotomique récursive en Python avec interface graphique Tkinter.

Programme réaliser dans le cadre d'un projet du premier trimestre en cours de spécialité Numérique et Sciences de l'Informatique ( NSI ) au lycée. Le projet a été réaliser en groupe avec [@Candlio] (https://github.com/Candlio)
Compte rendu à partir de l'explication du choix, réalisé par ce dernier.

## Comment fonctionne le programme :

- On a tout d'abord un espace de création du tableau. On entre un nombre entier dans le champ de saisie puis on appuie sur 'ajouter' pour ajouter notre nombre au tableau. Le tableau est trié à chaque fois qu'un nombre est ajouté.
  Pour réinitialiser le tableau, on a le bouton 'reset'. Cela va supprimer entièrement le tableau et le rendre à nouveau vide.
- Le second espace sert à appliquer la recherche dichotomique à notre tableau. On entre d'abord dans le champ de saisie l'entier qu'on va chercher puis on appuie sur le bouton rechercher pour lancer la recherche.
  On sait par la suite si l'entier appartient au tableau grâce au résultat : `False` si il n'y est pas et `True` si il y est.
- Le dernier espace sert à calculer la compléxité de notre programme. En appuyant sur le bouton 'test', un graphique de la complexité apparaît à l'écran.

## Explication du choix de l'algorithme :

De manière générale, le principe récursif admet une efficacité limitée.
Cependant, l'algorithme de recherche dichotomique de base est réputé pour son efficacité et sa complexité logarithmique.
Il serait donc intéressant d'étudier les performances de la version récursive de ce dernier.

## Présentation de l'algorithme :

- **Préconditions :** Tableau composé de valeurs entières, entier à rechercher

- **Post-conditions :** Renvoie un booléen, `True` si l'entier est dans le tableau, `False` si il ne l'est pas. On pose `n` un entier à rechercher et `t` un tableau

- **Cas de base :** si `t` est un tableau vide [], `n` n'est pas dans `t`. Renvoie `False`.

## Principe récursif:

Soit `m`, l'indice au milieu de `t`.`(m=(len(t)-1)//2)`

Si n == t[m], `n` est dans `t`. Renvoie `True`.
Sinon, si `n<t[m]`, `n` peut se trouver dans la partie inférieure/gauche de `t`. On appelle récursivement l'algorithme avec en entrée `n` et `t[:m]`
sinon, `n>t[m]`, `n` peut se trouver dans la partie supérieure/droite de `t`. On appelle récursivement l'algorithme avec en entrée `n` et `t[m+1:]`.

## Analyse critique des performances :
<div align="center">
  <img src="https://github.com/Murasakaaa/Recherche-dichotomique-recursive/assets/119632356/ef1e65c0-26dc-4416-ab3c-1c8bc6be1d6f?raw=true" alt="image of the graph" width="600" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</div>


Comme l'indique le graphique, l'algorithme montre une complexité linéaire.
Cela est un résultat plutôt satisfaisant pour un algorithme récursif.
De plus, après tests, on peut affirmer que cet algorithme peut prendre en charge des tableaux de tailles allant jusqu'à 10^7.
Cela est également un résultat satisfaisant compte tenu de la limite de 1000 appelles de python.

Cependant, on n'arrive pas à la complexité logarithmique espérée avec le principe de recherche dichotomique de base.
Il serait possible, par des moyens plus complexes néanmoins, de compléter le programme pour atteindre, toujours par principe récursif, une complexité logarithmique.
