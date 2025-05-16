from operator import ne

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = []
        for curr_word, curr_group in zip(words, groups):
            best_prev = max(
                (seq for prev_word, prev_group, seq in zip(words, groups, dp)
                 if prev_group != curr_group
                 and len(prev_word) == len(curr_word)
                 and sum(map(ne, prev_word, curr_word)) == 1),
                key=len,
                default=[]
            )
            dp.append(best_prev + [curr_word])
        return max(dp, key=len)