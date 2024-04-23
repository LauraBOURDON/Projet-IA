import tkinter
from tkinter import *
import random
import networkx as nx
import matplotlib.pyplot as plt

# Liste des noms de villes
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
# Fonction pour afficher une matrice carrée
def afficherMatriceCarree(matrice):
    n = len(matrice)
    max_len = max(len(str(matrice[i][j])) for i in range(n) for j in range(n))
    format_str = "{:" + str(max_len) + "}"
    for i in range(n):
        ligne = [format_str.format(matrice[i][j]) for j in range(n)]
        print(" ".join(ligne))

##################################################################################################
# Fonction pour générer une matrice de distances aléatoires entre les villes
def genererMatriceDistances(n):
    # Matrice nxn avec les valeurs initialisés à 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # On leur attribut une valeur aléatoire entre 1 à 100
            distance = random.randint(1, 100)
            matrice[i][j] = distance
            matrice[j][i] = distance
    return matrice

##################################################################################################
# Fonction pour calculer la distance totale d'un circuit
def distance_totale(circuit, matrice_distances):
    # On initialise la valeur initiale à 0
    distance_totale = 0
    #On va
    for i in range(len(circuit)):
        ville1 = circuit[i]
        if i == len(circuit) - 1:
            ville2 = circuit[0]  # Retour à la ville de départ
        else:
            ville2 = circuit[i + 1]
        distance_totale += matrice_distances[ListeVilles.index(ville1)][ListeVilles.index(ville2)]
    return distance_totale

##################################################################################################
# Fonction pour générer une population initiale de circuits aléatoires
def generer_population_initiale(n, taille_population):
    population = []
    # Mélange les villes pour avoir des villes aléatoires
    random.shuffle(ListeVilles)
    for i in range(taille_population):
        circuit = [ListeVilles[j] for j in range(n)]
        random.shuffle(circuit)
        population.append(circuit)
    return population

##################################################################################################
# Fonction pour effectuer un croisement par ordre (Order Crossover) entre deux circuits
def croisement(circuit1, circuit2):
    # taille identique aux parents
    taille = len(circuit1)
    
    # Choisir un point de coupure aléatoire
    point_coupure = random.randint(1, taille - 1) # 1 et -1 sinon on ne peut pas couper
    
    # Créer les deux nouveaux circuits enfants qui sont hamiltoniens et sont le croisement entre les parents
    nouveau_circuit1 = []
    for i in range(point_coupure):
        nouveau_circuit1.append(circuit1[i])
    for ville in circuit2:
        if ville not in nouveau_circuit1:
            nouveau_circuit1.append(ville)
    
    nouveau_circuit2 = []
    for i in range(point_coupure):
        nouveau_circuit2.append(circuit2[i])
    for ville in circuit1:
        if ville not in nouveau_circuit2:
            nouveau_circuit2.append(ville)
    
    return nouveau_circuit1, nouveau_circuit2

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
# Fonction pour calculer le fitness d'un circuit
def calculer_fitness(circuit, matrice_distances):
    distanceTotale = distance_totale(circuit, matrice_distances)
    if distanceTotale == 0:
        return float('inf')  # Éviter la division par 0
    else:
        return 1 / distanceTotale

##################################################################################################
# Fonction qui selectionne les 4 meilleurs circuits en fonction du fitness
def selection_par_tri(population, fitness_population):
    # Trier la population par ordre croissant de fitness
    population_triee = sorted(zip(population, fitness_population))
    # Sélectionner les 4 meilleurs circuits
    parents = [circuit for circuit, _ in population_triee[:4]]
    return parents

##################################################################################################
# Fonction principale de l'algorithme génétique
def algorithme_genetique(n, distance_matrice, taille_population, nb_generations):
    # Générer la population initiale
    population = generer_population_initiale(n, taille_population)

    # Calculer le fitness de chaque circuit de la population
    fitness_population = [calculer_fitness(circuit, distance_matrice) for circuit in population]

    # Garder trace du meilleur circuit et du nombre de générations sans amélioration
    meilleur_circuit = population[fitness_population.index(max(fitness_population))]
    meilleures_generations_sans_amelioration = 0

    # Boucle principale de l'algorithme génétique
    for generation in range(nb_generations):
        print(f"Génération {generation+1}")
        # On selectionne les 4 meilleurs circuits (parents)
        nouvelle_population = []
        parents = selection_par_tri(population, fitness_population)

        # On crée la nouvelle population en croisant et mutant les parents
        while len(nouvelle_population) < len(population):
            # Croiser et muter les deux parents
            parent1, parent2 = random.sample(parents, 2)
            nouveau_circuit1, nouveau_circuit2 = croisement(parent1, parent2)
            nouveau_circuit1 = mutation(nouveau_circuit1)
            nouveau_circuit2 = mutation(nouveau_circuit2)

            # Ajouter les deux nouveaux circuits à la nouvelle population
            nouvelle_population.append(nouveau_circuit1)
            nouvelle_population.append(nouveau_circuit2)

        # Remplacer l'ancienne population par la nouvelle
        population = nouvelle_population
        fitness_population = [calculer_fitness(circuit, distance_matrice) for circuit in population]

        # Mettre à jour le meilleur circuit et le nombre de générations sans amélioration
        nouveau_meilleur_circuit = population[fitness_population.index(max(fitness_population))]
        if nouveau_meilleur_circuit == meilleur_circuit:
            meilleures_generations_sans_amelioration += 1
        else:
            meilleur_circuit = nouveau_meilleur_circuit
            meilleures_generations_sans_amelioration = 0

        # Vérifier le critère d'arrêt
        if meilleures_generations_sans_amelioration >= 5:
            print("Arrêt de l'algorithme génétique : le meilleur circuit n'a pas été amélioré depuis 5 générations.")
            break
        print(distance_totale(meilleur_circuit, distance_matrice))

    return meilleur_circuit

##################################################################################################
def circuits():
    bouton.config(state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable
    grph.config(state = tkinter.ACTIVE)

    n = int(nbVilles.get())
    matrice_distances = genererMatriceDistances(n)
    taille_population = 10 # nombre de circuit
    nb_generations = 100
    
    print("--------------------------------------------------------------------------------------")
    print("\n")
    afficherMatriceCarree(matrice_distances)
    print("\n")
    print("--------------------------------------------------------------------------------------")

    algorithme_genetique(n,matrice_distances,taille_population,nb_generations)


##################################################################################################
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
