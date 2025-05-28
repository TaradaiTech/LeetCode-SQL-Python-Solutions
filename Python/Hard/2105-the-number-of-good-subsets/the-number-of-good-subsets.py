from math import prod

MOD = 1_000_000_007

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        # Count frequency of numbers from 1 to 30
        freq = [0] * 31
        for num in nums:
            freq[num] += 1

        # Number of ways to include or exclude 1s (can be in any subset)
        ones_contrib = pow(2, freq[1], MOD)

        # Handle primes with no repeated factors: 17, 19, 23, 29
        large_prime_contrib = prod((freq[p] + 1) for p in (17, 19, 23, 29)) % MOD

        # Build all valid combinations of distinct primes from the small primes
        distinct_prime_groups = [tuple()]
        small_primes = [2, 3, 5, 7, 11, 13]

        for prime in small_primes:
            new_groups = []
            for group in distinct_prime_groups:
                # Add the current prime as a new element
                new_groups.append(group + (prime,))
                # Multiply current prime with each element of the group to form new numbers
                for i, val in enumerate(group):
                    new_number = val * prime
                    new_group = group[:i] + (new_number,) + group[i+1:]
                    new_groups.append(new_group)
            distinct_prime_groups.extend(new_groups)

        # Count how many valid subsets exist for each distinct-prime group
        def group_product_count(group):
            product = 1
            for val in group:
                if val > 30:
                    return 0  # Out of bounds
                product *= freq[val]
            return product % MOD

        subset_count = sum(group_product_count(group) for group in distinct_prime_groups) % MOD

        # Final result = total good subsets * subsets of 1s - invalid empty set
        return ones_contrib * (large_prime_contrib * subset_count % MOD - 1) % MOD