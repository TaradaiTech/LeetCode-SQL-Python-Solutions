from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                dp[i][diff] += cnt + 1
                total += cnt  # Only extend existing sequences (length ≥3)

        return total