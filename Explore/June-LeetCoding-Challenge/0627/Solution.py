class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l2r = [1]
        for i in range(1, n):
            l2r.append((l2r[-1]+1) if ratings[i-1] < ratings[i] else 1)
        r2l = [1]
        for i in range(n-2, -1, -1):
            r2l.append((r2l[-1]+1) if ratings[i] > ratings[i+1] else 1)
        r2l.reverse()

        ans = 0
        for i in range(n):
            ans += max(l2r[i], r2l[i])
        return ans
