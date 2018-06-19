#!/usr/bin/env python2.7

__counter = 0

def sum(list):
	global __counter
	__counter += 1
	sum = 0

	for this in list:
		sum += this
	return sum

def prodl(list):
	global __counter
	__counter += 1
	prodl = 1

	for this in list:
		prodl *= this
	return prodl

if __name__ == "__main__":
	print("Yeah, activated")
	l = [i + 1 for i in range(5)]
	print(sum(1) == 15)
	print(prodl == 120)
