from itertools import accumulate

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Prefix sums of the differences, starting with 0 as the first element of the sequence
        pfs = list(accumulate(differences, initial=0))
        
        # Compute the total spread of the sequence
        min_val = min(pfs)
        max_val = max(pfs)
        
        # Number of valid integer values the first number in the sequence can take
        return max(0, (upper - lower) - (max_val - min_val) + 1)