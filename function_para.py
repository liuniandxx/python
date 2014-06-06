#!/usr/bin/python

def print_max(a, b):
	if a > b:
		print a , 'is max'
	elif a == b:
		print a, 'is equal to', b
	else:
		print b, 'is max'

print_max(3 , 4)

x = 5
y = 7
print_max(x , y)
