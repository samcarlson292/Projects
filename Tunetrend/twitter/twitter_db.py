from DB import DB, DB_NAME
def main():
	db = DB(DB_NAME)
	con = db.connection()
	cur = db.cursor()
	text_file = open("twitter_db.txt","w")
	q = 'Select distinct song_name,artist from songs_proper'
        for line in db.query(q):
        	#cur.execute('Insert into twitter_info (song, song_id) VALUES (%s,%s)', (line[0], line[1]))
        	#con.commit()
		#q2 = 'Select * from twitter_info'
		#for line in db.query(q2):
		#print line[0],line[1]
		text_file.write(line[0])
		text_file.write(" ")
		text_file.write(line[1])
		text_file.write("\n")

if __name__ == '__main__':
        main()
