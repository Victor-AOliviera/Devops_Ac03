import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE victor (id integer, nome text not null, email text null)''')
c.execute("INSERT INTO victor VALUES (1, 'Victor','Victor.oliveira@aluno.faculdadeimpacta.com')")
c.execute("INSERT INTO victor VALUES (2, 'Augusto', null)")

c.execute('''SELECT * FROM victor''')

for row in c.fetchall():
    print(row)

conn.commit()
conn.close()