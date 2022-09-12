def generate(num_rows: int) -> list[list[int]]:
	res = [[1] * i for i in range(1, num_rows + 1)]
	for i in range(2, num_rows):
		for j in range(1, i):
			res[i][j] = res[i-1][j-1]+res[i-1][j]
	return res


print(generate(5))
# https://leetcode.com/problems/pascals-triangle/
