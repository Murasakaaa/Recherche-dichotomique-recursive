import tkinter as tk
from tkinter import ttk


# ------------------------------------------------- ALGORITHME RECURSIF -------------------------------------------------
def r_dichotomique_recursive(n: int, t: list) -> bool:
    """
    Algorithme de recherche dichotomique par récursivité.
    Renvoie True si n est dans t, False sinon.
    T doit être un tableau d'entiers, triés par ordre croissant, ou vide"""

    if t != sorted(t):  # Programmation défensive : sécurité condition tab trié
        raise ValueError("le tableau t doit être trié!")

    if t == []:
        return False  # 1e Cas de base : si tableau vide, n ne peut pas être dans le tableau

    milieu = (len(t) - 1) // 2

    if n == t[milieu]:  # 2e cas de base et principe dichotomique : si l'élément du milieu est n, on renvoie true
        return True

        # Principe récursif :
    if n < t[
        milieu]:  # si n est inférieur au milieu, on appelle récursivement le programme sur la moitié inférieure du tableau
        return r_dichotomique_recursive(n, t[0:milieu])
    if n > t[
        milieu]:  # si n est supérieur au milieu, on appelle récursivement le programme sur la moitié supérieure du tableau
        return r_dichotomique_recursive(n, t[milieu + 1:])


# batterie de tests
assert r_dichotomique_recursive(15, []) == False  # test tableau vide
assert r_dichotomique_recursive(3, [1, 2, 3]) == True  # test valeur dans le tableau
assert r_dichotomique_recursive(4, [1, 2, 3]) == False  # test valeur hors du tableau
assert r_dichotomique_recursive(1, [e for e in range(100)]) == True  # test tableau long

# ------------------------------------------------- TKINTER -------------------------------------------------

fenetre = tk.Tk()
fenetre.title('Recherche dichotomique récursive')
fenetre.geometry('1080x300')
fenetre.resizable(False, False)

n = 0
t = []


def ajout_tab() -> None:
    """lorsque le bouton est pressé ajoute le nb entré dans le tab et tri le tab"""
    item = int(entreeRemplirTab.get())
    t.append(item)  # ajout valeur
    t.sort()  # tri, obligatoire pour la recherche dichotomique
    tabCourant.config(text=str(t))  # mis a jour sur l'interface


def reset_tab() -> None:
    """fonction qui lorsque le bouton est pressé réinitialise le tableau en affichage et en donnée"""
    global t
    t = []  # réinitialisation du tableau t global
    tabCourant.config(text=str(t))  # mise a jour sur l'interface


def recherche_entry() -> None:
    """lorsque le bouton est pressé lance la recherche dichotomique et affiche le résultat"""
    n = int(entreeRecherche.get())
    resultatRechercheDichotomique = r_dichotomique_recursive(n, t)  # stockage résultat dans une variable
    resultat.config(text=f"Résultat : {resultatRechercheDichotomique}")  # affichage sur l'interface


def button_complexity() -> None:
    """lorsque le bouton est pressé lance la création du graphique du calcul de la complexité"""
    tailles = []  # Tableau des tailles n de tableau
    delais = []  # Tableau des delais d'execution du programme

    for n in range(1000, 10000, 1000):  # Remplissage tableau tailles
        tailles.append(n)

    for n in tailles:  # Remplissage tableau delais
        delais.append(delai_algorithme([e for e in range(1, n + 1)]))
    graph(tailles, delais)


# ------------------------------------------------- WIDGETS -------------------------------------------------

# ------------------[ widget labelFrame : Boite pour appliquer l'algorithme ]------------------
labelframeTableau = ttk.LabelFrame(master=fenetre, text="Création du tableau")
labelframeTableau.pack()

frame0 = ttk.Frame(labelframeTableau)
frame0.pack(pady=10, padx=70)

# ttk label
tabCourant = ttk.Label(frame0, text='[]')
tabCourant.grid(row=0)

# widget Entry : Champs de saisie de la valeur a ajouté dans le tableau
entreeRemplirTab = ttk.Entry(frame0)
entreeRemplirTab.grid(row=1, column=0)

# widget button : lancer la recherche de la valeur entrée dans EntreeRecherche
ajoutButton = ttk.Button(frame0, text="ajouter", command=ajout_tab)
ajoutButton.grid(row=1, column=1)

# widget button : Réinitialisation du tableau en tableau vide []
resetButton = ttk.Button(frame0, text="Reset", command=reset_tab)
resetButton.grid(row=0, column=1)

# ------------------[ widget labelFrame : Boite pour appliquer l'algorithme ]------------------
labelframeRecherche = ttk.LabelFrame(master=fenetre, text="Recherche dichotomique : application")
labelframeRecherche.pack()

frame1 = ttk.Frame(labelframeRecherche)
frame1.pack(pady=15, padx=70)

# widget Entry : Champs de saisie de la valeur a rechercher dans le tableau
entreeRecherche = ttk.Entry(frame1)
entreeRecherche.grid(row=0, column=0)

# widget button : lancer la recherche de la valeur entrée dans EntreeRecherche
recherche = ttk.Button(frame1, text="Rechercher", command=recherche_entry)
recherche.grid(row=0, column=1)

# widget Label : affiche le résultat
resultat = ttk.Label(frame1, text="Résultat : ")
resultat.grid(row=1)

# ------------------[ widget labelFrame : Boite pour étude de la complexité ]------------------
labelframeComplexite = ttk.LabelFrame(master=fenetre, text="Calcul de la complexité")
labelframeComplexite.pack()

# widget button : Lancer graphique de complexité)
btn_complexity = ttk.Button(labelframeComplexite, text="test", command=button_complexity)
btn_complexity.pack(pady=10, padx=132)

# ------------------------------------------------- COMPLEXITE -------------------------------------------------

import time
import matplotlib.pyplot as plt


def delai_algorithme(tab: list) -> float:
    """Calcul du temps d'éxecution de l'algorithme de recherche dichotomique récursif
    On se place dans le pire cas, on recherche un nombre qui n'est PAS dans le tableau"""
    start = time.perf_counter()
    r_dichotomique_recursive(0, tab)
    end = time.perf_counter()
    return (end - start)
    # delai en secondes


def graph(tab_x: list, tab_y: list) -> None:  # la fonction graphique
    """tab_x=liste des x, tab_y=liste des y, place les points(x,y)"""
    fig = plt.figure()  # creation feuille graphique
    plt.title("Complexité temporelle algorithme recherche dichotomique récursive")  # titre
    plt.xlabel('tailles des tableaux')  # Label Axe des x
    plt.ylabel('durée d\'éxecution')  # Label Axe des y
    plt.plot(tab_x, tab_y)  # placement point par point
    fig.savefig('graph.png')  # sauvegarde sous le nom 'graph.png'
    plt.show()  # Affichage du graphe


fenetre.mainloop()

