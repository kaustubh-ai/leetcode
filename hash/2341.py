from collections import Counter


def number_of_pairs(nums: list[int]) -> list[int]:
	ans1, ans2 = 0, 0

	for v in Counter(nums).values():
		if v % 2 != 0:
			ans2 += 1

		ans1 += (v // 2)

	return [ans1, ans2]


print(number_of_pairs([1, 3, 2, 1, 3, 2, 2]))
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/
