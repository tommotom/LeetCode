class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(n)]
        count = 0
        ans = []
        for i, c in queries:
            if arr[i] == c:
                ans.append(count)
                continue

            if i > 0 and arr[i-1] == arr[i] != 0: count -= 1
            if i+1 < n and arr[i] == arr[i+1] != 0: count -= 1
            arr[i] = c
            if i > 0 and arr[i-1] == arr[i]: count += 1
            if i+1 < n and arr[i+1] == c: count += 1

            ans.append(count)
        return ans
