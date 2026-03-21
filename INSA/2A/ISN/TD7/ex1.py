import tkinter as Tk


class Fenetre(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x450")
        self.title("Fenetre pour s'échauffer")

        b1 = Tk.Button(text="Bouton du haut")
        b1.pack(side="top")

        frame = Tk.Frame(self)
        frame.pack(side="top")
        right_frame = Tk.Frame(frame)
        right_frame.pack(side="right")
        Tk.Label(
            frame, text="Un gros label", background="lightblue", height=15, width=50
        ).pack(side="left")
        Tk.Label(right_frame, text="Un label").pack()
        Tk.Button(right_frame, text="Bouton de droite 1").pack()
        Tk.Button(right_frame, text="Bouton de droite 2").pack()

        Tk.Button(self, text="quitter", command=self.quitter).pack(side="bottom")

    def quitter(self):
        self.destroy()


f = Fenetre()
f.mainloop()
