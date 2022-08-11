from tkinter import ttk
from tkinter import *
import os

def past():
    endr = str(enderc.get())
    nome = mtr.get()
    senha = pssw.get()
    os.system('start net use')
    os.system('C:/Windows/System32/net.exe use \\\\%s /u:tjce-dom-01\%s %s' % (endr, nome, senha))
    os.system('start cmdkey /add:%s /user:tjce-dom-01\%s /pass:%s' % (endr, nome, senha))
    os.system('start \\\\%s' % (endr))
    exit()


root = Tk()
root.title('PASTA DE REDE')
root.geometry('250x200')

listEndrc=["tj.ce.gov.br\\tjce","10.1.2.60","tjce-sai-01","10.1.1.10"]

label1 = Label(root,text = "Endereço")
label1.pack()

enderc=ttk.Combobox(root,values=listEndrc)
enderc.set("10.1.1.10")
enderc.pack()

label2 = Label(root,text = "Matricula").pack()
mtr = Entry(root)
mtr.pack()


label3 = Label(root,text = "Senha").pack()
pssw = Entry(root, show='*')
pssw.pack()

buton = Button(root, text="Iniciar", command= past)
buton.pack()


root.mainloop()
