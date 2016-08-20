#Author : Mackenzie Park-McInnes
#Title : P9
#Purpose : Solve 'projecteuler.net' archived problem 9

import sys

for a in range(1, 1000):
	for b in range(a+1, 1000):
		for c in range(b+1, 1000):
			sum = a**2 + b**2
			if sum == c**2:
				if a + b + c == 1000:
					print "%d\n%d\n%d" % (a, b, c)
					product = a * b * c
					print product
					sys.exit("Success")
