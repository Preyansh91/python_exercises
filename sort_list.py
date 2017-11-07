#!/usr/bin/env python

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []


'''try this with merge sort. Merge sort does logn because each step of merge doubles the size. It does n work for each merge step because it must look at every item. so O(n log n)'''
def Merge_Sort(A):
	merge_sort2(A,0,len(A) - 1)

def merge_sort2(A,first,last):
	if first < last:
		middle = (first + last) // 2
		print first, middle, last
		merge_sort2(A,first,middle)
		merge_sort2(A,middle+1,last)
		merge(A,first,middle,last)


def merge(A,first,middle,last):
	L = A[first:middle+1]
	R = A[middle+1:last+1]
	L.append(999999999)
	R.append(999999999)
	print L
	print R
	i = j = 0
	for k in range(first,last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1	



def new_mergesort(alist):
	print ("splitting", alist)
	if len(alist) > 1:
		mid = len(alist) // 2
		print mid
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		print lefthalf
		print righthalf

		new_mergesort(lefthalf)
		new_mergesort(righthalf)

		i = j = k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1
		
		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
		
	print ("Merging", alist)


def Quicksort():
	'''O(n log n)'''
	


A = [5,9,1,2,4,8,6,3,7]
new_mergesort(A)
print A
