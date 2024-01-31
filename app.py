import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# from tkcalendar import Calendar
from datetime import datetime

# root window
root = tk.Tk()
root.geometry("854x480")
root.resizable(False, False)
root.title('Registro de pedidos')

# store email address and password
pedido = tk.StringVar()
preco = tk.IntVar()
quantidade = tk.IntVar()


def registrar():
    """ callback when the login button clicked
    """

    _pedido = pedido.get()
    _preco = preco.get()
    __quantidade = quantidade.get()
    info = []
    info.append([_pedido, _preco, __quantidade])

    msg = (
        f'- Pedido: {pedido.get()} \n'
        f'- Preço: {preco.get()} \n'
        f'- Quantidade: {quantidade.get()} \n'
    )
    showinfo(
        title='Information',
        message=msg
    )
    
    date = datetime.now()
    dateOnly = date.date()
    print(dateOnly)
    print(info)


# def abrir_calendario():
#     calendario = Calendar(form, fg="gray75", bg="blue", font=("Times", "9", "bold"), locale="pt_br")
#     calendario.grid(row=1, column=1)

#     select_button = ttk.Button(text="Selecionar")
#     select_button.grid(row=1, column=2)



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

quantidade_entry = ttk.Entry(form, textvariable=quantidade)
quantidade_entry.grid(row=0, column=4,  padx=5)

# preco button
preco_label = ttk.Label(form, text="Preço:")
preco_label.grid(row=0, column=6)

preco_entry = ttk.Entry(form, textvariable=preco)
preco_entry.grid(row=0, column=7, padx=5)


# calendario button
# calendario_button = ttk.Button(form, text="Selecionar Data: ", command=abrir_calendario)
# calendario_button.grid(row=0, column=9)

# calendario_entry = ttk.Entry(form, width=10)
# calendario_entry.grid(row=0, column=10, padx=10)



# login button
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


root.mainloop()