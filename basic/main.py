# Uso básico con Python
# Como ejemplo, creeemos una base de datos de citas de autores

import sqlite3

conn = sqlite3.connect('db.sqlite3')
db = conn.cursor()

# Listar tablas

tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables existentes:")
print(tables.fetchall())


result = db.execute('SELECT * FROM authors')
print(result.fetchall())
# Tabla de autor

#db.execute('CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)')

# Crear la tabla
#db.execute('CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, text TEXT, author INTEGER, FOREIGN KEY(author) REFERENCES authors(id))')

# Insertar algunos datos

db.execute('INSERT INTO authors (name) VALUES (?)', ('Fiodor Dostoievsky',))
db.execute('INSERT INTO authors (name) VALUES (?)', ('Marco Aurelio',))
conn.commit()

# Consultar autores

result = db.execute('SELECT * FROM authors')
print(result.fetchall())

