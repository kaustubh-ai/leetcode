def running_sum(nums: list[int]) -> list[int]:
	sigma, ans = 0, []

	for i in nums:
		ans.append(i + sigma)
		sigma += i

	return ans


print(running_sum([1, 2, 3, 4]))
# https://leetcode.com/problems/running-sum-of-1d-array/
