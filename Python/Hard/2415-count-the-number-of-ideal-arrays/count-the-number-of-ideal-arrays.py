MODULO = int(1e9 + 7)
MAX_VALUE = 10_000

# Precompute number of strictly increasing multiplicative sequences
# STRICT_COUNTS[k][v] will hold number of multiplicative sequences of length k+1 ending with a number ≤ v
STRICT_COUNTS = [[i + 1 for i in range(MAX_VALUE)]]

prev_row = [1] * MAX_VALUE  # Sequences of length 1 — all ones
next_row = [0] * MAX_VALUE
prev_base = 1  # Smallest value in current level of sequences

while (prev_base << 1) <= MAX_VALUE:
    next_base = prev_base << 1  # Double the base each level (sequence length increases)
    
    # Reset the next_row buffer
    for i in range(next_base - 1, MAX_VALUE):
        next_row[i] = 0
    
    # Build multiplicative extensions of sequences
    for prev_num in range(prev_base, MAX_VALUE + 1):
        prev_count = prev_row[prev_num - 1]
        for mult in range(2, MAX_VALUE + 1):
            product = prev_num * mult
            if product > MAX_VALUE:
                break
            next_row[product - 1] = (next_row[product - 1] + prev_count) % MODULO

    # Convert to prefix sums for faster range queries
    current_counts = [next_row[next_base - 1]]
    for next_num in range(next_base, MAX_VALUE):
        current_counts.append((current_counts[-1] + next_row[next_num]) % MODULO)

    STRICT_COUNTS.append(current_counts)

    # Prepare for next round
    prev_base = next_base
    prev_row, next_row = next_row, prev_row  # Swap buffers

# Main function
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        result = 0
        combo = 1  # C(n-1, 0)
        top = n - 1
        bottom = 1
        base = 1

        # Iterate over sequence lengths from 1 to min(n, max chain length)
        for k in range(min(n, len(STRICT_COUNTS))):
            if base <= maxValue:
                # Add count of sequences of length (k+1) ending with value ≤ maxValue
                result = (result + combo * STRICT_COUNTS[k][maxValue - base]) % MODULO
            else:
                break

            # Update binomial coefficient C(n-1, k+1) = C(n-1, k) * (top)/(bottom)
            combo = combo * top // bottom
            top -= 1
            bottom += 1
            base <<= 1  # base *= 2

        return result