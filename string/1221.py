from itertools import accumulate


def balanced_string_split(s: str) -> int:
	return list(accumulate(map({'L': 1, 'R': -1}.get, s))).count(0)


print(balanced_string_split('RLRRLLRLRL'))
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
