from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [True] + [False for _ in range(n-1)]
        q = deque([0])
        while q:
            key = q.pop()

            for k in rooms[key]:
                if visited[k]: continue
                visited[k] = True
                q.append(k)

        return all(visited)
