class Solution:
    @lru_cache(None)
    def splitString(self, s: str) -> bool:
        if s == "": return True
        for i in range(len(s)-1, 0, -1):
            num = int(s[i:])
            j = i-1
            while j >= 0 and int(s[j:i]) <= num+1:
                if int(s[j:i]) == num + 1:
                    if j == 0: return True
                    if self.splitString(s[:i]): return True
                j -= 1
        return False
