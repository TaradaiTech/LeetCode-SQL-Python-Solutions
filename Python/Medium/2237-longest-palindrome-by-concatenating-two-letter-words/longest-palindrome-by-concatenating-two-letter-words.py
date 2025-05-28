class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = [[0] * 26 for _ in range(26)]
        ans = 0

        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if counter[b][a]:
                ans += 4
                counter[b][a] -= 1
            else:
                counter[a][b] += 1

        for i in range(26):
            if counter[i][i]:
                ans += 2
                break

        return ans