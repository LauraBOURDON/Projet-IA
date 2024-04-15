#import time
#import networkx as nx
#import matplotlib.pyplot as plt

############################################## Valider l'entrée
"""def entryValid(villes):
    print("entryValid lancée")
    if villes.isdigit() and len(villes) <= 3:
        print("à true")
        return True
    return False"""

"""valid = tkinter.Button(text = "Valider")
    valid.grid(column = 3, row = 0)
    valid.config(command = entryValid(villes))"""
"""if valid:
        nbVilles.delete (0, len(nbVilles.get()))
        if not villes.isdigit() or len(villes) <= 3:
            print("False")
        else:
            print("good")"""
            
    #if entryValid(villes):
        #print("YEP")
    #if not nb:
        #print("Vous n'avez pas tapé de nombre")
        
    #nb = villes.isdigit()
    #time.sleep(10)


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