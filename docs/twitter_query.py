import sqlite3

# Connecting to the database file
sqlite_file = '/Users/toregozhinaaizhan/projects/database_ck_workshop/database_ck_workshop/docs/example.sqlite'
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

cursor.execute('select * from result WHERE rowid=15')
for records in cursor.fetchall():
  print(records)
connection.close()

#cursor.execute('select * FROM result WHERE created_at BETWEEN "2014-09-11" AND "2014-10-11"')
#date_times = c.fetchall()
#print ('all entries between Sep and Oct of 2014:', date_times)  

#cursor.execute('select * FROM result WHERE rowid BETWEEN 15 AND 20')
#cursor.execute('select * FROM result WHERE retweeted_status MATCH "THIS IS A RETWEET"')
#cursor.execute('select * FROM result WHERE query="bgolder"')    
