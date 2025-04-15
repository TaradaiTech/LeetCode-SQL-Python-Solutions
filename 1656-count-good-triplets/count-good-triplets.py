class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplet_count = 0
        n_elements = len(arr)
        
        # Iterate over all triplets (i, j, k) where i < j < k.
        for i in range(n_elements):
            for j in range(i + 1, n_elements):
                # Check the first condition: |arr[i] - arr[j]| <= a.
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n_elements):
                        # Check the remaining conditions:
                        #   - |arr[j] - arr[k]| <= b
                        #   - |arr[i] - arr[k]| <= c
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplet_count += 1
        
        return good_triplet_count