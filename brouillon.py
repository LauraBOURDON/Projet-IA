#import time
import networkx as nx
import matplotlib.pyplot as plt
#import random

circuit1 = ["oups", "gros","h","saperlipopette", "Bjr", "love"]
circuit2 = ["Bjr", "Cc", "Da","bitch", "gros","oups"]
nbVilles= 3

############################################## 

def graphe(c):
    """pr appuyer sur bouton apres le go et refaire plusieurs fois si on veut"""

    # Création d'un graphe orienté
    G = nx.DiGraph()  
    # Ajouter les tâches en tant que nœuds
    for v in c:
        G.add_node(v)
    for i in range (len(c)-1):
        G.add_edge(c[i], c[i+1])
    G.add_edge(c[len(c)-1], c[0])
    
    # vraie ver : plt.figure(f"Graphe du circuit à {nbVilles.get()} villes", figsize=(8, 5))
    plt.figure(f"Graphe du circuit à {nbVilles} villes", figsize=(8, 5))
    # Calculer la disposition des nœuds
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_color='blue', node_size=1000, font_size=10, font_weight='bold', arrowsize=16, arrows=True)
    # Afficher le graphe
    plt.show()
        
graphe(circuit2)      
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