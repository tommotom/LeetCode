class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helper(arr):
            length = len(arr)
            if length == 0: return 0
            if length == 1: return arr[0]
            l = r = length // 2
            height = area = arr[l]
            while l > 0 and r < length - 1:
                if arr[l-1] < arr[r+1]:
                    r += 1
                    height = min(height, arr[r])
                else:
                    l -= 1
                    height = min(height, arr[l])
                area = max(area, height * (r - l + 1))
            while l > 0:
                l -= 1
                height = min(height, arr[l])
                area = max(area, height * (r - l + 1))
            while r < length - 1:
                r += 1
                height = min(height, arr[r])
                area = max(area, height * (r - l + 1))
            return max([area, helper(arr[:length//2]), helper(arr[length//2:])])
        return helper(heights)
