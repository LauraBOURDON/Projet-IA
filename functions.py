import tkinter
from tkinter import *

def entryValid():
    var = False
    print("entryValid lancée")
    if len(nbVilles.get())>0 and len(nbVilles.get())<=2 and (nbVilles.get())!="0" and (nbVilles.get()).isdigit():
        if int(nbVilles.get())<=50:
            print(f"Vous avez choisi {nbVilles.get()} villes")
            var = True
    if var == False:
        print("Le nombre de villes doit être compris entre 1 et 50")
        bouton.config(state = tkinter.DISABLED)
    else:
        bouton.config(state = tkinter.ACTIVE)
    
def graphe():
    villes = int(nbVilles.get())
    print("fonction graphe lancée")
    bouton.config(state = tkinter.DISABLED) # -> bouton grisé = bouton non cliquable
    print(f"{villes}")
    result = 3 + villes
    print(f"{result}")
        
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
   