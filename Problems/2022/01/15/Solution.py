class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        for i, a in enumerate(arr):
            graph[a].append(i)

        steps = [None for _ in range(len(arr))]
        steps[0] = 0

        q = deque([0])
        while q:
            u = q.popleft()

            for v in graph[arr[u]]:
                if steps[v] == None:
                    steps[v] = steps[u] + 1
                    q.append(v)
            graph[arr[u]].clear()

            if u > 0 and steps[u-1] == None:
                steps[u-1] = steps[u] + 1
                q.append(u-1)

            if u+1 < len(steps) and steps[u+1] == None:
                steps[u+1] = steps[u] + 1
                q.append(u+1)

        return steps[-1]
