import sqlite3

#connect to database stored in this file. If the file doesn't exist it will be created.
#The database file will be in the same directory as this program for this example to run.
conn = sqlite3.connect('music.sqlite3') 
cur = conn.cursor() #a file handler

cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

#(?,?) indicates the actual values are passed in as a python tuple
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
	( 'Thunderstruck', 20 ) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
	( 'My Way', 15 ) )
conn.commit()

print 'Tracks:'
cur.execute('SELECT title, plays FROM Tracks')
for row in cur :
	print row
	
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

conn.close()