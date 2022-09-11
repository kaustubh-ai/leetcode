def count_k_difference(nums: list[int], k: int) -> int:
	return sum(nums[idx:].count(i - k) + nums[idx:].count(i + k) for idx, i in enumerate(nums))


print(count_k_difference([1, 2, 2, 1], 1))
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
