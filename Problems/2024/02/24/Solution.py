class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(set)
            for x, y, _ in grp:
                graph[x].add(y)
                graph[y].add(x)

                if x in can: queue.add(x)
                if y in can: queue.add(y)

            queue = deque(queue)
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if not v in can:
                        can.add(v)
                        queue.append(v)
        return can
