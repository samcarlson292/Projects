from DB import DB, DB_NAME
from operator import itemgetter

db = DB(DB_NAME)



# Query to find the inidividual artists
query_string = 'SELECT distinct(artist_id) from artists_proper;'
data = db.query(query_string)

# Dictionary to hold changes in popularity
slope_dict = dict()

print 'BEGINNING CALCULATIONS!'

for row in data:
	# Artist name is row[0]
	#print row[0]

	# Clean for apostrophes
	new_artist = row[0].replace("'", "''")
	# Query to find the inidividual songs per artist
	# Possibly should use song_id to avoid multi versioning?????
	song_list_query = "SELECT distinct(song_id), song_name from songs_proper where artist_id like '" + str(new_artist) + "';"
	song_list = db.query(song_list_query)

	# Process each individual song
	for song in song_list:
		# Song name is song[1]
		print str(song[0]) + '\t' + str(song[1])

		# Clean for apostrophes
		new_song = song[1].replace("'", "''")

		popularity_query = "SELECT song_popularity from songs_proper where song_id like '" + str(song[0]) + "' and artist_id like '" + str(new_artist) + "' order by collection_time desc;"
		
		# Find the list of popularities for a given song
		popularity_list = db.query(popularity_query)
		#print 'Popularity list for: ' + str(song[1]) + ' is ' + str(popularity_list) + '.\n'

		# Get the length of the list of popularities
		pop_list_length = len(popularity_list)
		#print 'Length of popularity list: ' + str(pop_list_length) + '.\n'
		

		if pop_list_length > 5:
			# Indexes for continual sum of differences
			prev_index = 0
			second_index = 1
			pop_rate_sum = 0
		
			# For each adjacent pair of elements in the list
			while second_index < pop_list_length:
			
				# Sum the difference
				pop_rate_sum += (popularity_list[prev_index][0] - popularity_list[second_index][0])
				#print 'Total pop_rate_sum: ' + str(pop_rate_sum) + '.\n'
			
				# Increment the indexes accordingly
				second_index += 1
				prev_index += 1

			# Find the average difference
			pop_rate_avg = float(pop_rate_sum) / float(pop_list_length)
			#print 'Average derivative of popularity with respect to time for: ' + str(song[0]) + 'is = ' + str(pop_rate_avg) + '.\n'
		
			# Append to list if enough data
			key = str(song[1]) + " version: " + str(song[0]) + " by artist_id: " + str(row[0])
			slope_dict[str(key)] = pop_rate_avg
		
print 'DONE WITH CALCULATIONS!'

print 'BEGINNING ANALYSIS! \n\n'

# Analyze slope_dict for the proper big movers (up and down)
sorted_slope_dict = sorted(slope_dict.items(), key=itemgetter(1), reverse=True)

for song, slope in sorted_slope_dict:
	if slope > 0:
		#print 'Big Movers Positive ++ ' + str(song) + '\t' + str(slope)
		print 'Big Movers Positive: \t %s with avg. popularity derivative: %s' % (str(song), str(slope))
	elif slope == 0:
		#print 'No Movers ' + str(song) + '\t' + str(slope)
		print 'No Movers: \t %s with avg. popularity derivative: 0' % (str(song))
	else:
		#print 'Big Movers Negative -- ' + str(song) + '\t' + str(slope)
		print 'Big Movers Negative: \t %s with avg. popularity derivative: %s' % (str(song), str(slope))

print '\n'
print 'DONE WITH ANALYSIS!! \n'



print 'DONE!'
