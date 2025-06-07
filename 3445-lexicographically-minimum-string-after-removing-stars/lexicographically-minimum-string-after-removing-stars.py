class Solution:
    def clearStars(self, s: str) -> str:
        if "*" not in s:
            return s
        h = []
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                if not h:
                    continue
                x = h[0]
                if not (v := stacks[x]):
                    continue
                v.pop()
                if not v:
                    heapq.heappop(h)
            else:
                x = ord(c) - 97
                v = stacks[x]
                if not v:
                    heapq.heappush(h, x)
                v.append(i)
        return "".join(s[i] for i in sorted(itertools.chain.from_iterable(stacks)))