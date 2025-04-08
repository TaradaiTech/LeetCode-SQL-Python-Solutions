from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Frequency map to count occurrences of each number
        freq = Counter(nums)
        
        # Early exit if array already has all distinct elements
        if all(count == 1 for count in freq.values()):
            return 0

        operations = 0
        index = 0

        # Continue removing chunks of 3 from the front until the array becomes distinct
        while index < len(nums):
            # Determine how many elements to remove (up to 3)
            remove_count = min(3, len(nums) - index)

            # Update frequency map and remove elements
            for i in range(remove_count):
                num = nums[index + i]
                freq[num] -= 1
                if freq[num] == 0:
                    del freq[num]

            index += remove_count
            operations += 1

            # Exit early if the rest is distinct
            if all(count == 1 for count in freq.values()):
                break

        return operations