class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        @lru_cache(None)
        def dp(i, j, k):
            if i == len(robot): return 0
            if j == len(factory): return inf
            res1 = dp(i, j+1, 0)
            res2 = dp(i+1, j, k+1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else inf
            return min(res1, res2)

        return dp(0, 0, 0)
