class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ans = sum(int(str(nums[i])+str(nums[n-i-1])) for i in range(n//2))
        return ans if n % 2 == 0 else ans + nums[n//2]
