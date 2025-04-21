class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        # Let's track the running sum of differences to reconstruct possible sequence ranges
        running_total = 0  # Starting from 0
        min_val = 0        # Tracks the minimum value seen so far
        max_val = 0        # Tracks the maximum value seen so far

        for d in diff:
            running_total += d
            min_val = min(min_val, running_total)
            max_val = max(max_val, running_total)

        # The sequence will range from [start, start + running_total]
        # So we need to shift the range to fit entirely inside [lower, upper]
        # The available room for shifting = (upper - lower) - (max_val - min_val)
        max_valid_starting_values = (upper - lower) - (max_val - min_val) + 1

        return max(0, max_valid_starting_values)