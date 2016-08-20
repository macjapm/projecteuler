fd = open("p13.txt", 'r+')
text = fd.read().replace('\n', '')
num  = text[:50]
sumation = 0

for number in range(0, 100):
	num = long(text[:50])
	text = text[50:]
	sumation += num

sumation = str(sumation)
print sumation[:10]
