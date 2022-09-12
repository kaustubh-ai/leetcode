import string


def check_if_pangram(sentence: str) -> bool:
    return set(sentence) == set(string.ascii_lowercase)


print(check_if_pangram('thequickbrownfoxjumpsoverthelazydog'))
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
