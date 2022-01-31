import sqlite3
from random import randint

conn = sqlite3.connect('databases/ship.db')
cursor = conn.cursor()

cursor.execute(f"""
SELECT * FROM ships
WHERE membro1 == 'Pedro' AND membro2 = 'Julia'
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()