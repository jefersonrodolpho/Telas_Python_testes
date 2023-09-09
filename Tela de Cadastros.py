import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão","Caixa","Pregos","Arames"]
lista_codigos = []

janela = tk.Tk()

#Criação da função para o Botão

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo) 
    lista_codigos.append((codigo_str,descricao,tipo,quantidade,data_criacao))
    

# Título da janela
janela.title("CADASTRO")

janela.geometry("600x400")

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(column=0, row=0, padx=50, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(column=0, row=1, padx=50, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do Material")
label_tipo_unidade.grid(column=0, row=2, padx=50, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(column=2, row=2, padx=50, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text="Quantidade de Material") 
label_quantidade.grid(column=0, row=3, padx=50, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(column=2, row=3, padx=50, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Criar Código", command=inserir_codigo)
botao_criar_codigo.grid(column=0, row=5, padx=50, pady=10, sticky='nswe', columnspan=6)


janela.mainloop()

print(lista_codigos)

