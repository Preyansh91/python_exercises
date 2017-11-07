#!/usr/bin/env python

'''
^ Match beginning of line
$ match end of line
. Matches any character
\s matches whitespace
\S matched anything  but whitespace
* Repeats a character 0 or morre times
*? Repeats a character 0 or more times(non greedy)
+ Repeats a char one or more times
+? Repeated a char one or more times(non greedy)
[aeiou] Matches a single char in listed set
( Indcates where string extraction should start
) Indicates where string extraction should end
'''

import re

def check_for_date(filename):
	fh = open(filename,'r')
	data = fh.read()
	for line in data.splitlines():
		out = re.search(r"([a-zA-Z]+) (\d+)",line)
		print out.group(0)
	fh.close()

def text_match(filename):
	fh = open(filename,'r')
        data = fh.read()
        for line in data.splitlines():
		out = re.search("ab*?",line)
		if out:
			print out.group()

def all_match(filename):
	fh = open(filename,'r')
	data = fh.read()
	matches = re.findall(r"[a-z]+ \d+",data,re.IGNORECASE)
	for match in matches:
		print match


def match_ip_addresses(filename):
	fh = open(filename,'r')
	data = fh.read()
	pat = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
	test = pat.search(data)
	print test
	if test:
		print ("Found a match")
		print test.group(0)


def search_ip_address(filename):
	fh = open(filename,'r')
	for line in fh:
		line = line.rstrip()
		if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line):
			print line

search_ip_address("file.txt")
#check_for_date("file.txt")

#text_match("file.txt")

#match_ip_addresses("file.txt")

