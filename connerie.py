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
    distanceTotale = 0  # Réinitialiser la distance à 0 pour chaque circuit
    for i in range(len(circuit)):
        ville1 = circuit[i]
        if i == len(circuit) - 1:
            ville2 = circuit[0]  # Retour à la ville de départ
        else:
            ville2 = circuit[i + 1]
        distanceTotale += matrice_distances[ville1][ville2]
    return distanceTotale

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
    for i in range(taille_population):
        circuit = genererVilles(n)
        random.shuffle(circuit)
    return circuit

##################################################################################################
#fonction pour échanger le début et la fin de deux circuits
def croisement(circuit1,circuit2):
    fin = len(circuit1)//2
    newCircuit1 = []
    newCircuit2 = []
    for i in range(fin):
            newCircuit1.append(circuit1[i])
            newCircuit2.append(circuit2[i])
    for i in range(fin, len(circuit1)):
        if circuit2[i] not in circuit1:
            newCircuit1.append(circuit2[i])
        if circuit1[i] not in circuit2:
            newCircuit2.append(circuit1[i])
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
    parents = [circuit for circuit, _ in population_triee[:4]]
    return parents
 
##################################################################################################
# Fonction pour muter un circuit
def mutation(circuit):
    tauxDeMutation = 0.5 # Taux de mutation afin que la mutation n'ait pas tout le temps lieu
    if random.random() < tauxDeMutation:
        # On choisit 2 villes au hasard
        ville1, ville2 = random.sample(range(len(circuit)), 2)
        # On inverse leur ordre
        circuit[ville1], circuit[ville2] = circuit[ville2], circuit[ville1]

    return circuit
##################################################################################################
def algorithme_génétique(n, taille_population, matrice_distances, pourcentage_sans_amelioration, nb_generations_max):
    # Initialisation de la population
    print("init pop marche")
    #villes = genererVilles(n)
    population = generer_population_initiale(n, taille_population)
    print(f"{population}")

    # Mémorisation du meilleur circuit trouvé
    meilleur_circuit = [] # None
    meilleure_fitness = 0
    
    print("nb g sans amelioration marche")
    nb_generations_sans_amelioration_actuel = 0
    nb_generations_sans_amelioration_max = int(nb_generations_max * pourcentage_sans_amelioration)

    print("nb generation max marche")
    for generation in range(nb_generations_max):
        # Évaluation de la fitness de chaque individu
        fitness_population = [(calculer_fitness(circuit, matrice_distances)) for circuit in population]
        print(f"fitness de la population = {fitness_population}")
            
        print("select par tri")
        # Sélection des meilleurs individus
        parents = selection_par_tri(population, fitness_population)
        print(f"tri par select : {parents}")
        
        print("new pop")
        # Croisement pour générer la nouvelle population
        nouvelle_population = []
        for c in parents:
            nouvelle_population.append(c)
            print(f"ajout parents dans new pop : {nouvelle_population}")
        
        while len(nouvelle_population) <= 8:  
            print("in the boucle new pop")
            for i in range(len(parents)-1):
                print("enf1 enf2")
                circuit1 = random.choice(parents)
                circuit2 = random.choice(parents)
                if (circuit1 != circuit2):
                    enfant1, enfant2 = croisement(circuit1, circuit2)
                    nouvelle_population.append(enfant1)
                    nouvelle_population.append(enfant2)
        print(f"ajout enfants dans new pop : {nouvelle_population}")

        print("mutation")
        # Mutation de la nouvelle population
        for i in range(len(nouvelle_population)-1):
            nouvelle_population[i] = mutation(nouvelle_population[i])

        print("pop = new pop")
        # Remplacement de la population
        population = nouvelle_population

        meilleure_fitness_generation = fitness_population[0]
        ind = 0
        #i = 1
        print(f"f = {meilleure_fitness_generation}")
        #while i < len(fitness_population):
        for i in range(len(fitness_population)-1):
            print(f"i = {i}")
            if fitness_population[i] >= meilleure_fitness_generation:
                print("on remplace")
                meilleure_fitness_generation = fitness_population[i]
                ind = i
            #i = i + 1
        print(f"{meilleure_fitness_generation}")
        print(f"pop = {population[ind]}")
        
        print("remplacer par le meilleur circuit")
        meilleur_circuit_generation = (population[ind]) #pb avec pop, jsp pk il marche pas c pr ça ind out of range
        if meilleure_fitness_generation > meilleure_fitness:
            meilleur_circuit = meilleur_circuit_generation
            meilleure_fitness = meilleure_fitness_generation
            #nb_generations_sans_amelioration_actuel = 0
        else:
            nb_generations_sans_amelioration_actuel += 1

        print("cond d'arret")
        # Condition d'arrêt
        if generation == nb_generations_max or nb_generations_sans_amelioration_actuel >= nb_generations_sans_amelioration_max:
            return meilleur_circuit

##################################################################################################
def circuits():
    bouton.config(state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable
    grph.config(state = tkinter.ACTIVE)
    
    print("circuit lancer fonctions marche")
    n = int(nbVilles.get())
    matrice_distances = genererMatriceDistances(n)
    taille_population = 10
    pourcentage_sans_amelioration = 0.1
    nb_generations_max = int(n+n*0.25)
    
    print("appel algo g marche")
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
