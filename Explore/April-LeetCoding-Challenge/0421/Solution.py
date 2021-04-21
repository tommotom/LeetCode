class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last = triangle[0]
        for i in range(1, len(triangle)):
            last = [min(last[j-1], last[j]) + triangle[i][j] if j > 0 else last[j]+triangle[i][j] for j in range(len(triangle[i])-1)] + [last[-1] + triangle[i][-1]]
        return min(last)
