from collections import Counter
from math import comb


def num_identical_pairs(nums: list[int]) -> int:
	c = Counter(nums)

	return sum(comb(i, 2) for i in c.values())


print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
# https://leetcode.com/problems/number-of-good-pairs/
