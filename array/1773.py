def count_matches(items: list[list[str]], rule_key: str, rule_value: str) -> int:
	temp, c = {'type': 0, 'color': 1, 'name': 2}, 0

	for i in items:
		if i[temp[rule_key]] == rule_value:
			c += 1

	return c


print(count_matches(items=[['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']],
					rule_key='color', rule_value='silver'))
# https://leetcode.com/problems/count-items-matching-a-rule/
