class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        q = []
        last = -float('inf')
        for i in range(len(nums)):
            heapq.heappush(q, (nums[i][0], i, 0))
            last = max(last, nums[i][0])

        ans = [q[0][0], last]

        while True:
            num, i, j = heapq.heappop(q)
            if j+1 == len(nums[i]): break
            heapq.heappush(q, (nums[i][j+1], i, j+1))
            last = max(last, nums[i][j+1])
            if ans[1] - ans[0] > last - q[0][0]:
                ans = [q[0][0], last]

        return ans
