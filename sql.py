import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_restaurante.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'pedidos'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = (
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'produto TEXT, '
        'quantidade INTEGER, '
        'preco NUMERIC, '
        'data TEXT'
    ')'
)

cursor.execute(sql)
connection.commit()


def inserirPedido(produto, quantidade, preco, data):
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(produto, quantidade, preco, data) '
        'VALUES '
        f'("{produto}", "{quantidade}", "{preco}", "{data}")'
    )
    
    cursor.execute(sql)
    connection.commit()




def mostrarDados():
    sql = (
        f'SELECT * FROM {TABLE_NAME}'
    )

    cursor.execute(sql)
    connection.commit()

    response = cursor.fetchall()
    return response

