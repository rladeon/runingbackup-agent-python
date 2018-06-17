import sqlite3
class DbUtils(object):
	def __init__(self,pathdb):
		self._pathdb = ""
		self._conn = None
		self._cursor = None
	@property
	def pathdb(self):
		return self._pathdb
	@pathdb.setter
	def pathdb(self,v):
		self._pathdb = v
	@property
	def conn(self):
		return self._conn
	@conn.setter
	def conn(self,v):
		self._conn = v
	@property
	def cursor(self):
		return self._cursor
	@cursor.setter
	def cursor(self,v):
		self._cursor = self.conn.cursor()
	
	def connectdb(self):
		self.conn = sqlite3.connect(self.pathdb)
	def commit(self):
		self.conn.commit()
	def closeConn(self):
		self.conn.close()