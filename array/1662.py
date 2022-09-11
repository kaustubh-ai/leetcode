def array_strings_are_equal(word1: list[str], word2: list[str]) -> bool:
    return ''.join(word1) == ''.join(word2)


print(array_strings_are_equal(['ab', 'c'], ['a', 'bc']))
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
