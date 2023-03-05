def bin_search(arr, k):
	arr_len = len(arr)
	low, high = 0, arr_len

	while low <= high:
		mid = low + ((high - low) // 2)
		print(f'low: {low} | high: {high} | mid: {mid}')

		if arr[mid] == k:
			return k
		if arr[mid] > k:
			high = mid - 1
		if arr[mid] < k:
			low = mid + 1

	return False


print(bin_search([-7, -2, 0, 5, 10, 20], -7))
