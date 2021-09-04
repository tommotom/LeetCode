class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        paths = defaultdict(list)
        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)

        rests = [0 for _ in range(n)]
        zero_to_node = [0 for _ in range(n)]
        visited = set()
        def helper(node, dist):
            nonlocal visited, rests, zero_to_node
            visited.add(node)
            zero_to_node[node] = dist
            ret = 0
            for next_node in paths[node]:
                if next_node in visited: continue
                ret += helper(next_node, dist+1)
            rests[node] = ret
            return ret + 1
        helper(0, 0)

        ans = [-1 for _ in range(n)]
        q = deque([(0, sum(zero_to_node))])
        while q:
            node, current_sum = q.popleft()
            ans[node] = current_sum
            for next_node in paths[node]:
                if ans[next_node] != -1: continue
                q.append((next_node, current_sum + n - 2 * (rests[next_node]+1)))

        return ans
