import tkinter
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *

def affichage():
    fenetre = tkinter.Tk()
    fenetre.title("Affichage du graphe")
    fenetre.minsize(width=350, height=275)
    fenetre.configure(pady=10)
    
    txt = tkinter.Label(text = "Nombre de villes :")
    txt.grid(column = 0, row = 0)
    
    nbVilles = tkinter.Entry(justify=CENTER, width=5)
    # faut vérifier les entrées pr que ce soit vrm un nbr et qu'il soit entre valMin et valMax
    """nb = villes.isdigit()
    villes = nbVilles.get() # recuperer le texte ecrit au clavier dans la case
    if not nb:
        print("Vous n'avez pas tapé de nombre")"""
    nbVilles.grid(column = 1, row = 0)
    
    bouton = tkinter.Button(text = "GO!")
    bouton.grid(column = 3, row = 0)
    bouton.config(command = graphe) # pr lancer notre fonction quand le button est pressé
    #bouton.config (state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable, voir comment on peut l'activer apres lancement de la fonction par GO!
    
    fenetre.mainloop()
    
    
def graphe():
    print("fonction graphe lancée") 
affichage()

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