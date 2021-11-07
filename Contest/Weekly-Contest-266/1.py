class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def isVowelSubstring(word):
            exists = {'a': False, 'i': False, 'u': False, 'e': False, 'o': False}
            for w in word:
                if w not in exists: return False
                exists[w] = True
            return all(exists.values())

        ans = 0
        for i in range(len(word)-1):
            for j in range(i+1, len(word)):
                if isVowelSubstring(word[i:j+1]):
                    ans += 1
        return ans
