class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target: int) -> int:
            top_swaps = bottom_swaps = 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return float('inf')  # Not possible
                if t != target:
                    top_swaps += 1
                if b != target:
                    bottom_swaps += 1
            return min(top_swaps, bottom_swaps)

        candidates = [tops[0], bottoms[0]]
        min_swaps = min(check(candidates[0]), check(candidates[1]))
        return -1 if min_swaps == float('inf') else min_swaps