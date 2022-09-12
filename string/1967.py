def num_of_strings(patterns: list[str], word: str) -> int:
    return sum(i in word for i in patterns)


print(num_of_strings(['a', 'abc', 'bc', 'd'], 'abc'))
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
