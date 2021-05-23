class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        visited = set([0])
        q = collections.deque([0])
        mx = 0
        while q:
            i = q.popleft()
            for j in range(max(i+minJump, mx), min(len(s), i+maxJump+1)):
                if s[j] == "0" and j not in visited:
                    if j == len(s) - 1: return True
                    q.append(j)
                    visited.add(j)
            mx = max(mx, i + maxJump)
        return False
