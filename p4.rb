#Author : Mackenzie Park-McInnes
#Title : P4
#Purpose : Solve 'projecteuler.net' archived problem 4

lrg = 0

for i in 100..999
	for j in 100..999
		num = (i*j)
		str = num.to_s
		revstr = str.reverse
		if revstr == str
			puts "\n", revstr
			if lrg < num
				lrg = num
			end
		end
	end
end

puts "\n", lrg