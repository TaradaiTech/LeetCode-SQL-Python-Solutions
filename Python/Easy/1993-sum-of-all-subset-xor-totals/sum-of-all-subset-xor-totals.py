class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Compute the bitwise OR of all elements in nums.
        bitwise_or = reduce(or_, nums)
        # Multiply by 2^(n-1) to account for each subset's contribution.
        return bitwise_or << (len(nums) - 1)