class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i, j in enumerate(words):
            for cha in j:
                if cha == x:
                    res.append(i)
                    break
        return res