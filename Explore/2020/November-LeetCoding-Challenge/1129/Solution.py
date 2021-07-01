class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        stack = [start]
        while stack:
            idx = stack.pop()
            if arr[idx] == 0: return True
            if idx in visited: continue
            visited.add(idx)
            if idx + arr[idx] < len(arr): stack.append(idx + arr[idx])
            if idx - arr[idx] >= 0 : stack.append(idx - arr[idx])

        return False
