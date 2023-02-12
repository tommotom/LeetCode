class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def low(i):
            l, r = i+1, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[i] + nums[m] < lower:
                    l = m + 1
                else:
                    r = m
            return l

        def up(i):
            l, r = i+1, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[i] + nums[m] > upper:
                    r = m
                else:
                    l = m + 1
            return l



        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            l, r = low(i), up(i)
            ans += r - l
        return ans
