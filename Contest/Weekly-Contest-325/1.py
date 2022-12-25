class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        ans = 0
        l = r = startIndex
        while True:
            if words[l] == target or words[r] == target: return ans
            l -= 1
            if l < 0: l += len(words)
            r += 1
            if r == len(words): r = 0
            ans += 1
