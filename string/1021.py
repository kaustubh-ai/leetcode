def remove_outer_parentheses(s: str) -> str:
	c, ans, f = 0, '', 1

	for idx, i in enumerate(s):
		if i == '(':
			c += 1
		else:
			c -= 1

		if c == 0:
			ans += s[f:idx]
			f = idx + 2

	return ans


print(remove_outer_parentheses('(()())(())'))
# https://leetcode.com/problems/remove-outermost-parentheses/
