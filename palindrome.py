#!/usr/bin/env python

n = raw_input("Etner a string: ")

length = len(n)

for i in range(0,(length/2)+1):
	if n[i] != n[-i-1]:
		break

if i < (length/2):
	print "Not a palindrome"
else:
	print "Palindrome"




