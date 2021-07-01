class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i, num in enumerate(nums):
            while ans and len(ans) + (n-i) > k and ans[-1] > num: ans.pop()
            ans.append(num)
        return ans[:k]
