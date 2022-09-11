def count_consistent_strings(allowed: str, words: list[str]) -> int:
	return sum(set(i).issubset(set(allowed)) for i in words)


print(count_consistent_strings(allowed='ab', words=['ad', 'bd', 'aaab', 'baa', 'badab']))
# https://leetcode.com/problems/count-the-number-of-consistent-strings/
