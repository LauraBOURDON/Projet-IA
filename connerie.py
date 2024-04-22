import tkinter
from tkinter import *
import random
import networkx as nx
import matplotlib.pyplot as plt

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
    return newCircuit1, newCircuit2

##################################################################################################
# Fonction pour calculer le fitness
def calculer_fitness(circuit, matrice_distances):
    distanceTotale = distance_totale(circuit, matrice_distances)
    if distanceTotale == 0:
        return float('inf')  # Éviter la division par 0
    else:
        return 1 / distanceTotale

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
    tauxDeMutation = 0.5 # Taux de mutation afin que la mutation n'ait pas tout le temps lieu
    if random.random() < 0.5:
        # On choisit 2 villes au hasard
        ville1, ville2 = random.sample(range(len(circuit)), 2)
        # On inverse leur ordre
        circuit[ville1], circuit[ville2] = circuit[ville2], circuit[ville1]

    return circuit
##################################################################################################
def algorithme_génétique(n, taille_population, matrice_distances, pourcentage_sans_amelioration, nb_generations_max):
    # Initialisation de la population
    villes = genererVilles(n)
    population = generer_population_initiale(n, taille_population)

    circuit = list(range(n))
    random.shuffle(circuit)
    distance = distance_totale(circuit, matrice_distances)
    print("--------------------------------------------------------------------------------------")
    print("Distance totale du circuit initial :", distance)
    print("Circuit :", [villes[i] for i in circuit])
    print("\n")
    afficherMatriceCarree(matrice_distances)
    print("\n")
    for i, circuit in enumerate(population):
        distance = distance_totale(circuit, matrice_distances)
        print(f"Circuit {i+1} (distance = {distance}) : {[villes[j] for j in circuit]}")


    # Mémorisation du meilleur circuit trouvé
    meilleur_circuit = None
    meilleure_fitness = 0

    nb_generations_sans_amelioration_actuel = 0
    nb_generations_sans_amelioration_max = int(nb_generations_max * pourcentage_sans_amelioration)

    for generation in range(nb_generations_max):
        # Évaluation de la fitness de chaque individu
        fitness_population = [(calculer_fitness(circuit, matrice_distances)) for circuit in population]

        # Sélection des meilleurs individus
        parents = selection_par_tri(population, fitness_population)

        # Croisement pour générer la nouvelle population
        nouvelle_population = []
        for i in range(0, len(parents)-2, 2):
            circuit1, circuit2 = parents[i], parents[i+1]
            enfant1, enfant2 = croisement(circuit1, circuit2)
            nouvelle_population.append(enfant1)
            nouvelle_population.append(enfant2)

        # Mutation de la nouvelle population
        for i in range(len(nouvelle_population)):
            nouvelle_population[i] = mutation(nouvelle_population[i])

        # Remplacement de la population
        population = nouvelle_population

        # Mise à jour du meilleur circuit
        meilleure_fitness_generation = max(fitness_population)
        meilleur_circuit_generation = population[fitness_population.index(meilleure_fitness_generation)]
        
        if meilleure_fitness_generation > meilleure_fitness:
            meilleur_circuit = meilleur_circuit_generation
            meilleure_fitness = meilleure_fitness_generation
            nb_generations_sans_amelioration_actuel = 0
        else:
            nb_generations_sans_amelioration_actuel += 1

        # Condition d'arrêt
        if generation == nb_generations_max - 1 or \
           nb_generations_sans_amelioration_actuel >= nb_generations_sans_amelioration_max:
            break
        
        print()
        
    return meilleur_circuit

##################################################################################################
def circuits():
    bouton.config(state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable
    grph.config(state = tkinter.ACTIVE)

    n = int(nbVilles.get())
    matrice_distances = genererMatriceDistances(n)
    taille_population = 10
    pourcentage_sans_amelioration = 0.1
    nb_generations_max = int(n+n*0.25)
    algoG = algorithme_génétique(n, taille_population, matrice_distances, pourcentage_sans_amelioration, nb_generations_max)

    print(algoG)
##################################################################################################
def graphe(circuit):
    grph.config(state = tkinter.DISABLED)

    G = nx.DiGraph() # Création d'un graphe orienté
    for v in circuit:
        G.add_node(v) # Ajouter les villes en tant que nœuds
        
    for i in range (len(circuit)-1):
        G.add_edge(circuit[i], circuit[i+1])
    G.add_edge(circuit[len(circuit)-1], circuit[0])
    
    plt.figure(f"Graphe du circuit à {nbVilles.get()} villes", figsize=(8, 5))
    pos = nx.spring_layout(G, k=0.3) # Disposition des nœuds
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_weight='bold', arrowsize=16, arrows=True)
    plt.show() # Afficher le graphe

################################################# AFFICHAGE #################################################
fenetre = tkinter.Tk()
fenetre.title("Affichage du graphe")
fenetre.configure(pady=10)
    
txt = tkinter.Label(text = "Nombre de villes :")
txt.grid(column = 0, row = 0)
    
nbVilles = tkinter.Entry(justify=CENTER, width=5)
nbVilles.grid(column = 1, row = 0)
    
bouton = tkinter.Button(text = "GO!", activebackground="green", activeforeground="white")
bouton.grid(column = 4, row = 0)
bouton.config(command = circuits, state = tkinter.DISABLED) # pr lancer notre fonction quand le button est pressé

valid = tkinter.Button(text = "Valider", activebackground="green", activeforeground="white")
valid.grid(column = 3, row = 0)
valid.config(command = entryValid)

grph = tkinter.Button(text = "Afficher le graphe", activebackground="purple", activeforeground="white")
grph.grid(column = 5, row = 0)
# grph.config(command = algorithme_génétique, state = tkinter.DISABLED) # Pour lancer notre fonction quand le button est pressé

fenetre.mainloop()
