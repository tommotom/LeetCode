class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def isSubstring(pattern, word):
            n = len(pattern)
            for i in range(len(word)-n+1):
                if word[i:i+n] == pattern:
                    return True
            return False

        ans = 0
        for pattern in patterns:
            if isSubstring(pattern, word):
                ans += 1
        return ans
