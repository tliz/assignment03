matrix = [ ['o', 'o', 'x'], ['x', 'o', 'x'], ['o', 'x', 'o'] ]

def checck_rows(matrix):
	for i in matrix:
		if i == ['x', 'x', 'x'] or i == ['o', 'o', 'o']:
			return True
		return False

print checck_rows(matrix)

def check_columns(matrix):

	for col in range(0,3):
		#if [matrix[0][col], matrix[1][col], matrix[2][col]] == ['x', 'x', 'x'] or [matrix[0][col], matrix[1][col], matrix[2][col]] == ['o', 'o', 'o']:	
		if matrix[0][col] == matrix[1][col] == matrix[2][col]:
			return True
	return False

print check_columns(matrix)

def check_diagonals(matrix):
	diag1 = []
	diag2 = []
	for i in range(3):
		diag1.append(matrix[i][i])
		diag2.append(matrix[i][2-i])

	if diag1 == ['x', 'x', 'x'] or diag1 == ['o', 'o', 'o']:
		return True
	elif diag2 == ['x', 'x', 'x'] or diag2 == ['o', 'o', 'o']:
		return True
	else:
		return False

print check_diagonals(matrix)