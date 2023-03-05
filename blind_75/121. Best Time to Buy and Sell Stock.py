def max_profit(prices):
	left, right, ans = 0, 1, 0

	while left < len(prices) and right < len(prices):
		current_profit = prices[right] - prices[left]

		if current_profit < 0:
			left = right
		else:
			ans = max(ans, current_profit)

		right += 1

	return ans


print(max_profit([7, 1, 5, 3, 6, 4]))
