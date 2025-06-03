from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def dfs(i):
            total = candies[i]
            status[i] = 0  # Mark as visited (closed again)
            for k in keys[i]:
                status[k] |= 1  # Grant key
                if status[k] == 3:  # If both open and inside now
                    total += dfs(k)
            for j in containedBoxes[i]:
                status[j] |= 2  # Box is now available
                if status[j] == 3:  # If both open and inside now
                    total += dfs(j)
            return total

        result = 0
        for i in initialBoxes:
            status[i] |= 2  # Mark as we have this box
            if status[i] == 3:  # If already open
                result += dfs(i)
        return result