def max_product_difference(nums: list[int]) -> int:
	nums.sort()

	return nums[-1] * nums[-2] - nums[0] * nums[1]


print(max_product_difference([5, 6, 2, 7, 4]))
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
