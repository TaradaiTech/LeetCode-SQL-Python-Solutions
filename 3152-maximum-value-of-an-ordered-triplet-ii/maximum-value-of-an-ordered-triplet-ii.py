class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Initialize variables to track the highest seen number, the highest difference,
        # and the result (maximum triplet value)
        highest_seen = 0
        highest_diff = 0
        max_triplet_value = 0
        
        # Iterate through each number in the input list
        for num in nums:
            # If the current triplet value (highest_diff * num) is greater than the current result,
            # update the result
            if highest_diff * num > max_triplet_value:
                max_triplet_value = highest_diff * num
            
            # If the difference between the highest seen number and the current number is greater 
            # than the current highest_diff, update highest_diff
            if highest_seen - num > highest_diff:
                highest_diff = highest_seen - num
            
            # If the current number is greater than the highest seen so far, update highest_seen
            if num > highest_seen:
                highest_seen = num
        
        return max_triplet_value