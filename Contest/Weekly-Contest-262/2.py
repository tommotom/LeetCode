class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        arr.sort()

        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) % x != 0: return -1

        base = arr[len(arr)//2]
        ans = 0
        for num in arr:
            ans += abs(num - base) // x
        return ans
