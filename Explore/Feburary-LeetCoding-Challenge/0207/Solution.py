class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        found = False
        dist = float('inf')
        ans = [dist for _ in range(len(s))]
        for i, char in enumerate(s):
            if char == c:
                dist = 0
                d = 1
                idx = i-1
                while idx >= 0 and ans[idx] > d:
                    ans[idx] = d
                    d += 1
                    idx -= 1
            ans[i] = dist
            dist += 1
        return ans
