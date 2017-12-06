import csv
from DB import DB, DB_NAME

db = DB(DB_NAME)

conn = db.connection()
cur = db.cursor()

full_list = open('full_artist_list.csv')
csv_data = csv.reader(full_list)

for row in csv_data:
	if len(row) == 5:
		cur.execute("INSERT INTO artists_proper(artist_name, spotify_identifier, artist_id, artist_popularity, artist_followers) VALUES(%s, %s, %s, %s, %s)", row)

conn.commit()
cur.close()
conn.close()

print 'DONE!'
