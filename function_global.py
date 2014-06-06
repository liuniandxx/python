#!/usr/bin/python

x = 50
def func():
	global x

	print 'x is ', x
	x = 2
	print 'Changed global x to', x


func()

print 'value of x is ', x

