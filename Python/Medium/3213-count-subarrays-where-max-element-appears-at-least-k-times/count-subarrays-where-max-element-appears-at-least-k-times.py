class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        max_num = max(nums)
        left = result = 0

        for num in nums:
            if num == max_num:
                count += 1
            while count >= k:
                if nums[left] == max_num:
                    count -= 1
                left += 1
            result += left

        return result