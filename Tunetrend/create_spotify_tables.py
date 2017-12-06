import json
from DB import DB, DB_NAME

def main():
	db = DB(DB_NAME)
	create_tables(db)
	
def create_tables(db):
	con = db.connection()
	cur = db.cursor()
	
	d1 = 'drop table if exists artists_proper;'
	d2 = 'drop table if exists songs_proper;'

	q1 = 'create table artists_proper(artist_name varchar(255), spotify_identifier varchar(255), artist_id varchar(255), artist_popularity int, artist_followers int, collection_time timestamp without time zone default now());' 
	q2 = 'create table songs_proper(artist varchar(255), artist_id varchar(255), song_name varchar(255), spotify_identifier varchar(255), song_id varchar(255), song_popularity int, collection_time timestamp without time zone default now());'

	for q in [d1, d2, q1, q2]:
		cur.execute(q)
	con.commit()

if __name__ == '__main__':
	main()
