from itertools import accumulate


def max_depth(s: str) -> int:
    return max(accumulate(1 if x == '(' else -1 if x == ')' else 0 for x in s))


print(max_depth('(1+(2*3)+((8)/4))+1'))
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
