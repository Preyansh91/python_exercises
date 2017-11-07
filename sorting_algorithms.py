#!/usr/bin/env python


def bubblesort(mylist):
	'''slow sorting algorithm. compares two adjacent items in a list.comlexity O(n^2). we use two loops.'''
	'''outer loop: i = 0  to n-1 '''
	'''inner loop: j = 0 to n-1-i'''
	for i in range(0,len(mylist) - 1):
		for j in range(0,len(mylist) -1 -i):
			if mylist[j] > mylist[j+1]:
				mylist[j],mylist[j+1] = mylist[j+1],mylist[j]

	return mylist


def insertionsort(mylist):
	for i in range(1,len(mylist)):
		key = mylist[i]
		j = i-1
		''' # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position'''
		while j >= 0 and key < mylist[j]:
			mylist[j+1] = mylist[j]
			j -= 1
		mylist[j+1] = key 
	return mylist


def selectionsort(mylist):
	'''first find the smallest item and swap it into the very first position'''
	'''we first take a min value and compare it to all other values and decide min based on that. Swap that min to the min value position'''
	for i in range(len(mylist)):
		min_index = i
		for j in range(i+1,len(mylist)):
			if mylist[min_index] > mylist[j]:
				min_index = j
		mylist[i],mylist[min_index] = mylist[min_index],mylist[i]
		
	return mylist

def mergesort(mylist)L
	

lst = [1,2,3,4,7,5,8]
l = [5,4,3,2,1]

print bubblesort(lst)	
print insertionsort(l)
print selectionsort(l)	
