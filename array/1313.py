def decompress_rle_list(nums: list[int]) -> list[int]:
	ans = []

	for i in range(0, len(nums), 2):
		ans.extend([nums[i + 1]] * nums[i])

	return ans


print(decompress_rle_list([1, 2, 3, 4]))
# https://leetcode.com/problems/decompress-run-length-encoded-list/
