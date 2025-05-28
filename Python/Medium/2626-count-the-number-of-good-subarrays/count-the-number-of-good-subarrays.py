from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency = defaultdict(int)
        left = 0
        current_pairs = 0
        good_subarray_count = 0

        for right in range(n):
            # Each time we add a new element, it can pair with all previous identical ones
            current_pairs += frequency[nums[right]]
            frequency[nums[right]] += 1

            # Shrink the window from the left while the condition is satisfied
            while current_pairs >= k:
                # All subarrays starting at current `left` and ending anywhere ≥ right are valid
                good_subarray_count += n - right
                frequency[nums[left]] -= 1
                current_pairs -= frequency[nums[left]]
                left += 1

        return good_subarray_count