class Solution:
    def checkPartitioning(self, s: str) -> bool:
        for i in range(len(s)-2):
            if s[:i+1] == s[:i+1][::-1]:
                for j in range(i+1, len(s)-1):
                    if s[i+1:j+1] == s[i+1:j+1][::-1]:
                        if s[j+1:] == s[j+1:][::-1]:
                            return True
        return False
