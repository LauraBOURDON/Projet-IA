import random

# Listes des noms de villes
ListeVilles = ["Paris", "Bordeaux", "Rouen", "Toulon", "Brest", "Saint-Hilaire", "Viry-Châtillon", "Cesson", "Strasbourg", "Melun"]

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

# Fonction pour générer une matrice de distances aléatoires entre les villes
def genererMatriceDistances(n):
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(1, 100)
            matrice[i][j] = distance
            matrice[j][i] = distance
    return matrice

# Fonction pour générer une liste de n villes aléatoires
def genererVilles(n):
    villes = []
    for _ in range(n):
        nom = genererNomVille()
        villes.append(nom)
    return villes

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

# Fonction pour afficher une matrice carrée
def afficherMatriceCarree(matrice):
    n = len(matrice)
    max_len = max(len(str(matrice[i][j])) for i in range(n) for j in range(n))
    format_str = "{:" + str(max_len) + "}"
    for i in range(n):
        ligne = [format_str.format(matrice[i][j]) for j in range(n)]
        print(" ".join(ligne))

# Fonction pour générer une population initiale de circuits aléatoires
def generer_population_initiale(n, taille_population):
    population = []
    for i in range(taille_population):
        circuit = list(range(n))
        random.shuffle(circuit)
        population.append(circuit)
    return population

n = int(input("Entrez le nombre de villes: "))
villes = genererVilles(n)
matrice_distances = genererMatriceDistances(n)
circuit = list(range(n))
random.shuffle(circuit)
taille_population = 10 # nombre de circuit
distance = distance_totale(circuit, matrice_distances)

print("Distance totale du circuit initial :", distance)
print("Circuit :", [villes[i] for i in circuit])
afficherMatriceCarree(genererMatriceDistances(n))

population = generer_population_initiale(n, taille_population)
for i, circuit in enumerate(population):
    distance = distance_totale(circuit, matrice_distances)
    print(f"Circuit {i+1} (distance = {distance}) : {[villes[j] for j in circuit]}")