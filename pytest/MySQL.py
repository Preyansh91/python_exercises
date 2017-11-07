import MySQLdb as db
import sys
import os
import re
import MySQLdb.cursors
import json


class SQL(object):
	def __init__(self,*args,**kwargs):
		try:
			self._db_init(*args,**kwargs)
		except db.error:
			print "failed to connect"
			if con:
				con.close()
			return  None

	def _db_init(self,*args,**kwargs):
		con = db.connect("127.0.0.1","root","default","test",local_infile=1)
		self.con = con
		cursor = self.con.cursor()
		cursor.connection.autocommit(True)
		self.cursor = cursor

	def create_table(self):
		try:
			cur = self.con.cursor()
			cur.execute('create table phone (number int(11))')
			out = cur.fetchall()
			print out
			if not out:
				return False
			return out
		except db.error:
			print "Got an exception"
			return False				
		return True

conn = SQL()
conn.create_table()	
