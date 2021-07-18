class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken = set(list(brokenLetters))
        for word in text.split():
            for w in word:
                if w in broken:
                    break
            else:
                ans += 1
        return ans
