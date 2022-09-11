def maximum_wealth(accounts: list[list[int]]) -> int:
	ans = 0

	for i in accounts:
		present_wealth = sum(i)
		ans = max(ans, present_wealth)

	return ans


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
# https://leetcode.com/problems/richest-customer-wealth/
