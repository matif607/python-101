import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts VALUES('Ayesha', 12345, 'ayesha@email.com')")

cursor = db.cursor()

cursor.execute("SELECT * from contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# if for loop or cursor.fetch runs more than the number of rows, its not going to print the rows again but return
# nothing or none

# to print the rows again we need to execute the code again


for row in cursor:
    print(row)

cursor.close()
# to actually save the changes commit the changes.
db.commit()
db.close()