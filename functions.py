import tkinter
from tkinter import *
import random

# Listes des noms de villes
ListeVilles = ["Évry","Marseille","Lyon","Toulouse","Nice","Nantes","Strasbourg","Montpellier","Bordeaux","Lille",
               "Rennes","Reims","Le Havre","Saint-Étienne","Toulon","Grenoble","Angers","Dijon","Brest","Le Mans",
               "Nîmes","Aix-en-Provence","Clermont-Ferrand","Tours","Amiens","Limoges","Villeurbanne","Metz",
               "Besançon","Perpignan","Orléans","Caen","Mulhouse","Boulogne-Billancourt","Rouen","Nancy",
               "Argenteuil","Montreuil","Saint-Denis","Roubaix","Paris","Maisons-Alfort","Cergy","Laval", 
               "Cannes","Saint-Hilaire","Viry-Châtillon","Cesson","La Rochelle","Melun","Hyères"]

##################################################################################################
def entryValid():
    var = False
    print("\n")
    if len(nbVilles.get())>0 and len(nbVilles.get())<=2 and (nbVilles.get())!="0" and (nbVilles.get()).isdigit():
        if int(nbVilles.get())<=50:
            print(f"Vous avez choisi {nbVilles.get()} villes")
            var = True
    if var == False:
        print("Le nombre de villes doit être compris entre 1 et 50")
        bouton.config(state = tkinter.DISABLED)
    else:
        bouton.config(state = tkinter.ACTIVE)
    return var

##################################################################################################
# Fonction pour générer un nom de ville aléatoire
def genererNomVille():
    # Si la liste est vide, on affiche une erreur
    if not ListeVilles:
        raise ValueError("Le nombre maximal de ville est de 50.")
    # On choisit aléatoirement la ville parmi la liste de villes
    Villes = random.choice(ListeVilles)
    # On supprime la ville choisie afin d'éviter de réutiliser la ville plusieurs fois
    ListeVilles.remove(Villes)
    return Villes

##################################################################################################
# Fonction pour générer une matrice de distances aléatoires entre les villes
def genererMatriceDistances(n):
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(1, 100)
            matrice[i][j] = distance
            matrice[j][i] = distance
    return matrice

##################################################################################################
# Fonction pour générer une liste de n villes aléatoires
def genererVilles(n):
    villes = []
    suppVilles = []
    for _ in range(n):
        nom = genererNomVille()
        villes.append(nom)
        suppVilles.append(nom)
    for v in suppVilles:
        ListeVilles.append(v)
    return villes

##################################################################################################
# Fonction pour calculer la distance totale d'un circuit
def distance_totale(circuit, matrice_distances):
    distance_totale = 0  # Réinitialiser la distance à 0 pour chaque circuit
    for i in range(len(circuit)):
        ville1 = circuit[i]
        if i == len(circuit) - 1:
            ville2 = circuit[0]  # Retour à la ville de départ
        else:
            ville2 = circuit[i + 1]
        distance_totale += matrice_distances[ville1][ville2]
    return distance_totale

##################################################################################################
# Fonction pour afficher une matrice carrée
def afficherMatriceCarree(matrice):
    n = len(matrice)
    max_len = max(len(str(matrice[i][j])) for i in range(n) for j in range(n))
    format_str = "{:" + str(max_len) + "}"
    for i in range(n):
        ligne = [format_str.format(matrice[i][j]) for j in range(n)]
        print(" ".join(ligne))

##################################################################################################
# Fonction pour générer une population initiale de circuits aléatoires
def generer_population_initiale(n, taille_population):
    population = []
    for i in range(taille_population):
        circuit = list(range(n))
        random.shuffle(circuit)
        population.append(circuit)
    return population

##################################################################################################
#fonction pour échanger le début et la fin de deux circuits
def croisement(circuit1,circuit2):
    deb = 0
    fin = len(circuit1)//2
    newCircuit1 = []
    newCircuit2 = []
    for i in range(deb,fin):
            newCircuit1.append(circuit1[i])
            newCircuit2.append(circuit2[i])
    for i in range(fin, len(circuit1)):
        if circuit2[i] not in circuit1:
            newCircuit1.append(circuit2[i])
        if circuit1[i] not in circuit2:
            newCircuit2.append(circuit1[i])
    print(f"{newCircuit1}")
    print(f"{newCircuit2}")

##################################################################################################
# Fonction pour calculer le fitness
def calculer_fitness(circuit, matrice_distances):
    distance_totale = distance_totale(circuit, matrice_distances)
    if distance_totale == 0:
        return float('inf')  # Éviter la division par 0
    else:
        return 1 / distance_totale

##################################################################################################
# Fonction qui selectionne les 5 meilleurs circuits en fonction du fitness
def selection_par_tri(population, fitness_population):
    # Trier la population par ordre croissant de fitness
    population_triee = sorted(zip(population, fitness_population))
    # Sélectionner les 5 meilleurs circuits
    parents = [circuit for circuit, _ in population_triee[:5]]
    return parents

##################################################################################################
# Fonction pour muter un circuit
def mutation(circuit):
    # On choisit 2 villes au hasard
    ville1, ville2 = random.sample(range(len(circuit)), 2)
    # On inverse leur ordre
    circuit[ville1], circuit[ville2] = circuit[ville2], circuit[ville1]
    return circuit
    
##################################################################################################
def graphe():
    bouton.config(state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable

    n = int(nbVilles.get())
    villes = genererVilles(n)
    matrice_distances = genererMatriceDistances(n)
    circuit = list(range(n))
    random.shuffle(circuit)
    taille_population = 10 # nombre de circuit
    distance = distance_totale(circuit, matrice_distances)
    
    print("--------------------------------------------------------------------------------------")
    print("Distance totale du circuit initial :", distance)
    print("Circuit :", [villes[i] for i in circuit])
    print("\n")
    afficherMatriceCarree(matrice_distances)
    print("\n")

    population = generer_population_initiale(n, taille_population)
    for i, circuit in enumerate(population):
        distance = distance_totale(circuit, matrice_distances)
        print(f"Circuit {i+1} (distance = {distance}) : {[villes[j] for j in circuit]}")


################################################# AFFICHAGE #################################################
fenetre = tkinter.Tk()
fenetre.title("Affichage du graphe")
fenetre.minsize(width=216, height=47)
fenetre.configure(pady=10)
    
txt = tkinter.Label(text = "Nombre de villes :")
txt.grid(column = 0, row = 0)
    
nbVilles = tkinter.Entry(justify=CENTER, width=5)
nbVilles.grid(column = 1, row = 0)
    
bouton = tkinter.Button(text = "GO!", activebackground="green", activeforeground="white")
bouton.grid(column = 4, row = 0)

bouton.config(command = graphe) # pr lancer notre fonction quand le button est pressé

valid = tkinter.Button(text = "Valider", activebackground="green", activeforeground="white")
valid.grid(column = 3, row = 0)
valid.config(command = entryValid)

fenetre.mainloop()
   
