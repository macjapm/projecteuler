import re

#Author : Mackenzie Park-McInnes
#Title : P8
#Purpose : Solve 'projecteuler.net' archived problem 8

'''
Given the input file 'p8.txt' find the thirteen adjacent digits
in the 1000-digit number that have the greatest product
'''

#Solution >>>

regex = re.compile(r'[\d]{13}')
fd = open("p8.txt", 'r')
text = fd.read().replace('\n', '')

match = regex.search(text)
matches = []
while match:
	matches.append(match.group())
	text = text[1:]
	match = regex.search(text)

def evaluate_series(list):
	sum = 1
	greatest_product = 0

	for element in matches:
		num = element
		for i in num:
			digit = int(i)
			sum = sum * digit
			if sum > greatest_product:
				greatest_product = sum
		print sum, greatest_product, (sum == greatest_product)
		sum = 1

	return greatest_product

print (evaluate_series(matches))
