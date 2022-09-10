def count_bits(n: int) -> list[int]:
	return [bin(i)[2:].count('1') for i in range(n + 1)]


print(count_bits(5))
# https://leetcode.com/problems/counting-bits/
