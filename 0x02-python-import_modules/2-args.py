#!/usr/bin/python3
import sys
num = len(sys.argv[1:])
if num > 1:
	print("{:d} arguments:".format(num, end=""))
elif num == 1:
	print("{:d} argument:".format(num, end=""))
else:
	print("{:d} arguments.".format(num))
for i in range(1, num+1):
    print("{:d}: {:s}".format(i, sys.argv[i]))
