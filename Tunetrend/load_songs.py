import csv
from DB import DB, DB_NAME

full_song_list = open('full_song_list.csv')
csv_song_data = csv.reader(full_song_list)

db = DB(DB_NAME)

conn = db.connection()
cur = db.cursor()

for row in csv_song_data:
	if len(row) == 6:
		cur.execute("INSERT INTO songs_proper(artist, artist_id, song_name, spotify_identifier, song_id, song_popularity) VALUES(%s, %s, %s, %s, %s, %s)", row)

conn.commit()
cur.close()

print 'DONE!'
