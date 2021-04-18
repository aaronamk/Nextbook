import sqlite3

conn = sqlite3.connect('database/database.db')
print ("Opened database successfully")
with open('database/schema.sql', mode='r') as f:
    conn.cursor().executescript(f.read())
conn.cursor().executescript('INSERT INTO review (isbn, score) VALUES (1,3);')
conn.cursor().executescript('INSERT INTO review (isbn, score) VALUES (1,4);')
conn.cursor().executescript('INSERT INTO review (isbn, score) VALUES (1,1);')
conn.commit()
print ("Created tables succesfully")
conn.close()

#This file is for creating/updating the database schema
#Uses the schema.sql file under the database folder to update the database.db file
#This WILL clear the database
