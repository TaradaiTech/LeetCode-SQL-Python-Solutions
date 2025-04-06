class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Get the total number of marbles
        num_marbles = len(weights)
        # If there are only two marbles or the number of bags is equal to the number of marbles,
        # there is no way to distribute, so return 0 (no score difference).
        if num_marbles <= 2 or num_marbles == k:
            return 0
        # Create a list to store the sums of adjacent marbles
        adjacent_sums = [0] * (num_marbles - 1)
        # Calculate the sum of each adjacent pair of marbles
        for i in range(num_marbles - 1):
            adjacent_sums[i] = weights[i] + weights[i + 1]
        # Sort the list of adjacent sums in ascending order
        adjacent_sums.sort()
        # The maximum score is the sum of the largest (k-1) partition sums
        max_score = sum(adjacent_sums[num_marbles - k:])
        # The minimum score is the sum of the smallest (k-1) partition sums
        min_score = sum(adjacent_sums[:k - 1])
        # Return the difference between the maximum and minimum scores
        return max_score - min_score
