def num_jewels_in_stones(jewels: str, stones: str) -> int:
    return len([i for i in stones if i in jewels])


print(num_jewels_in_stones('aA', 'aAAbbbb'))
# https://leetcode.com/problems/jewels-and-stones/
