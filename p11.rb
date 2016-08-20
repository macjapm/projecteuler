#Author : Mackenzie Park-McInnes
#Title : P11
#Purpose : Solve 'projecteuler.net' archived problem 11

def v(x, y, arr)
	prd = 1
	if y > 16 == false
		for rep in 1..4
			prd *= (arr[x + (y*19)]).to_i
			y += 1
		end
	end
	return prd
end

def h(x, y, arr)
	prd = 1
	if x > 16 == false
		for rep in 1..4
			prd *= (arr[x + (y*19)]).to_i
			x += 1
		end
	end
	return prd
end

def ld(x, y, arr)
	prd = 1
	if x > 16 || y > 16 == false
		for i in 1..4
			prd *= (arr[x + (y*19)]).to_i
			x += 1
			y += 1
		end
	end
	return prd
end

def rd(x, y, arr)
	prd = 1
	if x > 19 || y > 19 == false
		for i in 1..4
			prd *= (arr[x + (y*19)]).to_i
			x -= 1
			y += 1
		end
	end
	return prd
end

def prd(i, j, arr, l)

	p = (h(i, j, arr))
	l = p > l ? p : l

	p = v(i, j, arr)
	l = p > l ? p : l

	p = ld(i, j, arr)
	l = p > l ? p : l

	p = rd(i, j, arr)
	l = p > l ? p : l

	return l
end

lrg = 0
fd = File.open("p11.txt")
data = ""
fd.each do |line|
	data.concat(line)
end
data.sub("\n","")
elem = data.scan(/[\d]{2}/)

for i in 0..19
	for j in 0..19
		lrg = prd(i, j, elem, lrg)
	end
end

puts lrg
