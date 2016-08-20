def horprd(grid, i, j):
	prd = 1
	for l in range(0, 4):
		if i <= 19 and j <= 19:
			prd *= grid[i][j]
			i += 1
			if i >= 20 and j < 19:
				i = 0
				j += 1
		else:
			return 0
	return prd

def verprd(grid, i, j):
	prd = 1
	for l in range(0,4):
		if i <= 19 and j <= 19:
			prd *= grid[i][j]
			j += 1
		else:
			return 0
	return prd

def diaprd(grid, i, j):
	prd = 1
	for l in range(0, 4):
		if i <= 19 and j <= 19:
			prd *= grid[i][j]
			j += 1
			i += 1
			if i >= 20 and j < 19:
				i = 0
				j += 1
		else:
			return 0
	return prd
