from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        if n < 3:  # If there are less than 3 numbers, return 0 (not enough to form a triplet)
            return 0

        # Create an array to store the maximum value from the left up to index i
        left_max = [0] * n
        left_max[0] = nums[0]  # Initialize the first element
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])  # Store the max seen so far

        # Create an array to store the maximum value from the right up to index i
        right_max = [0] * n
        right_max[-1] = nums[-1]  # Initialize the last element
        for i in range(n - 2, -1, -1):  # Iterate backwards from second last to first
            right_max[i] = max(right_max[i + 1], nums[i])  # Store the max seen so far

        max_triplet_value = 0  # Variable to store the maximum computed value
        
        # Iterate over the middle element of the triplet
        for i in range(1, n - 1):
            left = left_max[i - 1]  # Get the maximum value from the left
            right = right_max[i + 1]  # Get the maximum value from the right
            
            # Compute the triplet value and update the maximum value found
            max_triplet_value = max(max_triplet_value, (left - nums[i]) * right)

        return max_triplet_value  # Return the maximum triplet value found