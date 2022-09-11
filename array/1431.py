def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
	high_enough = max(candies) - extra_candies

	return [i >= high_enough for i in candies]


print(kids_with_candies([2, 3, 5, 1, 3], 3))
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
