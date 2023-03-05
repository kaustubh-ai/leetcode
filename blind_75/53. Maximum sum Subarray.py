def max_sum_subarray(nums):
	ans = nums[0]
	sum_so_far = nums[0]

	for i in nums[1:]:
		sum_so_far = max(i, sum_so_far + i)
		ans = max(ans, sum_so_far)

	return ans


print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
