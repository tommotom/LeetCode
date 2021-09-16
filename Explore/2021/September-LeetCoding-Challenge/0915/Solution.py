class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        up_end, down_end = [1] * n, [1] * n
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                up_end[i] += down_end[i-1]
            if arr[i-1] > arr[i]:
                down_end[i] += up_end[i-1]

        return max(max(up_end), max(down_end))
