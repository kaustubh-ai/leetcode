def repeated_character(s: str) -> str:
	char_int_d = {}

	for i in s:
		char_int_d[i] = char_int_d.get(i, 0) + 1
		if char_int_d[i] == 2:
			return i


print(repeated_character('abccbaacz'))
# https://leetcode.com/problems/first-letter-to-appear-twice/
