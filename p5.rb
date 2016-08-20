#Author : Mackenzie Park-McInnes
#Title : P5
#Purpose : Solve 'projecteuler.net' archived problem 5

td = 1
i = 1

while 1 do
	for j in 1..20
		if i % j != 0
			td = 0
			break
		end
	end
	if td == 1
		puts "\n", i
		break
	else
		td = 1
		i += 1
	end
end