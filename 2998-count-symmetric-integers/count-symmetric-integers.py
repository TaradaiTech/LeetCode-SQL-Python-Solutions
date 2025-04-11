class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num: int) -> bool:
            s = str(num)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            return sum(map(int, s[:mid])) == sum(map(int, s[mid:]))

        # Round low up to next even-length number
        while low <= high and len(str(low)) % 2 != 0:
            low += 1

        count = 0
        for num in range(low, high + 1):
            if len(str(num)) % 2 != 0:
                continue  # early skip, odd-length
            if is_symmetric(num):
                count += 1

        return count