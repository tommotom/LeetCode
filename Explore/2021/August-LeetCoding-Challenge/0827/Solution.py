class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def isSubsequence(word1, word2):
            if len(word1) > len(word2): return False
            i = 0
            for j in range(len(word2)):
                if i < len(word1) and word1[i] == word2[j]: i += 1
            return i == len(word1)

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not isSubsequence(word1, word2) for j, word2 in enumerate(strs) if i!=j): return len(word1)

        return -1
