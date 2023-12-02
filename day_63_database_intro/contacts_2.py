import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = new_email@email.com
phone = input("please enter the phone number: ")

# update_sql = f"UPDATE contacts SET email = {new_email} WHERE phone = {phone}"
# the above method makes the code vulnerable for sql injection attack

update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print(f"{update_cursor.rowcount} rows update")

# cursor should be used to commit the changes
update_cursor.connection.close()
update_cursor.close()

for name, phone, email in db.execute('SELECT * FROM contacts'):
    print(name)
    print(phone)
    print(email)
    print('_' * 20)

# either this will be printed or the code above will be printed
for row in db.execute('SELECT * FROM contacts'):
    print(row)
