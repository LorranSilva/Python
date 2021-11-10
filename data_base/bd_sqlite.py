import sqlite3

conexao = sqlite3.connect('basededados.db')

#  cursor vai executar os comandos sql na base de dados
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES ("Murilo Estranho",80.5)')
conexao.commit()  # para executar op comando na base de dados

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
