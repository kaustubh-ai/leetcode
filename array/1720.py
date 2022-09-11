def decode(self, encoded: list[int], first: int) -> list[int]:
    ans = [first]

    for i in encoded:
        ans.append(ans[-1] ^ i)

    return ans


print(decode([1, 2, 3], 1))
# https://leetcode.com/problems/decode-xored-array/
