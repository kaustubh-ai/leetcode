def restore_string(s: str, indices: list[int]) -> str:
	return ''.join(s[indices.index(idx)] for idx, i in enumerate(indices))


print(restore_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]))
# https://leetcode.com/problems/shuffle-string/
