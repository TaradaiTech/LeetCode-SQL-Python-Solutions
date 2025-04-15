class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        # If the total sum is odd, it's impossible to split into two equal subsets.
        if total % 2 != 0:
            return False

        target = total // 2

        # Initialize a bitmask where only the 0th bit is set.
        # dp[i] being set means we can form a subset with sum 'i'.
        dp = 1 << 0

        for num in nums:
            # Update the bitmask: for each possible existing sum,
            # mark that we can now also form sum + num
            dp |= dp << num

        # Check if the bit corresponding to the target sum is set
        return (dp >> target) & 1 == 1
