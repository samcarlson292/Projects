import spotipy


sp = spotipy.Spotify()
artist_list = open('artist_list.txt')
full_list = open('full_artist_list.csv', 'w')

# full_list format
# Name, uri, popularity, identifier, followers


# Keep a list of artist IDs
# If the artist found is already in the list, do not add
already_added = []

for artist in artist_list:
	#print artist
	result = sp.search(q='artist:' + artist, type='artist')
	try:
		name = result['artists']['items'][0]['name']
		uri = result['artists']['items'][0]['uri']
		popularity = result['artists']['items'][0]['popularity']
		followers = result['artists']['items'][0]['followers']['total']
		#genres = result['artists']['items'][0]['genres']
		#print str(genres)
		already_added.append(uri[15:])
		identity = uri[15:]
		full_list.write(name + ',' + str(uri) + ',' + str(identity) + ',' + str(popularity) + ',' + str(followers) + '\n')
		related = sp.artist_related_artists(uri)
		for person in related['artists']:
			iden = person['uri'][15:]
			if iden not in already_added:
				already_added.append(iden)
				full_list.write(str(person['name']) + ',' + str(person['uri']) + ',' + str(iden) + ',' + str(person['popularity']) + ',' + str(person['followers']['total']) + '\n')
	except:
		pass


