class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers from 1 to n
        total_sum = n * (n + 1) // 2

        # Count of numbers divisible by m in range [1, n]
        count_divisible = n // m

        # Sum of all numbers divisible by m:
        # m + 2m + 3m + ... + (n//m)m = m * (1 + 2 + ... + n//m)
        divisible_sum = m * count_divisible * (count_divisible + 1) // 2

        # num1 - num2 = (total_sum - divisible_sum) - divisible_sum
        return total_sum - 2 * divisible_sum