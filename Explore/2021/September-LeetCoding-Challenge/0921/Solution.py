class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        consecutive = 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                ans = max(ans, consecutive)
                consecutive = 0
        return max(ans, consecutive)
