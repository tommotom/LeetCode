class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(length//2):
            if length % (i+1) != 0:
                continue
            elif s == s[:i+1] * (length // (i+1)):
                return True
        else:
            return False
