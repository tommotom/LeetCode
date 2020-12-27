from collections import deque
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        length = len(arr)
        q = deque([(0, 0)])
        visited = [False for _ in range(length)]

        samevalues = defaultdict(list)
        for i, num in enumerate(arr):
            samevalues[num].append(i)


        while q:
            i, step = q.popleft()
            if i == length - 1: return step

            if 0 < i and not visited[i-1]:
                visited[i-1] = True
                q.append((i-1, step+1))
            if i + 1 < length and not visited[i+1]:
                visited[i+1] = True
                q.append((i+1, step+1))

            for j in samevalues[arr[i]]:
                if not visited[j]:
                    visited[j] = True
                    q.append((j, step+1))
            del samevalues[arr[i]]

        return -1
