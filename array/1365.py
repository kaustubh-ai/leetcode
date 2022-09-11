def smaller_numbers_than_current(nums: list[int]) -> list[int]:
	sort_nums = sorted(nums)
	return [sort_nums.index(i) for i in nums]


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
