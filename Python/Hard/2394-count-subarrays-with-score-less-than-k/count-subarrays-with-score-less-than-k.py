class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        total = 0
        count = 0

        for right in range(n):
            total += nums[right]
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            count += (right - left + 1)
        
        return count