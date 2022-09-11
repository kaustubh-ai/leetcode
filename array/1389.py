def create_target_array(nums: list[int], index: list[int]) -> list[int]:
	ans = []

	for i, j in zip(nums, index):
		ans.insert(j, i)

	return ans


print(create_target_array([0, 1, 2, 3, 4],  [0, 1, 2, 2, 1]))
# https://leetcode.com/problems/create-target-array-in-the-given-order/
