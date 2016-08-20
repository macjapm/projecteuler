#Author : Mackenzie Park-McInnes
#Title : P1
#Purpose : Solve 'projecteuler.net' archived problem 1

i = 1
sum = 0
while i < 1000 do
	if i % 3 == 0 || i % 5 == 0
		sum += i
	end
	i+=1
end
puts sum