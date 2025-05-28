from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        seen = defaultdict(list)
        dp = {}
        ans = 0

        # Pre-fill the seen dict with indices of each number
        for i, num in enumerate(nums):
            seen[num].append(i)

        for i in range(2, len(nums)):
            for j in range(i):
                needed = 2 * nums[j] - nums[i]
                if needed in seen:
                    for k in seen[needed]:
                        if k < j:
                            count = 1 + dp.get((k, j), 0)
                            dp[(j, i)] = dp.get((j, i), 0) + count
                            ans += count

        return ans