class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l = 0
        while l < len(fruits) and fruits[l][0] < startPos and (startPos - fruits[l][0]) > k:
            l += 1

        r = l
        point = fruits[l][1] if l < len(fruits) and fruits[l][0] <= startPos and (startPos - fruits[l][0]) <= k else 0
        while r+1 < len(fruits) and fruits[r+1][0] <= startPos:
            r += 1
            point += fruits[r][1]

        ans = point
        steps = startPos - fruits[l][0] if l < len(fruits) else 0
        cur = startPos
        while r+1 < len(fruits) and k >= 2 * (fruits[r+1][0] - startPos):
            r += 1
            steps += 2 * (fruits[r][0] - cur)
            point += fruits[r][1]
            cur = fruits[r][0]

            while steps > k and l+1 < len(fruits) and fruits[l+1][0] <= startPos:
                steps -= fruits[l+1][0] - fruits[l][0]
                point -= fruits[l][1]
                l += 1
            if steps <= k:
                ans = max(ans, point)

        r = len(fruits)-1
        while 0 <= r and startPos < fruits[r][0] and (fruits[r][0] - startPos) > k:
            r -= 1

        l = r
        point = fruits[r][1] if 0 <= r and startPos <= fruits[r][0] and (fruits[r][0] - startPos) <= k else 0
        while 0 <= l-1 and startPos <= fruits[l-1][0]:
            l -= 1
            point += fruits[l][1]

        ans = max(ans, point)
        steps = fruits[r][0] - startPos if 0 <= r else 0
        cur = startPos
        while 0 <= l-1 and k >= 2 * (fruits[l-1][0] - startPos):
            l -= 1
            steps += 2 * (cur - fruits[l][0])
            point += fruits[l][1]
            cur = fruits[l][0]
            while steps > k and 0 <= r-1 and startPos <= fruits[r-1][0]:
                steps -= fruits[r][0] - fruits[r-1][0]
                point -= fruits[r][1]
                r -= 1
            if steps <= k:
                ans = max(ans, point)

        return ans
