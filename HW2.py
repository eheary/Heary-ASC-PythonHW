#!/usr/bin/python

width = float(input('Enter width: '))
height = float(input('Enter Height: '))

print "Do you want area [1] or perimeter [2]"
input = int(raw_input("> "))

while (input != 1 and input != 2):
        print "please enter [1] or [2]"
        input = int(raw_input("> "))

if input == 1:
	area = width * height
	print "area is %.2f" %area

elif input == 2:
	perimeter = 2 * (width + height)
	print "permeter is %.2f" %perimeter
