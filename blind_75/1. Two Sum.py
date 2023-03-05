def two_sum(nums, target):
	store = {}

	for idx, i in enumerate(nums):
		if target - i in store:
			return store[target - i], idx

		store[i] = idx


print(two_sum([2, 7, 11, 15], 9))
