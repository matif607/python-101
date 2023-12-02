import sqlite3

db = sqlite3.connect('contacts.sqlite')

name = input("type a name to search for: ")
for rows in db.execute('SELECT * FROM contacts WHERE name = ?', (name, )):
    print(rows)