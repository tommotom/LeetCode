class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)

        d = list(directions)
        ans = 0
        for i in range(n-1):
            if d[i] == "R" and d[i+1] == "L":
                ans += 2
                d[i] = d[i+1] = "S"

        s = []
        for i in range(n):
            if d[i] == "S":
                s.append(i)

        while s:
            i = s.pop()
            l = r = i
            while r+1 < n and d[r+1] == "L":
                ans += 1
                r += 1
                d[r] = "S"
            while l-1 >= 0 and d[l-1] == "R":
                ans += 1
                l -= 1
                d[l] = "S"
        return ans
