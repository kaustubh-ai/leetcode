from collections import defaultdict


def count_points(rings: str) -> int:
	comp = defaultdict(set)

	for colour, ring in zip(rings[::2], rings[1::2]):
		comp[ring].add(colour)

	return sum(len(i) == 3 for i in comp.values())


print(count_points('B0B6G0R6R0R6G9'))
# https://leetcode.com/problems/rings-and-rods/
