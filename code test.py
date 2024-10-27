from tkinter import *
import webbrowser

def page():
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

#affichage de la page et sa config 
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("image.ico")
window.config(background="green")

#creation de la frame
frame = Frame(window, bg=("green"), bd=1, relief=SUNKEN)



#texte de la page
label_title = Label(frame, text="Bienvenue sur mon logiciel de génération de mots de passe", font=("Arial", 30), bg=("green"), fg=("blue"))
label_title.pack()

label_title = Label(frame, text="Commencez!!!", font=("Arial", 20), bg=("green"), fg=("blue"))
label_title.pack()

#premier bouton
button = Button(frame, text="Générez", font=("Arial", 20), bg=("white"), fg=("black"), command=page)
button.pack()

#afficher frame
frame.pack()











window.mainloop()

