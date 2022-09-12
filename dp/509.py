from functools import cache


@cache
def fib(n: int) -> int:
	return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(100))
# https://leetcode.com/problems/fibonacci-number/
