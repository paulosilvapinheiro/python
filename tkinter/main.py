import tkinter as tk
from tkinter import messagebox
import subprocess as sp
import os
# import win32api

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

main = tk.Tk()

# Define a function to show the popup message
def show_msg():
   valueA = int(txt_valorA.get())
   valueB = int(txt_valorB.get())
   result = valueA + valueB
   messagebox.showinfo("Message","Hey There! I hope you are doing well.\nO valor da soma de A + B é :{0}".format(result))

def get_exec():
   # sp.run("C:\Program Files\SASHome\SASEnterpriseGuide\8\SEGuide.exe")
   explore("C:\\Users\\331675\\OneDrive - Natura Cosméticos\\02-Areas\\Credito\\01-Atividades Bau\\02-Aumento semanal\\GESTAO_LIMITES_REVISAO_202300404-v8-3.egp")

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        sp.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        sp.run([FILEBROWSER_PATH, '/enter,', os.path.normpath(path)])

def posicionarItem(item, posicaoHorizontal, posicaoVertical,pularLinha):
    item.place(x=posicaoHorizontal,y=posicaoVertical)
    if pularLinha == True :
        posicaoVertical = posicaoVertical + 20
    return posicaoVertical

main.geometry("800x400")
main.title("Soma")

lbl_ValorA = tk.Label(text="Valor A:")
posicaoVertical = posicionarItem(lbl_ValorA,10,10,False)

txt_valorA = tk.Entry()
posicaoVertical = posicionarItem(txt_valorA,65,posicaoVertical,True)

lbl_ValorB = tk.Label(text="Valor B:")
posicaoVertical = posicionarItem(lbl_ValorB,10,posicaoVertical,False)

txt_valorB = tk.Entry()
posicaoVertical = posicionarItem(txt_valorB,65,posicaoVertical,True)

btn_Calc = tk.Button(text="SOMAR",command=show_msg)
btn_Calc.place(x=10,y=50)

btn_Exec = tk.Button(text="Chamar executavel",command=get_exec)
btn_Exec.place(x=10,y=100)

main.mainloop()