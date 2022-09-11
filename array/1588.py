def sum_odd_length_subarrays(arr: list[int]) -> int:
	ans, size = 0, len(arr)

	for idx, i in enumerate(arr):
		ans += ((((idx + 1) * (size - idx) + 1) // 2) * i)

	return ans


print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
