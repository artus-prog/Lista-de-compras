import funçoes
import main
from tkinter import *

janela_main = Tk()
janela_main.title("Lista de compras")
texto_main = Label(janela_main, text=("Selecione a opção desejada:"))
texto_main.grid(column=(0), row=(0))
botao1 = Button(janela_main, text=("Adicionar item"), command= funçoes.adicionar_item(main.lista_compras))
botao1.grid(column=(0),row=(1))
janela_main.mainloop()