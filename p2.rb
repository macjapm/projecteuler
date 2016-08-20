#Author : Mackenzie Park-McInnes
#Title : P2
#Purpose : Solve 'projecteuler.net' archived problem 2

i = 1
j = 1
t = 0
sum = 0
limit = 2000000


while i < limit do
	temp = j
	j += i
	i = temp
	puts j


	if j % 2 == 0
		sum += j
	end
end


puts sum