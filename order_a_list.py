#!/usr/bin/env python
'''
l = [0,1,2,0,1,2,1,2,2] 
yeh question poocha than
output = [0,0,1,1,1,2,2,2]
in one loop
'''

def get_dict_of_list(l):
	length = len(l)
	num_dict = {}
	for i in l:
		num_dict[i] = num_dict.get(i,0) + 1
	output_sorted_list(num_dict)

def output_sorted_list(ddict):
	output = []
	for key in sorted(ddict.keys()):
		print key, ddict[key]
		output.extend([key] * ddict[key])
	print output





def output_in_place(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			l[i],l[i+1] = l[i+1],l[i]
	print l
		

l = [0,1,2,0,1,2,1,2,2]

output_in_place(l)
#get_dict_of_list(l)
