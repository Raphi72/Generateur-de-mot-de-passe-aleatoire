from tkinter import *
import string
from random import randint, choice
import os 


SEP = ";"    
EOL = "\n"   

d = {}
nomDuFichier = ""



def charge(nom_du_fichier):
    global nomDuFichier
    if os.path.exists(nom_du_fichier):
        nomDuFichier = nom_du_fichier
        with open(nom_du_fichier, 'r') as fichier:
            scores = fichier.readlines()
            for line in scores:
                t = line.strip().split(SEP)  
                if len(t) == 2:  
                    d[t[0]] = t[1]  
        return True
    else:
        return False

def sauve():
    with open(nomDuFichier, 'w') as fichier:
        for key, value in d.items():
            fichier.write(f"{key}{SEP}{value}{EOL}")

def lit(nom):
    return d.get(nom)

def ecrit(nom, mdp):
    d[nom] = mdp
    return True

    return modifie
def generate_mdp():
    mdpmin = 6
    mdpmax = 24
    alltxt = string.ascii_lowercase + string.punctuation + string.digits
    mdpf = "".join(choice(alltxt) for _ in range(randint(mdpmin, mdpmax)))
    mdp.delete(0, END)
    mdp.insert(0, mdpf)
  

def supp():
    mdp.delete(0, END)
    Name.delete(0, END)

def execute():
    charge("Données.txt")
    get_entry()
    if lit(contenu) is None:  
        ecrit(contenu, contenu_mdp)
        sauve()
        label_title = Label(rframe, text="Nom et MDP enregistrés", font=("Arial", 20), bg=("#4065A4"), fg=("white"))
        label_title.pack()
        window.after(3500, label_title.destroy)
    else:
        label_title = Label(rframe, text="Ce nom a déjà été utilisé", font=("Arial", 20), bg=("#4065A4"), fg=("white"))
        label_title.pack()
        window.after(3500, label_title.destroy)
    supp()
    

def get_entry():
    global contenu, contenu_mdp
    contenu = Name.get()
    contenu_mdp = mdp.get()

    

# affichage de la page et sa config 
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.maxsize(1080, 720)
window.iconbitmap("image.ico")
window.config(background="#4065A4")

frame = Frame(window, bg=("#4065A4"))


def get_entry_recherche():
    global contenu_recherche
    contenu_recherche = Search.get()

def recherche_nom():
    global result_label, contenu_recherche
    charge("Données.txt")  
    get_entry_recherche()   
    if result_label is not None:
        result_label.destroy()
    mot_de_passe = lit(contenu_recherche)
    if mot_de_passe is None:
        result_label = Label(recherche_frame, text="Ce nom n'a pas été enregistré", font=("Arial", 20), bg="#4065A4", fg="white")
        result_label.pack()  
        window.after(3500, lambda: result_label.destroy())  
    else:
        result.insert(0, mot_de_passe)  
        window.after(3500, lambda: result.delete(0, END))  

def copier_contenu():
    contenu = result.get()  # Récupère le contenu de result
    window.clipboard_clear()  # Efface le presse-papiers
    window.clipboard_append(contenu)  # Ajoute le contenu au presse-papiers
    window.update() 


def ouvrir_recherche():
    global Search, recherche_frame, result_label, result
    
    # Création de la fenêtre secondaire pour la recherche
    recherche = Toplevel(window)
    recherche.title("Recherche de mot de passe")
    recherche.geometry("720x480")
    recherche.maxsize(1080, 720)
    recherche.iconbitmap("image.ico")
    recherche.config(background="#4065A4")
    
    # Cadre pour la recherche
    recherche_frame = Frame(recherche, bg="#4065A4")
    Label(recherche_frame, text="Rechercher un mot de passe", font=("Arial", 20), bg="#4065A4", fg="white").pack(pady=20)
    
    # Champ de recherche
    Search = Entry(recherche_frame, font=("Arial", 20), bg="#4065A4", fg="white")
    Search.pack(pady=10)
    
    # Bouton de recherche
    Button(recherche_frame, text="Rechercher", font=("Arial", 20), bg="white", fg="black", command=recherche_nom).pack(pady=10)
    
    result_frame = Frame(recherche_frame, bg="#4065A4")
    result_frame.pack(pady=10)
    
    result = Entry(recherche_frame, font=("Arial", 20), bg=("#4065A4"), fg=("white"))
    result.pack()
    
    Button(result_frame, text="Copier", font=("Arial", 15), bg="green", fg="black", command=copier_contenu).pack(side="left", padx=10)
    
    # Placeholder pour le label de résultat
    result_label = None  # Sera défini lors de la recherche
    
    recherche_frame.pack(expand=YES)


# affichage de l'image_names
width = 250
height = 250
image = PhotoImage(file="pin-code.png").zoom(1)
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)


rframe= Frame(frame, bg=("#4065A4"))

#texte de la page

label_title = Label(rframe, text="Nom", font=("Arial", 20), bg=("#4065A4"), fg=("white"))
label_title.pack()

Name = Entry(rframe, font=("Arial", 20), bg=("#4065A4"), fg=("white"))
Name.pack()


label_title = Label(rframe, text="Mot de passe", font=("Arial", 20), bg=("#4065A4"), fg=("white"))
label_title.pack()

mdp = Entry(rframe, font=("Arial", 20), bg=("#4065A4"), fg=("white"))
mdp.pack()



générateur = Button(rframe, text="Générer", font=("Arial", 20), bg=("#4065A4"), fg=("white"), command=generate_mdp)
générateur.pack(fill=X)


Validation = Button(rframe, text="Valdider", font=("Arial", 20), bg=("green"), fg=("white"), command=execute)
Validation.pack(fill=X)


rframe.grid(row=0, column=1, sticky=W)


#afficher frame
frame.pack(expand=YES)


menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label="Recherche", command=ouvrir_recherche)
menu.add_cascade(label="Fonction", menu=file)
window.config(menu=menu)

# lancer la fenêtre
window.mainloop()


