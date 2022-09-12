def min_cost_climb_stairs(cost: list[int]) -> int:
	for i in range(2, len(cost)):
		cost[i] = min(cost[i] + cost[i-1], cost[i] + cost[i-2])
	return min(cost[-1], cost[-2])


print(min_cost_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# https://leetcode.com/problems/min-cost-climbing-stairs/
