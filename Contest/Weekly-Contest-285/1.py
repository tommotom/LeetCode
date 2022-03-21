class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        compress = [nums[0]]
        for num in nums[1:]:
            if compress[-1] == num:
                continue
            compress.append(num)

        ans = 0
        for i in range(1, len(compress)-1):
            if compress[i-1] < compress[i] > compress[i+1]: ans += 1
            if compress[i-1] > compress[i] < compress[i+1]: ans += 1

        return ans
