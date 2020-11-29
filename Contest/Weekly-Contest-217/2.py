class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            while ans and k - len(ans) < len(nums) - i and ans[-1] > nums[i]: ans.pop()
            if len(ans) < k: ans.append(nums[i])
            i += 1
        return ans
