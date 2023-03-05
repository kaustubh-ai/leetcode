def max_product_subarray(nums):
	max_prod, min_prod, ans = nums[0], nums[0], nums[0]

	for i in nums[1:]:
		max_prod = max(max_prod, max_prod * i, i)
		min_prod = min(min_prod, min_prod * i, i)


# print(max_product_subarray([2, 3, -2, 4]))
print(max_product_subarray([-1, -3, 10, 0, 60]))
