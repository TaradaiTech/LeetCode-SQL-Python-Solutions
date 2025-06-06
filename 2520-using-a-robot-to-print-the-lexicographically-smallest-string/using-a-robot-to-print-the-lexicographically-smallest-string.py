from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        ctr, lo, t, p = Counter(s), 'a', [], []

        for ch in s:
            t.append(ch)
            ctr[ch] -= 1
            if ctr[ch] == 0:
                del ctr[ch]
            # Update `lo` to the next smallest available char
            if lo != 'z' and lo not in ctr:
                lo = min(ctr, default='z')

            # Write to paper if top of `t` is <= smallest remaining char
            while t and t[-1] <= lo:
                p.append(t.pop())

        return ''.join(p)