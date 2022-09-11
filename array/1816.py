def truncate_sentence(s: str, k: int) -> str:
	c, ans = 0, ''

	for i in f'{s} ':
		if i == ' ':
			c += 1
			if c == k:
				return ans

		ans += i


print(truncate_sentence('Hello how are you Contestant', 4))
# https://leetcode.com/problems/truncate-sentence/
