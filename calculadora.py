import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.font import Font
from functools import partial
from imaginario import Imaginario
import re
class Calculadora(tk.Tk):
    __resultado=None
    def __init__(self):
        super().__init__()
        self.title('Calculadora')
        self.geometry('230x450')
        fuente=Font(size=25)
        opts = { 'ipadx': 12, 'ipady': 5 , 'sticky': 'nswe' }

        self.__resultado=tk.StringVar()
        resultado=tk.Label(self,textvariable=self.__resultado,width=7,font=fuente,borderwidth=1,relief='solid').grid(row=0,column=1,columnspan=2,sticky='E',ipadx=12,ipady=17)
        
        i=tk.Button(self, text='i', command=partial(self.ponerIMAGINARIO, 'i'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=0,**opts)
        uno=tk.Button(self, text='1', command=partial(self.ponerNUMERO, '1'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=1,**opts)
        dos=tk.Button(self, text='2', command=partial(self.ponerNUMERO, '2'),font=fuente,borderwidth=1,relief='solid').grid(column=1, row=1,**opts)
        tres=tk.Button(self, text='3', command=partial(self.ponerNUMERO, '3'),font=fuente,borderwidth=1,relief='solid').grid(column=2, row=1,**opts)
        cuatro=tk.Button(self, text='4', command=partial(self.ponerNUMERO, '4'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=2,**opts)
        cinco=tk.Button(self, text='5', command=partial(self.ponerNUMERO, '5'),font=fuente,borderwidth=1,relief='solid').grid(column=1, row=2,**opts)
        seis=tk.Button(self, text='6', command=partial(self.ponerNUMERO, '6'),font=fuente,borderwidth=1,relief='solid').grid(column=2, row=2,**opts)
        siete=tk.Button(self, text='7', command=partial(self.ponerNUMERO, '7'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=3,**opts)
        ocho=tk.Button(self, text='8', command=partial(self.ponerNUMERO, '8'),font=fuente,borderwidth=1,relief='solid').grid(column=1, row=3,**opts)
        nueve=tk.Button(self, text='9', command=partial(self.ponerNUMERO, '9'),font=fuente,borderwidth=1,relief='solid').grid(column=2, row=3,**opts)
        cero=tk.Button(self, text='0', command=partial(self.ponerNUMERO, '0'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=4,**opts)

        mas=tk.Button(self, text='+', command=partial(self.ponerOPERADOR, '+'),font=fuente,borderwidth=1,relief='solid').grid(column=1, row=4,**opts)
        menos=tk.Button(self, text='-', command=partial(self.ponerOPERADOR, '-'),font=fuente,borderwidth=1,relief='solid').grid(column=2, row=4,**opts)
        por=tk.Button(self, text='*', command=partial(self.ponerOPERADOR, '*'),font=fuente,borderwidth=1,relief='solid').grid(column=0, row=5,**opts)
        div=tk.Button(self, text='/', command=partial(self.ponerOPERADOR, '/'),font=fuente,borderwidth=1,relief='solid').grid(column=1, row=5,**opts)
        igual=tk.Button(self, text='=', command=self.calcular,font=fuente,borderwidth=1,relief='solid').grid(column=2, row=5,**opts)


    def ponerNUMERO(self,num):
        resultado=self.__resultado.get()
        resultado+=num
        self.__resultado.set(resultado)

    def ponerIMAGINARIO(self,i):
        expresion=self.__resultado.get()
        if expresion.endswith('+') or expresion.endswith('-') or expresion.endswith('*') or expresion.endswith('/'):
            messagebox.showerror(title='Error',message='Debe ser ingresado despues de un número')
        elif expresion.count('i')==2:
            messagebox.showerror(title='Error',message='No puede haber más de dos números imaginarios')
        else:
            expresion+=i
            self.__resultado.set(expresion)

    def ponerOPERADOR(self,op):
        expresion=self.__resultado.get()
        if expresion.endswith('+') or expresion.endswith('-') or expresion.endswith('*') or expresion.endswith('/'):
            messagebox.showerror(title='Error de operador',message='No puede ingresar dos operadores seguidos')
        else:
            expresion+=op
            self.__resultado.set(expresion)


    def calcular(self):
        expresion=self.__resultado.get()
        if expresion.endswith('+') or expresion.endswith('-') or expresion.endswith('*') or expresion.endswith('/'):
            messagebox.showerror(title='Error de operación',message='La expresion debe finalizar con un numero')
        else:
            operandos=re.split(r'[*-/+]',expresion)

            expresionDividida=expresion.split('i',maxsplit=1)

            operandosUno=[expresionDividida[0][0],expresionDividida[0][1:].split('i')[0]]
            operandosDos=[expresionDividida[1][1],expresionDividida[1][2:].split('i')[0]]

            operadorPrincipal=expresionDividida[1]
            operadorPrincipal=operadorPrincipal[0]

            expresion1=Imaginario(int(operandosUno[0]),int(operandosUno[1]))
            expresion2=Imaginario(int(operandosDos[0]),int(operandosDos[1]))

            if operadorPrincipal=='+':
                resultado=expresion1+expresion2
                self.__resultado.set(resultado)
            elif operadorPrincipal=='-':
                resultado=expresion1-expresion2
                self.__resultado.set(resultado)
            elif operadorPrincipal=='*':
                resultado=expresion1*expresion2
                self.__resultado.set(resultado)
            elif operadorPrincipal=='/':
                resultado=expresion1/expresion2
                self.__resultado.set(resultado)
