class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr)-1):
            min_diff = min(min_diff, arr[i+1] - arr[i])
        return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == min_diff]
