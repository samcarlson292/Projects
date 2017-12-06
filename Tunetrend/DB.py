import psycopg2

DB_NAME = 'tuneTrend'

class DB:
	def __init__(self, db_name):
		try:
			self.conn = psycopg2.connect("dbname='%s'" % db_name)
			print 'Connected to tuneTrend.'
		except:
			print 'I am unable to connect to tuneTrend.'
			exit()
		self.cur = self.conn.cursor()
	def cursor(self):
		return self.cur
	def getNewCursor(self):
		return self.conn.cursor()
	def connection(self):
		return self.conn
	def query(self, q):
		self.cur.execute(q)
		return self.cur.fetchall()
