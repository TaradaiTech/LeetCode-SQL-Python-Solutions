from collections import Counter
from math import factorial, prod

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        Count the number of good n-digit integers.
        A "good" integer is one whose digits can be rearranged to form a k-palindromic number,
        where a k-palindromic number is a palindrome that is divisible by k.
        
        For n = 1, we simply check the single digits 1-9.
        For n > 1, we generate all possible n-digit palindromes by constructing the half part
        and mirroring it (adding a middle digit if n is odd). Then we filter those palindromes
        by checking divisibility by k.
        
        Finally, for each distinct digit frequency pattern (after sorting digits), we count the
        number of unique permutations without leading zeros.
        """
        # Special case: 1-digit numbers
        if n == 1:
            # Only digits 1-9 are valid (no leading zero) – count those divisible by k.
            return sum(num % k == 0 for num in range(1, 10))
        
        # Generate the "half" of the palindrome.
        # For an n-digit number, half_length is n//2.
        # We generate numbers with exactly half_length digits.
        half_length = n // 2
        start = 10 ** (half_length - 1)
        end = 10 ** half_length
        first_halves = [str(num) for num in range(start, end)]
        
        # Construct full palindromic numbers.
        palindromes = []
        if n % 2 == 0:
            # Even length: mirror first_half directly.
            palindromes = [half + half[::-1] for half in first_halves]
        else:
            # Odd length: try every digit (0-9) as the middle digit.
            for middle in map(str, range(10)):
                palindromes.extend([half + middle + half[::-1] for half in first_halves])
        
        # Filter palindromes that are divisible by k.
        valid_palindromes = [p for p in palindromes if int(p) % k == 0]
        
        # Get unique frequency patterns by sorting digits.
        # This way, numbers that are rearrangements of each other yield the same pattern.
        unique_patterns = set(''.join(sorted(p)) for p in valid_palindromes)
        
        total_good_count = 0
        
        # For each unique digit frequency pattern, calculate the number of distinct permutations.
        for pattern in unique_patterns:
            # Create a frequency counter for digits in the pattern.
            digit_freq = Counter(pattern)
            # Total permutations with these digits (without restriction) is:
            total_permutations = factorial(n) // prod(factorial(freq) for freq in digit_freq.values())
            
            # Adjust count to remove numbers with a leading zero.
            if digit_freq.get('0', 0) > 0:
                # Count permutations where '0' is fixed at the first position.
                digit_freq_leading_zero = digit_freq.copy()
                digit_freq_leading_zero['0'] -= 1  # One zero is used as the leading digit.
                invalid_permutations = factorial(n - 1) // prod(factorial(freq) for freq in digit_freq_leading_zero.values())
                total_permutations -= invalid_permutations
            
            total_good_count += total_permutations
        
        return total_good_count