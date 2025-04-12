class Solution:
    def factorial(self, number: int) -> int:
        """Compute factorial of a number."""
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    def count_multiset_permutations(self, freqs: list[int], total: int) -> int:
        """
        Count the number of distinct permutations of a multiset.
        Example: For freqs = [f0, f1, ..., f9] and total number of digits = total.
        """
        res = self.factorial(total)
        for f in freqs:
            res //= self.factorial(f)
        return res

    def generate_palindromes(self, n: int, current: list[str], index: int, palindromes: list[str]) -> None:
        """
        Recursively generate all n-digit palindromic numbers.
        
        current: current list of characters (digits) forming the number.
        index: current index to set (we only need to set the first half, then mirror).
        palindromes: list to store the resulting palindrome strings.
        """
        # When the first half is constructed
        if index >= (n + 1) // 2:
            # Mirror the left half to form the palindrome.
            for i in range(n // 2):
                current[n - 1 - i] = current[i]
            palindrome = ''.join(current)
            if palindrome[0] != '0':  # Ensure no leading zero.
                palindromes.append(palindrome)
            return
        
        # For the first position, digits must be 1-9; else, 0-9.
        start_digit = 1 if index == 0 else 0
        for digit in range(start_digit, 10):
            current[index] = str(digit)
            self.generate_palindromes(n, current, index + 1, palindromes)

    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        Count the number of good n-digit integers.
        A good integer's digits can be rearranged to form a k-palindromic number.
        """
        # 1. Generate all n-digit palindromic numbers (without leading zeros)
        palindromes = []
        self.generate_palindromes(n, [''] * n, 0, palindromes)
        
        # 2. Filter valid palindromes: must be divisible by k.
        valid_palindromes = [p for p in palindromes if int(p) % k == 0]
        
        # 3. Convert each valid palindrome to a digit frequency pattern
        freq_patterns = set()
        for num in valid_palindromes:
            freqs = [0] * 10  # Frequency for digits 0-9.
            for ch in num:
                freqs[int(ch)] += 1
            freq_patterns.add(tuple(freqs))  # Use tuple to store immutable frequency pattern.
        
        total_count = 0
        
        # 4. Count permutations for each frequency pattern.
        for pattern in freq_patterns:
            freqs = list(pattern)
            # Total permutations from this multiset.
            perms = self.count_multiset_permutations(freqs, n)
            # Adjust for permutations with a leading zero:
            # If there is at least one '0', count how many permutations have '0' as the first digit.
            if freqs[0] > 0:
                freqs_with_leading_zero = freqs.copy()
                freqs_with_leading_zero[0] -= 1  # Fix a zero at the front.
                invalid_perms = self.count_multiset_permutations(freqs_with_leading_zero, n - 1)
                perms -= invalid_perms
            total_count += perms
        
        return total_count