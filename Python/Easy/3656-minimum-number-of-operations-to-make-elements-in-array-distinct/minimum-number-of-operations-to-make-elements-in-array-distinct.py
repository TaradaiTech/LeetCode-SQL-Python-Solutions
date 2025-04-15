class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Track seen elements from the end of the array
        seen = set()

        # Traverse backwards to identify the earliest point where duplicates exist
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                # Duplicate found — return the number of operations needed to reach index i
                return i // 3 + 1
            seen.add(nums[i])
        
        # No duplicates found — array is already distinct
        return 0
