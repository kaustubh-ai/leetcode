def count_asterisks(s: str) -> int:
	f, ans = 0, 0

	for i in s:
		if i == '|':
			f += 1

		if f % 2 == 0 and i == '*':
			ans += 1

	return ans


print(count_asterisks('l|*e*et|c**o|*de|'))
# https://leetcode.com/problems/count-asterisks/
