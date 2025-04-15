class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        def count(val: int) -> int:
            # Convert val to string for digit-level comparison.
            val_str = str(val)
            # n = length of the prefix part, where s is the fixed suffix.
            n = len(val_str) - len(s)
            if n < 0:
                # If there aren’t enough digits to even include s, no valid number exists.
                return 0
            
            # Initialize a DP table with dimensions (n+1) x 2
            # dp[i][tight] represents the count of valid ways for positions i..n-1,
            # where 'tight' indicates whether we are still restricted by the prefix of val.
            dp = [[0] * 2 for _ in range(n + 1)]
            
            # Base case: if we've chosen all digits for the prefix, then
            # dp[n][0] = 1 because we're already free,
            # and dp[n][1] depends on whether the suffix part of val is >= s.
            dp[n][0] = 1
            dp[n][1] = int(val_str[n:] >= s)
            
            # Process the prefix digits from rightmost to leftmost.
            for i in range(n - 1, -1, -1):
                # The current digit in val at position i.
                current_digit = int(val_str[i])
                
                # When not restricted by the prefix of val (free state),
                # any digit from 0 to limit is allowed.
                dp[i][0] = (limit + 1) * dp[i + 1][0]
                
                # When the state is tight (restricted by val)
                if current_digit <= limit:
                    # We have two parts:
                    # - Choosing any digit below current_digit (which makes subsequent digits free).
                    # - Choosing exactly current_digit, which keeps it tight.
                    dp[i][1] = current_digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    # If current_digit is larger than limit, all choices are free.
                    dp[i][1] = (limit + 1) * dp[i + 1][0]
            
            # dp[0][1] is the number of powerful integers ≤ val.
            return dp[0][1]
        
        # The total count between start and finish is the difference of counts.
        return count(finish) - count(start - 1)