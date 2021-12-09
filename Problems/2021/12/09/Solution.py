class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False for _ in range(n)]
        q = deque([start])
        while q:
            i = q.popleft()
            visited[i] = True
            jump = arr[i]
            if jump == 0: return True
            if i-jump >= 0 and not visited[i-jump]:
                q.append(i-jump)
            if i+jump < n and not visited[i+jump]:
                q.append(i+jump)
        return False
