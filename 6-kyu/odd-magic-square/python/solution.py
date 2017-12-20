def magicSquare(n):
	if n % 2 == 0:
		return 'Please enter an odd integer.'

	square = [[0] * n for _ in range(n)]
	row = 0
	col = n//2
	square[row][col] = 1

	for i in range(2, n * n + 1):
		if row == 0:
			newRow = n - 1
		else:
			newRow -= 1

		newCol = (col + 1) % n

		if square[newRow][newCol] != 0:
			newRow = row + 1
			newCol = col

		square[newRow][newCol] = i	
		row, col = newRow, newCol

	return square