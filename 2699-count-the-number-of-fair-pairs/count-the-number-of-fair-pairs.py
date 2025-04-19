from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Sort to enable binary search on pair sums
        total_fair_pairs = 0
        n = len(nums)

        for i in range(n):
            # For each nums[i], find range of j > i such that:
            # lower <= nums[i] + nums[j] <= upper
            min_required = lower - nums[i]
            max_allowed = upper - nums[i]

            # Binary search for bounds in sorted array starting after i
            left_index = bisect_left(nums, min_required, i + 1)
            right_index = bisect_right(nums, max_allowed, i + 1)

            total_fair_pairs += right_index - left_index

        return total_fair_pairs