#Author : Mackenzie Park-McInnes
#Title : P6
#Purpose : Solve 'projecteuler.net' archived problem 6

sumsqu = 0
squsum = 0

for i in 1..100
	sumsqu += i ** 2
	squsum += i
end

squsum = squsum ** 2

diff = squsum - sumsqu
puts diff