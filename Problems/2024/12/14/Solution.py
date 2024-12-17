class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        q = deque([])
        maxs, mins = [], []
        ans = valid = 0
        for i, num in enumerate(nums):
            q.append((num, i))
            heapq.heappush(maxs, (-num, i))
            heapq.heappush(mins, (num ,i))
            while mins[0][0] < num - 2:
                _, j = heapq.heappop(mins)
                valid = max(valid, j+1)
            while -maxs[0][0] > num + 2:
                _, j = heapq.heappop(maxs)
                valid = max(valid, j+1)
            while q[0][1] < valid:
                q.popleft()
            ans += len(q)
        return ans
