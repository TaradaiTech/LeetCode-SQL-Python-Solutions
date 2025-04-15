class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Map each value to its index in nums2
        index_in_nums2 = [0] * n
        for i, val in enumerate(nums2):
            index_in_nums2[val] = i

        # Transform nums1 into the index sequence of nums2
        transformed = [index_in_nums2[val] for val in nums1]

        # Fenwick Tree (Binary Indexed Tree) helpers
        def update(bit, i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        # First pass: count how many values less than transformed[i] we've seen so far
        left_smaller = [0] * n
        bit = [0] * (n + 2)  # 1-indexed BIT
        for i in range(n):
            val = transformed[i]
            left_smaller[i] = query(bit, val)
            update(bit, val + 1, 1)

        # Second pass (reverse): count how many values greater than transformed[i] are after it
        right_larger = [0] * n
        bit = [0] * (n + 2)
        for i in reversed(range(n)):
            val = transformed[i]
            right_larger[i] = query(bit, n) - query(bit, val + 1)
            update(bit, val + 1, 1)

        # Combine results: For each i, treat it as the middle of a triplet
        return sum(left_smaller[i] * right_larger[i] for i in range(n))