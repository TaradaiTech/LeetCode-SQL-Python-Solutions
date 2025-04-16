from functools import cache

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # Count the frequency of each number from 1 to 30.
        frequency = [0] * 31
        for num in nums:
            frequency[num] += 1

        # Build a bitmask for each number in [1, 30] representing its prime factors.
        # Each prime factor is represented by a bit corresponding to that prime.
        # Only numbers with all prime factors distinct are valid;
        # if a number has a repeated factor, its mask remains 0 (invalid for forming a good subset).
        # For number 1, we assign a special non-zero mask (0b10) as a placeholder.
        prime_masks = [0] * 31
        for num in range(1, 31):
            if num == 1:
                prime_masks[num] = 0b10  # Special mask for 1 (does not contribute any prime factor)
            else:
                mask = 0
                temp = num
                for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
                    while temp % prime == 0:
                        # If this prime factor is already recorded, then num has a repeated factor.
                        if (mask >> prime) & 1:
                            break  # repeated factor found; break out immediately
                        mask ^= (1 << prime)  # add this prime factor to the mask
                        temp //= prime
                    else:
                        # Continue checking the next prime if inner loop did not break.
                        continue
                    # If we broke out of the inner loop, break out of the prime loop as well.
                    break
                else:
                    # If no break occurred in the prime loop, set the mask for this number.
                    prime_masks[num] = mask

        @cache
        def count_subsets(num: int, current_mask: int) -> int:
            """
            Recursively compute the number of good subsets using numbers in [num, 30],
            given that current_mask holds the combined prime factors (as bitmask) of chosen numbers.
            A subset is 'good' if its product (ignoring any copies of 1) can be written as a product
            of one or more distinct primes, which is ensured if current_mask > 2 (since 0b10 is the mask for 1).
            """
            if num == 31:
                # Only count the subset if we've included at least one number with actual prime factors.
                return int(current_mask > 2)
            
            # Option 1: Skip the current number.
            total = count_subsets(num + 1, current_mask)
            
            # Option 2: Include current number, if it appears and has a valid prime mask.
            if frequency[num] and prime_masks[num]:
                if num == 1:
                    # For 1, we can choose it in any combination;
                    # including 1's does not affect the product's prime factors.
                    total = (total * (2 ** frequency[num])) % MOD
                elif (current_mask & prime_masks[num]) == 0:
                    # We can include num only if its prime factors do not conflict with those already chosen.
                    total = (total + frequency[num] * count_subsets(num + 1, current_mask | prime_masks[num])) % MOD
            return total % MOD

        # Begin recursion from number 1 with an initially empty prime factor mask (0).
        return count_subsets(1, 0)