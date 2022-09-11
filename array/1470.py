def shuffle(nums: list[int], n: int) -> list[int]:
	ans = []

	for i in range(n):
		ans.extend([nums[i], nums[i + n]])

	return ans


print(shuffle([2, 5, 1, 3, 4, 7], 3))
# https://leetcode.com/problems/shuffle-the-array/
# https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis
