def build_array(nums: list[int]) -> list[int]:
	size = len(nums)

	for i in range(size):
		nums[i] = size * (nums[nums[i]] % size) + nums[i]

	for i in range(size):
		nums[i] = nums[i] // size

	return nums


build_array([0, 2, 1, 5, 3, 4])
# https://leetcode.com/problems/build-array-from-permutation/
