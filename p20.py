#Author : Mackenzie Park-McInnes
#Title : P20
#Purpose : Solve 'projecteuler.net' archived problem 20

#n factorial

n = 100
fprd = 1
fsum = 0
fprdStr = ""

for e in range(1, n):
	fprd *= e

fprdStr = str(fprd)
for char in fprdStr:
	fsum += int(char)

print fprd
print fsum
