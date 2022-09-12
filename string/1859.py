def sort_sentence(s: str) -> str:
    return ' '.join([i[:-1] for i in sorted(s.split(), key=lambda x: x[-1])])


print(sort_sentence('is2 sentence4 This1 a3'))
# https://leetcode.com/problems/sorting-the-sentence/
