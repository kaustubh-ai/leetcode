def bisect_right(arr, n):
	len_arr = len(arr)
	high, low = len_arr, 0

	while low <= high:
		mid = low + ((high - low) // 2)

		if arr[mid] < n:
			low = mid + 1
		if arr[mid] > n:
			high = mid - 1
		if arr[mid] == n:
			return arr[mid + 1], mid + 1


print(bisect_right([-9, -7, 0, 5, 10, 20], -9))
