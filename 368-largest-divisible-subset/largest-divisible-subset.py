from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # If the input list is empty, return an empty list.
        if not nums:
            return []
        
        # Step 1: Sort the numbers in ascending order.
        nums.sort()
        n = len(nums)
        
        # dp[i] will hold the size of the largest divisible subset that ends with nums[i].
        dp = [1] * n  
        # maxi tracks the maximum size of any divisible subset found.
        maxi = 1  
        
        # Step 2: Fill the dp array.
        # For every element, we look at all previous elements to see if the current number is divisible by them.
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] is divisible by nums[j] and update dp[i] accordingly.
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    maxi = max(maxi, dp[i])
        
        # Step 3: Reconstruct the largest divisible subset.
        # We iterate backwards to collect elements of the subset.
        result = []
        prev = -1  # This variable (similar to 'num' in your C++ code) is used to ensure divisibility of chosen elements.
        for i in range(n - 1, -1, -1):
            # If the current element can be part of the subset (it has the current required dp value)
            # and either it's the first element we're picking (prev == -1) or it divides the previously selected element.
            if dp[i] == maxi and (prev == -1 or prev % nums[i] == 0):
                result.append(nums[i])
                prev = nums[i]  # Update the previous element to the current one.
                maxi -= 1     # Decrease the count needed as we've found one element in our subset.
        
        return result