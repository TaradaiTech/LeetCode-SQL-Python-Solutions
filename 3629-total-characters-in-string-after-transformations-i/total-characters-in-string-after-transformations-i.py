class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 26  # count[i] stores how many times char chr(i + ord('a')) appears
        res = len(s)      # initial length of the string
        z = 25            # index for 'z'

        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            res = (res + count[z]) % MOD  # each 'z' adds 1 more char ("ab")
            count[(z + 1) % 26] = (count[(z + 1) % 26] + count[z]) % MOD  # propagate to 'a'
            z = (z + 25) % 26  # move 'z' one step back in circular alphabet

        return res