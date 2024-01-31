import tkinter as tk
from tkinter import ttk
from datetime import datetime
from sql import *

# janela principal
root = tk.Tk()
root.geometry("854x480")
root.resizable(False, False)
root.title('Registro de pedidos')

pedido = tk.StringVar()
price = tk.IntVar()
qtd = tk.IntVar()

response = mostrarDados()
pedido_list = []
quantidade_list = []
preco_list = []
data_list = []

for row in response:
    _, produto, quantidade, preco, data = row
    pedido_list.append(produto)
    quantidade_list.append(quantidade)
    preco_list.append(preco)
    data_list.append(data)


def registrar():
 
    _pedido = pedido.get()
    _preco = price.get()
    _quantidade = qtd.get()
    data = datetime.now()
    data_apenas = data.date()

    inserirPedido(_pedido, _quantidade, _preco, data_apenas)



# sessão do formulário
form = ttk.Frame(root)
form.pack(padx=10, pady=10, fill='x')

# pedido
pedido_label = ttk.Label(form, text="Pedido:")
pedido_label.grid(row=0, column=0)

pedido_entry = ttk.Entry(form, textvariable=pedido)
pedido_entry.grid(row=0, column=1,  padx=5)
pedido_entry.focus()

# quantidade
quantidade_label = ttk.Label(form, text="Quantidade:")
quantidade_label.grid(row=0, column=3)

quantidade_entry = ttk.Entry(form, textvariable=qtd)
quantidade_entry.grid(row=0, column=4,  padx=5)

# botão preço
price_label = ttk.Label(form, text="Preço:")
price_label.grid(row=0, column=6)

price_entry = ttk.Entry(form, textvariable=price)
price_entry.grid(row=0, column=7, padx=5)

# botão registrar
registrar_button = ttk.Button(form, text="Registrar", command=registrar)
registrar_button.grid(row=0, column=11, pady=10)

# tabela de entrada de pedidos
tabela = ttk.Frame(root)
tabela.pack(padx=10, pady=10, fill='x')
tree = ttk.Treeview(tabela)

tree["columns"] = ("pedido", "preco", "quantidade", "data-entrada")

#Formantando as colunas
tree.column("#0", width=70, minwidth=70) # Anchor --> Posicionamento do texto
tree.column("pedido", width=120, minwidth=120)
tree.column("preco", width=120, minwidth=120)
tree.column("quantidade", width=120, minwidth=120)
tree.column("data-entrada", width=120, minwidth=120)

#Definindo os cabeçalhos das colunas
tree.heading("#0", text="ID")
tree.heading("pedido", text="PEDIDO")
tree.heading("preco", text="PREÇO")
tree.heading("quantidade", text="QTD")
tree.heading("data-entrada", text="ENTRADA")

tree.pack(fill='x')

for i in range(len(pedido_list)):
    tree.insert("", tk.END, text=f"{i}", values=(f"{pedido_list[i]}, {quantidade_list[i]}, {preco_list[i]}, {data_list[i]}"))


root.mainloop()


