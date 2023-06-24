import json
from urllib.request import urlopen
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from functools import partial

class Aplicacion():
    __ventana = None
    __precioPeso = None
    __dolar = None
    def __init__(self):
        super().__init__()
        self.__ventana = Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.configure(bg="black")
        self.__ventana.title("Calculo de IVA")
        mainframe = ttk.Frame(self.__ventana, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N,E,W,S))   
        mainframe["borderwidth"]=2
        mainframe["relief"]="sunken"
        self.__dolar = StringVar()
        self.__precioPeso = StringVar()
        url ='https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen (url)
        data = json.loads(response.read())
        for d in data:
            if d['casa']['nombre'] == 'Oficial':
                precioDolar = d['casa']['compra']
                dolar = float(precioDolar.replace(',','.'))
        self.__dolar.trace('w', partial(self.calcular, dolar))
        ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=N)
        self.dolar = ttk.Entry(mainframe, width=10, textvariable=self.__dolar)
        self.dolar.grid(column=2, row=1, sticky=N)
        self.pesos = ttk.Label(mainframe, textvariable=self.__precioPeso).grid(column=2, row=2, sticky=N)
        ttk.Label(mainframe, text="es equivalente a ").grid(column=1, row=2, sticky=N)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=N)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(column=3, row=3, sticky=N)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=6, pady=6)
        self.__ventana.mainloop()

    def calcular (self, dolar, *args):
        if self.dolar.get() != '':
            try:
                valor = float (self.dolar.get())
                self.__precioPeso.set(f"{dolar*valor:.2f}") 
            except ValueError:
                messagebox.showerror(title='Error', message='Ingrese un valor valido')
                self.__precioPeso.set('')



def testApp():
    a = Aplicacion()
if __name__=="__main__":
    testApp()