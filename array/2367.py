def arithmetic_triplets(nums: list[int], diff: int) -> int:
    return sum(i - diff in nums and i + diff in nums for i in nums)


print(arithmetic_triplets([0, 1, 4, 6, 7, 10], 3))
# https://leetcode.com/problems/number-of-arithmetic-triplets/
