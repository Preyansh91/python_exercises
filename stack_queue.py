#!/usr/bin/env python

class Stack(object):
	def __init__(self):
		self.data = []
	
	def isEmpty(self):
		if len(self.data) == 0:
			return True
		return False

	def push(self,val):
		self.data.append(val)

	
	def pop(self):
		if not self.isEmpty():
			self.data.pop()

	def size(self):
		return len(self.data)

	def printstack(self):
		for item in  reversed(self.data):
			print item

	

class Queue(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items = []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


	

s = Stack()
print (s.isEmpty())
s.push(2)
print s.data
s.push(4)
print s.data
s.pop()
s.printstack()
	
		


