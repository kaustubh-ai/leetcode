def most_words_found(sentences: list[str]) -> int:
	return max(len(i.split()) for i in sentences)


print(most_words_found(['please wait', 'continue to fight', 'continue to win']))
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
