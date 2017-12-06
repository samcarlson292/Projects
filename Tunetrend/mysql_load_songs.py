import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "123456", "music_info")
cursor = db.cursor()

full_song_list = open('full_song_list.csv')
csv_song_data = csv.reader(full_song_list)

for row in csv_song_data:
	if len(row) == 6:
		#print row
		cursor.execute("INSERT INTO songs_proper(artist, artistID, songName, spotifyInfo, songID, songPopularity) VALUES(%s, %s, %s, %s, %s, %s)", row)

db.commit()
cursor.close()
db.close()

print 'DONE!'
