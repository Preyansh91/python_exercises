

class DB:
	def __init__(self):
		self.connection = Connection()

	def connect(self,connection_string):
		return self.connection

class Connection:
	def __init__(self):
		self.cur = Cursor()

	def cursor(self):
		return self.cur

	def close(self):
		pass

class Cursor():
	def execute(self,query):
		if query == "select id from emp where name=Prey":
			return 123
		elif query == "select id from emp where name=Deep":
			return 789
		else:
			return -1

	def close(self):
		pass
