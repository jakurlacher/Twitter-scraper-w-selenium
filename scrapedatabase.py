import sqlite3
import ast
import re

conn = sqlite3.connect('obamawords.sqlite')
conn2 = sqlite3.connect('everywords.sqlite')
cursor2 = conn2.cursor()
cursor = conn.cursor()

file = 'obama_word_counts'
fhand = open(file, 'r')


inp = fhand.read()

obj = ast.literal_eval(inp)

if isinstance(obj, list) and all(isinstance(i, tuple) for i in obj):
    tuples = obj


word_counts = dict(tuples)
data = [(key, value) for key, value in word_counts.items()]

cursor.executescript('''CREATE TABLE IF NOT EXISTS DBtable (Word TEXT, Frequency INTEGER)''')
cursor.executemany("INSERT INTO DBtable (Word, Frequency) VALUES (?, ?)", data)

#Run the program, comment out everything under "Trump 1", uncomment everything
#under "Obama 2", and then run the program again. This will compare two users.


#TRUMP 1
cursor2.executescript('''CREATE TABLE IF NOT EXISTS DBtable1 (TrumpWord TEXT, TrumpFrequency INTEGER)''')
cursor2.executemany("INSERT INTO DBtable1 (TrumpWord, TrumpFrequency) VALUES(?, ?)", data)

cursor2.execute('''CREATE TABLE IF NOT EXISTS DBtable (Word TEXT, TrumpFrequency INTEGER,  ObamaFrequency INTEGER)''')
cursor2.executemany("INSERT INTO DBtable (Word, TrumpFrequency) VALUES (?, ?)", data)


#OBAMA 2
#cursor2.execute('''CREATE TABLE IF NOT EXISTS DBtable2 (ObamaWord TEXT, ObamaFrequency INTEGER)''')
#cursor2.executemany("INSERT INTO DBtable2 (ObamaWord, ObamaFrequency) VALUES(?, ?)", data)

#cursor2.execute('''CREATE TABLE IF NOT EXISTS DBtable (Word TEXT, TrumpFrequency INTEGER,  ObamaFrequency INTEGER)''')
#cursor2.executemany("INSERT INTO DBtable (Word, ObamaFrequency) VALUES (?, ?)", data)

# Commit the changes
conn.commit()
conn2.commit()
