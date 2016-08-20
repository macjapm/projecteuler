import re
from p11func import *

#Author : Mackenzie Park-McInnes
#Title : P11
#Purpose : Solve 'projecteuler.net' archived problem 11

rex = re.compile('[0-9]{2}')
fd = open("p11.txt", 'r')
text = fd.read().replace('\n', '')
matches = rex.findall(text)

lrgprd = 0
prds = []
grid = [[0 for x in range(20)] for y in range(20)]

for i in range(0, 20):
	for j in range(0, 20):
		grid[i][j] = int(matches[i + (j*19)])

for j in range(0, 20):
	for i in range(0, 20):
		prds.append(horprd(grid, i, j))
		prds.append(verprd(grid, i, j))
		prds.append(diaprd(grid, i, j))
		print grid[i][j]


for element in prds:
	if element > lrgprd:
		lrgprd = element

print lrgprd
