import sqlite3
from random import randint

conn = sqlite3.connect('databases/ship.db')
cursor = conn.cursor()

nome1 = input('Nome 1: ')
nome2 = input('Nome 2: ')
porcent = randint(0,100)

cursor.execute(f"""
INSERT INTO ships (membro1, membro2, porcentagem)
VALUES (?,?,?)
""", (nome1, nome2, porcent)) 
conn.commit()

print('Table criada com sucesso.')

conn.close()