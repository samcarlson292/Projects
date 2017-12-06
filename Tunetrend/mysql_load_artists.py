import MySQLdb
import csv

db = MySQLdb.connect("localhost","root","123456","music_info")
cursor = db.cursor()

full_list = open('full_artist_list.csv')
csv_data = csv.reader(full_list)

for row in csv_data:
	if len(row) == 4:
		#print row
		cursor.execute("INSERT INTO full_artists(artistName, spotifyField, popularity, id) VALUES(%s, %s, %s, %s)", row)

db.commit()
cursor.close()
db.close()

print 'DONE!'
