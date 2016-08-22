import MySQLdb

class Database:
	def __init__(self, host, user, password, database):
		self._host = host
		self._user = user
		self._password = password
		self._database = database

	def fetchone(self, query):
		db = MySQLdb.connect(self._host, self._user, self._password,
			self._database)
		cursor = db.cursor()
		cursor.execute(query)
		data = cursor.fetchone()
		db.close()
		return data

	def fetchall(self, query):
		db = MySQLdb.connect(self._host, self._user, self._password,
			self._database)
		cursor = db.cursor()
		cursor.execute(query)
		data = cursor.fetchall()
		db.close()
		return data

