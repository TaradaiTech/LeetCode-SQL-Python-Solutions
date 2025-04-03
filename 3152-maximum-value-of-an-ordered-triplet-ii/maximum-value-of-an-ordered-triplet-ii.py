from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If there are fewer than 3 elements, return 0 (no triplets possible)
        if n < 3:
            return 0

        # Create an array to store the maximum value encountered from the left side for each index
        max_left = [0] * n
        max_left[0] = nums[0]
        
        # Fill the max_left array where each element is the maximum of all previous elements
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])

        # Create an array to store the maximum value encountered from the right side for each index
        max_right = [0] * n
        max_right[-1] = nums[-1]
        
        # Fill the max_right array where each element is the maximum of all subsequent elements
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])

        # Initialize the result variable to store the maximum triplet value
        max_triplet_value = 0
        
        # Iterate through all possible middle elements of the triplet (excluding first and last index)
        for i in range(1, n - 1):
            # For each element at index 'i', calculate the value of the triplet
            left = max_left[i - 1]  # The maximum value to the left of 'i'
            right = max_right[i + 1]  # The maximum value to the right of 'i'
            # Calculate the triplet value and update the result if it's greater than the current maximum
            max_triplet_value = max(max_triplet_value, (left - nums[i]) * right)

        return max_triplet_value