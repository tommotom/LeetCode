class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            nonlocal boxes
            if i > j: return 0

            idx = i+1
            count = 1
            while idx <= j and boxes[idx-1] == boxes[idx]:
                idx += 1
                count += 1

            ans = dp(idx, j, 0) + (k+count) ** 2

            for m in range(idx, j+1):
                if boxes[m] == boxes[i]:
                    ans = max(ans, dp(idx, m-1, 0) + dp(m, j, k+count))

            return ans

        return dp(0, len(boxes)-1, 0)
