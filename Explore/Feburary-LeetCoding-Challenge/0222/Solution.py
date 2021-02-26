class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        n = len(s)
        for word in sorted(sorted(d), key=len, reverse=True):
            m = len(word)
            i = j = 0
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == m: return word

        return ""
