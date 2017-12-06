import MySQLdb
import spotipy
import io

full_songs = io.open('full_song_list.csv', 'w', encoding='utf8')

sp = spotipy.Spotify()
db = MySQLdb.connect('localhost', 'root', '123456', 'music_info')
cursor = db.cursor()

#queryString = 'SELECT distinct(id)) FROM full_artists;'
#cursor.execute(queryString)
testQueryString = 'SELECT distinct(artistName) from full_artists;'
cursor.execute(testQueryString)
data = cursor.fetchall()

for row in data:
        #print row[0]
	results = sp.search(q=row[0], limit=10)
	for i, t in enumerate(results['tracks']['items']):
		#print str(row[0]).encode('utf-8')
		#print unicode(row[0], 'utf8')
		print t['name']
		full_songs.write(row[0] + ',' + t['artists'][0]['id'] + ',' + t['name'] + ',' + t['uri'] + ',' + t['id'] + ',' + str(t['popularity']) + '\n')

cursor.close()
db.close()

print 'DONE!'

