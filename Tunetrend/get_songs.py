from DB import DB, DB_NAME
import spotipy
import io

full_songs = io.open('full_song_list.csv', 'w', encoding='utf8')
sp = spotipy.Spotify()

db = DB(DB_NAME)

testQueryString = 'SELECT distinct(artist_name) from artists_proper;'
data = db.query(testQueryString)

for row in data:
	results = sp.search(q=row[0], limit=10)
	for i, t in enumerate(results['tracks']['items']):
		print t['name']
		full_songs.write(row[0] + ',' + t['artists'][0]['id'] + ',' + t['name'] + ',' + t['uri'] + ',' + t['id'] + ',' + str(t['popularity']) + '\n')

print 'DONE!'

