class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If all elements are already equal to k
        if all(num == k for num in nums):
            return 0

        # Collect unique values greater than k
        greater_than_k = {num for num in nums if num > k}

        # If there are no elements greater than k OR elements less than k exist, it's invalid
        if not greater_than_k or any(num < k for num in nums):
            return -1

        # Each unique value greater than k requires one operation to bring it down to k
        return len(greater_than_k)