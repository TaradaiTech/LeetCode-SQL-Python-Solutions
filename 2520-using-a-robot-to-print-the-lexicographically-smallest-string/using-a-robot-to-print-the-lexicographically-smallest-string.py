class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suffix = [''] * n
        min_suffix[-1] = s[-1]

        # Build suffix min array
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        stack = []
        result = []

        for i in range(n):
            stack.append(s[i])

            # While top of stack <= smallest remaining in s
            while stack and (i == n - 1 or stack[-1] <= min_suffix[i + 1]):
                result.append(stack.pop())

        return ''.join(result)