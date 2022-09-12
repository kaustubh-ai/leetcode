from collections import Counter


def sort_string(s: str) -> str:
	cnt, ans, asc = Counter(s), [], True
	while cnt:                                                                  # if Counter not empty.
		for c in sorted(cnt) if asc else reversed(sorted(cnt)):                 # traverse keys in ascending/descending order.
			ans.append(c)                                                       # append the key.
			cnt[c] -= 1                                                         # decrease the count.
			if cnt[c] == 0:                                                     # if the count reaches to 0.
				del cnt[c]                                                      # remove the key from the Counter.
		asc = not asc                                                           # change the direction, same as asc ^= True.
	return ''.join(ans)


print(sort_string('aaaabbbbcccc'))
# https://leetcode.com/problems/increasing-decreasing-string/
