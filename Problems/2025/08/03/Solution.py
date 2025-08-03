class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruits.sort(key = lambda x: x[0])
        n = len(fruits)

        r = n - 1
        while r >= 0 and fruits[r][0] > startPos:
            r -= 1
        l, count = r, 0
        while l >= 0 and startPos - fruits[l][0] <= k:
            count += fruits[l][1]
            l -= 1

        ans = count
        while r + 1 < n:
            r += 1
            count += fruits[r][1]
            trip = 2 * (fruits[r][0] - startPos)
            if trip >= k: break
            while startPos - fruits[l+1][0] > k - trip:
                l += 1
                count -= fruits[l][1]
            ans = max(ans, count)

        l = 0
        while l < n and fruits[l][0] < startPos:
            l += 1
        r, count = l, 0
        while r < n and fruits[r][0] - startPos <= k:
            count += fruits[r][1]
            r += 1

        ans = max(ans, count)
        while l > 0:
            l -= 1
            count += fruits[l][1]
            trip = 2 * (startPos - fruits[l][0])
            if trip >= k: break
            while fruits[r-1][0] - startPos > k - trip:
                r -= 1
                count -= fruits[r][1]
            ans = max(ans, count)

        return ans
