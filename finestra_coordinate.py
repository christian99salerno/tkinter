from tkinter import *
from tkinter import ttk
from punto import *




class MyWin(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Distanza")

        self.mainframe=ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(N,S,E,W))

        self.x = StringVar()
        self.y = StringVar()
        self.risultato = StringVar()
        self.risultato.set("0")

        ttk.Label(self.mainframe, text="X:").grid(column=0, row=0, sticky=(E,))
        self.coordinate_entry = ttk.Entry(self.mainframe, textvariable=self.x)
        self.coordinate_entry.grid(column=1, row=0, sticky=(W,))

        ttk.Label(self.mainframe, text="Y:").grid(column=0, row=1, sticky=(E,))
        self.coordinate_entry = ttk.Entry(self.mainframe, textvariable=self.y)
        self.coordinate_entry.grid(column=1, row=1, sticky=(W,))

        ttk.Button(self.mainframe, text="Calcola Distanza", command=self.distanza).grid(column=1, row=2, sticky=(W,))

        ttk.Label(self.mainframe, textvariable=self.risultato).grid(column=1, row=3, sticky=(W,))

    def distanza(self):
        p = Punto(float(self.x.get()),float(self.y.get()))
        self.risultato.set(p.calcolo_origine_punto())
    
    def start(self):
        self.mainloop()

root = MyWin()
root.start()

