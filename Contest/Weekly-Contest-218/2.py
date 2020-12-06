from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        stock = defaultdict(lambda: 0)
        ans = 0
        for num in nums:
            if stock[k-num] > 0:
                ans += 1
                stock[k-num] -= 1
            else:
                stock[num] += 1
        return ans
