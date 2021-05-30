class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []
        for i, s in enumerate(servers):
            heapq.heappush(available, (s, i))

        processing = []
        i = time = 0
        ans = []
        while i < len(tasks):
            while processing and processing[0][0] <= time:
                _, server, idx = heapq.heappop(processing)
                heapq.heappush(available, (server, idx))

            while available and i <= time and i < len(tasks):
                server, idx = heapq.heappop(available)
                heapq.heappush(processing, (time+tasks[i], server, idx))
                ans.append(idx)
                i += 1
            if not available:
                time = processing[0][0]
            else:
                time += 1

        return ans
