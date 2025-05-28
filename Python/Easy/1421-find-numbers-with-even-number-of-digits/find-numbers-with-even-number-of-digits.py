class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if not len(str(num)) % 2 :
                ans += 1
        return ans