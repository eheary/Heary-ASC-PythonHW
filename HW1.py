#!/usr/bin/python

from sys import argv

script, first, second, third = argv

with open("customers.txt", "a") as myfile:
	line1 = first
	line2 = second
	line3 = third

	myfile.write(line1)
	myfile.write(line2)
	myfile.write(line3)

	myfile.close()

print "%s %s %s" % (first,second,third)

