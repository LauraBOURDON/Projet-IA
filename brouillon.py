#import time
#import networkx as nx
#import matplotlib.pyplot as plt
import random

circuit1 = ["Lilles", "Alexis", "Laura", "love"]
circuit2 = ["Bjr", "Caca", "Da", "gros"]

############################################## CHAT GPT avec mes mots
def croisement(circuit1, circuit2):
    start = random.randint(0, len(circuit1)-1)
    end = random.randint(start+1, len(circuit2))
    newCircuit1 = circuit1[:start] + [c for c in circuit2 if c not in circuit1[:start]] + circuit1[end:]
    print(f"{newCircuit1}")
    newCircuit2 = circuit2[:start] + [c for c in circuit1 if c not in circuit2[:start]] + circuit2[end:]
    print(f"{newCircuit2}")
    return newCircuit1, newCircuit2
    
"""def croisement(circuit1, circuit2):
    deb = 0
    fin = len(circuit1)//2
    print(f"{deb}")
    print(f"{fin}")
    newCircuit1 = []
    for n in circuit1:
        deb = deb + 1
        if deb <= fin:
            newCircuit1.append(n)
            for i in range(len(circuit1)):
                if i > fin:
                    for n[i] in circuit2:
                        newCircuit1.append(n)
    #newCircuit2 =
    #return newCircuit1, newCircuit2
    print(f"{newCircuit1}")"""

croisement(circuit1, circuit2)

################################################### truc de sye
"""
    def draw(self):
        self.run()
        
        # Création d'un graphe orienté
        G = nx.DiGraph()
        
        # Ajouter les tâches en tant que nœuds
        for task in self.listTask:
            G.add_node(task.name)

        # Ajouter les arêtes en fonction du parallélisme maximal
        for i, task1 in enumerate(self.listTask):
            for task2 in self.listTask[i+1:]:
                if not self.checkBernstein(task1, task2):
                    G.add_edge(task1.name, task2.name)
        
        # Suppression des arêtes redondantes
        areteSuppr = []
        for task1, task2 in G.edges():
            chemins = list(nx.all_simple_paths(G, source=task1, target=task2))
            # S'il existe plus d'un chemin on l'ajoute dans areteSuppr
            if len(chemins) > 1:
                areteSuppr.append((task1, task2))
        # On supprime toutes les arrêtes dans areteSuppr qui sont les arêtes en trop
        G.remove_edges_from(areteSuppr)

        # Calculer la disposition des nœuds
        pos = nx.spring_layout(G, k=0.3)
        
        # Dessiner le graphe
        figure_name = f"Figure {TaskSystem.compteur}"
        plt.figure(figure_name, figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold', arrowsize=16, arrows=True)
        
        # Ajouter un titre
        plt.title(figure_name)
        
        # Afficher le graphe
        plt.show()
            
        # Incrémenter le compteur de figure
        TaskSystem.compteur += 1
"""