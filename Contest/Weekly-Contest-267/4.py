class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        group_id = [i for i in range(n)]

        def validation(arr):
            nonlocal restrictions
            for x, y in restrictions:
                if arr[x] == arr[y]: return False
            return True

        ans = []
        for u, v in requests:
            if v < u: u, v = v, u
            tmp = [g for g in group_id]
            for i in range(n):
                if tmp[i] == group_id[v]:
                    tmp[i] = group_id[u]
            if validation(tmp):
                ans.append(True)
                group_id = tmp
            else:
                ans.append(False)

        return ans
