class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        n = len(roads) + 1
        q = deque([])
        for i in range(n):
            if len(graph[i]) == 1:
                q.append((i, 1))

        visited = set()
        ans = 0
        people = [1] * n
        while q:
            i, p = q.popleft()
            if i == 0: continue
            j = graph[i].pop()
            graph[j].remove(i)
            ans += math.ceil(p/seats)
            people[j] += p
            if len(graph[j]) == 1:
                q.append((j, people[j]))

        return ans
