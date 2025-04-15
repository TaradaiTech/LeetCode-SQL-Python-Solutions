class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Initialize counter for good triplets.
        good_triplets = 0
        n = len(arr)
        
        # Iterate over all possible triplets with indices i, j, k such that i < j < k.
        for i in range(n):
            for j in range(i + 1, n):
                # Check the first condition: difference between arr[i] and arr[j] must be <= a.
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        # Check the remaining conditions:
                        #   - Difference between arr[j] and arr[k] must be <= b.
                        #   - Difference between arr[i] and arr[k] must be <= c.
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1
                            # \U0001f94b Rock Lee: "Another success from persistence!" \U0001f973
        
        return good_triplets