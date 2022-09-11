def final_value_after_operations(operations: list[str]) -> int:
	ans = 0

	for i in operations:
		if i[0] == '-' or i[-1] == '-':
			ans -= 1
		else:
			ans += 1

	return ans


print(final_value_after_operations(['--X', 'X++', 'X++']))
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
