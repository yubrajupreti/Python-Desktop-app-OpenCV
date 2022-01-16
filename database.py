import sqlite3

conn = sqlite3.connect('hito_login.db')
c=conn.cursor()


def create_user_table():
    c.execute("""CREATE TABLE IF NOT EXISTS User(full_name TEXT, email TEXT, phone INTEGER, username TEXT, address TEXT, password TEXT )""")

def create_knownface_table():
    c.execute("""CREATE TABLE IF NOT EXISTS known_face(id INTEGER PRIMARY KEY AUTOINCREMENT, image BLOB,  username TEXT , CONSTRAINT fk_User FOREIGN KEY (username) REFERENCES User(username))""")

create_user_table()
# create_knownface_table()