class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, words = set(), set()
        for i in range(9, len(s)):
            if s[i-9:i+1] in words: ans.add(s[i-9:i+1])
            words.add(s[i-9:i+1])
        return ans
