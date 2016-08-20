#Author : Mackenzie Park-McInnes
#Title P9
#Purpose : Solve 'projecteuler.net' archived problem 9


for a in 1..900
	for b in a+1..900
		for c in b+1..900
			d = a ** 2 + b ** 2
			if d == c ** 2
				t = a+b+c
				if t == 1000
					puts (a*b*c)
					break
				end
			end
		end
	end
end