import sqlite3

conn = sqlite3.connect('database.db')
print('abriu db corretamente')

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print('TABELA CRIADA!!')
conn.close()