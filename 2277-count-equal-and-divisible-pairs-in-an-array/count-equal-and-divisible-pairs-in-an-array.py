
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = defaultdict(list)   # nums[i] : [i, i2, i3 ...]
        result = 0

        for i in range(len(nums)):
            for j in index_map[nums[i]]:
                if (i * j) % k == 0:
                    result += 1

            index_map[nums[i]].append(i)

        return result