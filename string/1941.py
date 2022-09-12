from collections import Counter


def are_occurrences_equal(s: str) -> bool:
    return len(set(Counter(s).values())) == 1



print(are_occurrences_equal('abacbc'))
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
