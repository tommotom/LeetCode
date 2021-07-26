class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])

        @lru_cache(None)
        def score(i, j):
            nonlocal students, mentors
            score = 0
            for k in range(n):
                if students[i][k] == mentors[j][k]:
                    score += 1
            return score

        ans = 0
        def helper(i, used, point):
            nonlocal ans
            if i == m:
                ans = max(ans, point)
                return
            for j in range(m):
                if used[j]: continue
                used[j] = True
                helper(i+1, used, point + score(i, j))
                used[j] = False

        helper(0, [False for _ in range(m)], 0)

        return ans
