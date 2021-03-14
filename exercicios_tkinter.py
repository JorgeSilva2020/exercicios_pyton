from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Meu Primeiro APP")
menu_inicial.geometry("500x300")
# menu_inicial.mainloop()

def cmd_Click(mensagem):
    print(mensagem)
# Botão
cmd= Button(menu_inicial, text="Executar", command=lambda:cmd_Click("Mensagem 1"))

cmd.pack()
cmd= Button(menu_inicial, text="Clicar", command=lambda:cmd_Click("Mensagem 2"))

cmd.pack()

menu_inicial.mainloop()