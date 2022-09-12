def dest_city(paths: list[list[str]]) -> str:
	a, b = map(set, zip(*paths))
	return (b - a).pop()


print(dest_city([['B', 'C'], ['D', 'B'], ['C', 'A']]))
# https://leetcode.com/problems/destination-city/
