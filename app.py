import tkinter as tk
from tkinter import ttk
from datetime import datetime
from sql import *
from tkinter.messagebox import showinfo

##### janela principal
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
id_list = []

for row in response:
    id, produto, quantidade, preco, data = row
    id_list.append(id)
    pedido_list.append(produto)
    quantidade_list.append(quantidade)
    preco_list.append(preco)
    data_list.append(data)

##### funções
def registrar():
    _pedido = pedido.get()
    _preco = price.get()
    _quantidade = qtd.get()
    data = datetime.now()
    data_apenas = data.date()

    inserirPedido(_pedido, _quantidade, _preco, data_apenas)

    showinfo(
        title="",
        message="Pedido registrado com sucesso!"
    )

    pedido.set("")
    price.set("")
    qtd.set("")
    
def atualizarTabela():
    root.update()
    root.update_idletasks() # não está funcionando

    

##### sessão do formulário
form = ttk.Frame(root)
form.pack(padx=10, pady=10, fill='x')

##### pedido
pedido_label = ttk.Label(form, text="Pedido:")
pedido_label.grid(row=0, column=0)

pedido_entry = ttk.Entry(form, textvariable=pedido)
pedido_entry.grid(row=0, column=1,  padx=5)
pedido_entry.focus()

##### quantidade
quantidade_label = ttk.Label(form, text="Quantidade:")
quantidade_label.grid(row=0, column=3)

quantidade_entry = ttk.Entry(form, textvariable=qtd)
quantidade_entry.grid(row=0, column=4,  padx=5)

##### botão preço
price_label = ttk.Label(form, text="Preço:")
price_label.grid(row=0, column=6)

price_entry = ttk.Entry(form, textvariable=price)
price_entry.grid(row=0, column=7, padx=5)

##### botão registrar
registrar_button = ttk.Button(form, text="Registrar", command=registrar)
registrar_button.grid(row=0, column=11, pady=10)

##### tabela de entrada de pedidos
tabela = ttk.Frame(root)
tabela.pack(padx=10, pady=10, fill='x')
tree = ttk.Treeview(tabela)

tree["columns"] = ("pedido", "preco", "quantidade", "data-entrada")

##### Formantando as colunas
tree.column("#0", width=70, minwidth=70, anchor="center") # Anchor --> Posicionamento do texto
tree.column("pedido", width=120, minwidth=120, anchor="center")
tree.column("quantidade", width=120, minwidth=120, anchor="center")
tree.column("preco", width=120, minwidth=120, anchor="center")
tree.column("data-entrada", width=120, minwidth=120, anchor="center")

##### Definindo os cabeçalhos das colunas
tree.heading("#0", text="ID")
tree.heading("pedido", text="PEDIDO")
tree.heading("quantidade", text="QTD")
tree.heading("preco", text="PREÇO")
tree.heading("data-entrada", text="ENTRADA")

for i in range(len(pedido_list)):
    tree.insert("", tk.END, text=f"{id_list[i]}", values=(f"{pedido_list[i]}, {preco_list[i]: .2f}, {quantidade_list[i]}, {data_list[i]}"))

tree.pack(fill='x')


campo_atualizar = ttk.Frame(root)
campo_atualizar.pack(padx=10, pady=10, fill='x')

btn_atualizar = ttk.Button(campo_atualizar, text="Atualizar tabela", command=atualizarTabela)
btn_atualizar.grid(row=0, column=1, pady=5)

root.mainloop()


