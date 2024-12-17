class Solution:
    def findScore(self, nums: List[int]) -> int:
        used = [False for _ in range(len(nums))]

        q = []
        for i, num in enumerate(nums):
            heapq.heappush(q, (num, i))

        score = 0
        while q:
            num, i = heapq.heappop(q)
            if used[i]: continue
            used[i] = True
            score += num
            if i > 0: used[i-1] = True
            if i+1 < len(nums): used[i+1] = True

        return score
