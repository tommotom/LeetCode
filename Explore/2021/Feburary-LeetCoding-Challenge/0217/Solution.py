class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1

        area = 0
        while i < j:
            tmp = min(height[i], height[j])
            area = max(area, tmp * (j - i))
            if height[i] < height[j]:
                while i < j:
                    i += 1
                    if height[i] > tmp: break
            else:
                while i < j:
                    j -= 1
                    if height[j] > tmp: break

        return area
