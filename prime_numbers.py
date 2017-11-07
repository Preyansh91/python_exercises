#!/usr/bin/env python



def find_prime(number):
	if number <= 2:
		return False
	is_prime = True
	for factor in range(2,number):
		if number % factor == 0:
			is_prime = False
			return False
	return True	


number = input("Please enter a number: ")

if (find_prime(number) == True):
	print("Number is prime")
else:
	print("Number is not prime")

