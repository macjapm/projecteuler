#Author : Mackenzie Park-McInnes
#Title : P4
#Purpose : Solve 'projecteuler.net' archived problem 4

pal = 0

for i in range(100,999):
	for j in range(100, 999):
		num = i * j
		print "Number = %i Pal = %d" % (num, pal)
		numString = str(num)
		reverseString = numString[::-1]

		if numString == reverseString:
			if num > pal:
				pal = num

print "Final Pal = ", pal
