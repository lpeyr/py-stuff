import csv
import tkinter as Tk
from tkinter import messagebox


class Fenetre(Tk.Tk):
    def lecture_data(self, nom_fichier):
        """
        Charge le fichier dans un dictionnaire et le stocke dans l’attribut dico.
        :parametres: nom_fichier : chemin du fichier a charger.
        :return:
        """
        with open(nom_fichier, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            self.dico = {}
            for ligne in reader:
                ident, nom, age = ligne
                if ident not in self.dico:
                    self.dico[ident] = [nom, int(age)]

    def age_min_max(self):
        age_min = self.dico["0"][1]
        age_max = self.dico["0"][1]

        for v in self.dico.values():
            if v[1] < age_min:
                age_min = v[1]
            if v[1] > age_max:
                age_max = v[1]

        return (age_min, age_max)

    def messageBox1(self):
        messagebox.showinfo("Titre de la box", "Ouverture d'une messagebox")

    def affiche_selon_seuil(self):
        seuil = self.valeur_seuil.get()
        # parcours de la liste a ecrire
        for nom, age in self.dico.values():
            if age <= seuil:
                texte = f"=> {nom} âgé de {age} ans\n"
                self.text_area.insert(Tk.INSERT, texte)

    def affiche_age_moyen(self):
        m = 0
        for v in self.dico.values():
            m += v[1]
        self.text_area.insert(Tk.INSERT, f"=> Age moyen : {m/len(self.dico):.2f} ans\n")

    def quitter(self):
        self.destroy()

    def execute_choix(self):
        if self.choix.get() == "Message":  # cochage du radiobutton radio1
            self.text_area.insert(Tk.INSERT, "Je viens de cocher le choix 1\n")
        elif self.choix.get() == "Liste":  # cochage du radiobutton radio2
            for val in self.dico.values():
                self.text_area.insert(Tk.INSERT, val[0] + "\n")
        else:
            self.text_area.delete(1.0, Tk.END)

    def __init__(self):
        self.lecture_data("test.csv")
        bornes = self.age_min_max()
        super().__init__()
        self.geometry("500x350")
        self.title("Fenetre pour s'échauffer")
        self.resizable(False, False)
        Tk.Button(
            text="Cliquez pour ouvrir une MessageBox", command=self.messageBox1
        ).pack(fill="x")
        Tk.Button(text="Quitter l'application", command=self.quitter).pack(
            side="bottom", fill="x"
        )
        self.valeur_seuil = Tk.DoubleVar()
        self.text_area = Tk.scrolledtext.ScrolledText(
            self, wrap=Tk.WORD, width=40, height=15
        )
        self.text_area.pack(side="left")
        self.text_area.insert(Tk.INSERT, "*** Zone de texte pour infos ***\n")
        Tk.Button(text="Afficher âge moyen", command=self.affiche_age_moyen).pack()
        Tk.Label(text="Seuil à choisir").pack()
        self.scale = Tk.Scale(
            self,
            orient="horizontal",
            from_=bornes[0],
            to=bornes[1],
            tickinterval=25,
            resolution=1,
            variable=self.valeur_seuil,
        )
        self.scale.pack(fill="x")
        Tk.Button(text="Afficher selon seuil", command=self.affiche_selon_seuil).pack()

        # Creation d’une etiquette, de 3 radioButtons et d’un bouton
        self.select = Tk.Label(self, text="Radiobuttons :", font="Helvetica 10 bold")
        self.select.pack(anchor=Tk.W)
        self.choix = Tk.StringVar()  # Variable commune aux 3 RadioButtons
        self.choix.set("Message")
        self.radio1 = Tk.Radiobutton(
            self, text="Message simple", variable=self.choix, value="Message"
        )
        self.radio1.pack(anchor=Tk.W)
        self.radio2 = Tk.Radiobutton(
            self, text="Lister les noms", variable=self.choix, value="Liste"
        )
        self.radio2.pack(anchor=Tk.W)
        self.radio3 = Tk.Radiobutton(
            self, text="Effacer ScrolledText", variable=self.choix, value="Effacer"
        )
        self.radio3.pack(anchor=Tk.W)
        self.bouton_6 = Tk.Button(self, text="Choix", command=self.execute_choix)
        self.bouton_6.pack()


f = Fenetre()
f.mainloop()
