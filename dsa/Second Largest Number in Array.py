def second_largest(arr):
	alpha, beta = float('-inf'), float('-inf')

	for i in arr:
		if i > alpha:
			beta = alpha
			alpha = i
			print(alpha, beta, '1!')
		elif alpha > i > beta:
			beta = i

	return alpha, beta


print(second_largest([-9, 10, 8, 3, -100, 200, 50]))
