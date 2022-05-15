class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        special = [bottom-1] + special + [top+1]
        ans = 0
        for i in range(len(special)-1):
            ans = max(ans, special[i+1] - special[i] - 1)
        return ans
