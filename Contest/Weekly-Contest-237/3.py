class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = [(i, task) for i, task in enumerate(tasks)]
        arr.sort(key=lambda x: (x[1][0], x[1][1]))
        time = 0
        idx = 0
        n = len(tasks)
        q = []
        ans = []
        while idx < n or q:
            while idx < n and time >= arr[idx][1][0]:
                heapq.heappush(q, (arr[idx][1][1], arr[idx][0]))
                idx += 1
            if q:
                processing, i = heapq.heappop(q)
                ans.append(i)
                time += processing
            else:
                time = arr[idx][1][0]
        return ans
