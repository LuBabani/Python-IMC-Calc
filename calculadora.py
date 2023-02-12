from tkinter import *
root =Tk()

class App():
    def __init__(self):
        self.root = root
        self.config()
        self.calculadora()
        root.mainloop()

   # Calc Frame
    def config(self):
        self.root.title("Calculadora de IMC da Lu")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

      # Data Entry
    def calculadora(self):
        self.lbl1 = Label(text='Digite o seu peso: ',background="Pink")
        self.lbl1.place(relx=0.15,rely=0.1)
        self.numero1 = DoubleVar()
        self.lbl1_enty = Entry(textvariable=self.numero1)
        self.lbl1_enty.place(relx=0.45,rely=0.1)
        self.lbl2 = Label(text='Digite a sua altura: ', background="Pink")
        self.lbl2.place(relx=0.15, rely=0.25)
        self.numero2 = DoubleVar()
        self.lbl2_enty = Entry(textvariable=self.numero2)
        self.lbl2_enty.place(relx=0.45, rely=0.25)

      # Result IMC
        self.lbl3 = Label(text='Resultado do IMC é:', background="pink")
        self.lbl3.place(relx=0.15, rely=0.6)
        self.resultado = StringVar()
        self.l_resultado = Label(textvariable=self.resultado, font=("Roboto", '8'))
        self.l_resultado.place(relx=0.5, rely=0.6)

         
      # Button
        self.btn1 = Button(text='Calcular',command=self.soma)
        self.btn1.place(relx=0.65, rely=0.4)
        

    def soma(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        resul = num1 / (num2**2)
        self.resultado.set(resul)


App()