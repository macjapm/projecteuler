#Author : Mackenzie Park-McInnes
#Title : P1
#Purpose : Solve 'projecteuler.net' archived problem 1

sum = 0

for i in range (1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i


print sum
